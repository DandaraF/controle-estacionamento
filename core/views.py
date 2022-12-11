import random
import string
from datetime import datetime

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .forms import ParkingForm, PaymentForm
from .models import Parking


def random_code(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class ParkingViewSet(viewsets.ViewSet):
    @staticmethod
    def get_parkings(request):
        search = request.GET.get('search')

        if search:
            parkings = Parking.objects.filter(
                plate__icontains=search).order_by("-date_input")

        else:
            parkings_list = Parking.objects.filter(left=False).order_by(
                "-paid")

            paginator = Paginator(parkings_list, 12)

            page = request.GET.get('page')

            parkings = paginator.get_page(page)

        return render(request, 'home/index.html', {"parkings": parkings})

    @staticmethod
    def post(request):
        if request.method == "POST":
            form = ParkingForm(request.POST)

            if form.is_valid():
                parking = form.save()
                parking.code = random_code()
                parking.save()
                return redirect('/')
        else:
            form = ParkingForm()
            return render(request, 'parking/add_input.html', {'form': form})

    @staticmethod
    def update(request, id: int):
        parking = get_object_or_404(Parking, pk=id)
        form = ParkingForm(instance=parking)

        if request.method == 'POST':
            form = ParkingForm(request.POST, instance=parking)
            if form.is_valid():
                print('é valido')
                parking.save()
                return redirect('/')

        else:
            print('não')
            return render(request, 'parking/edit_parking.html',
                          {'form': form, 'parking': parking})

    @staticmethod
    def delete(request, id: int):
        parking = get_object_or_404(Parking, pk=id)
        parking.delete()

        messages.info(request, 'Entrada deletada com sucesso.')

        return redirect('/')

    @staticmethod
    def output(request, id: int):
        parking = get_object_or_404(Parking, pk=id)

        if parking.paid:
            parking.left = True
            parking.date_output = datetime.now()
            parking.save()
            messages.success(request, 'Saída permitida!')

        else:
            messages.warning(request,
                             'Saída não permitida. Pagamento em aberto!')

        return redirect('/')

    @staticmethod
    def payment(request, id: int):
        parking = get_object_or_404(Parking, pk=id)
        form = PaymentForm(instance=parking)

        total_time = parking.total_time(parking.date_input)

        if request.method == 'POST':
            form = PaymentForm(request.POST, instance=parking)

            if form.is_valid():
                parking.paid = True
                form.save()

            return redirect('/')

        else:
            json_data = {'form': form,
                         'parking': parking,
                         'total_time': total_time,
                         'datetime_now': datetime.now()}

            return render(request, 'payment/payment.html', json_data)

    @staticmethod
    def historic(request, plate):
        parkings_filted = Parking.objects.filter(plate=plate).order_by(
            "-date_input")

        parkings = [{"id": p.id,
                     "code": p.code,
                     "plate": p.plate,
                     "client": p.client,
                     "vehicle": p.vehicle,
                     "paid": p.paid,
                     "value": p.value,
                     "date_input": p.date_input,
                     "date_output": p.date_output,
                     "time": p.total_time(p.date_input)}
                    for p in parkings_filted]

        return render(request, 'historic/historic.html',
                      {"parkings": parkings})
