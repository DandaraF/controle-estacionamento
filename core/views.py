from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Tuple

from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .models import Parking
from .forms import ParkingForm, PaymentForm
from django.contrib import messages
from django.core.paginator import Paginator


class PaymentViewSet(viewsets.ViewSet):
    @staticmethod
    def amount_to_pay(date_input: datetime, date_now: datetime):

        total_hour = date_now.hour - date_input.hour

        if date_now.date() == date_input and total_hour <= 3:
            if total_hour <= 1:
                return 2, total_hour
            else:
                return 4, total_hour
        else:

            return 10, total_hour


# def home(request):
#     search = request.GET.get('search')
#
#     if search:
#         parkings = Parking.objects.filter(plate__icontains=search)
#
#     else:
#         parkings_list = Parking.objects.filter(left=False)
#
#         paginator = Paginator(parkings_list, 10)
#
#         page = request.GET.get('page')
#
#         parkings = paginator.get_page(page)
#
#     return render(request, 'home/index.html', {"parkings": parkings})


class ParkingViewSet(viewsets.ViewSet):
    @staticmethod
    def get_parkings(request):
        search = request.GET.get('search')

        if search:
            parkings = Parking.objects.filter(plate__icontains=search)

        else:
            parkings_list = Parking.objects.filter(left=False)

            paginator = Paginator(parkings_list, 10)

            page = request.GET.get('page')

            parkings = paginator.get_page(page)

        return render(request, 'home/index.html', {"parkings": parkings})

    @staticmethod
    def post(request):
        if request.method == "POST":
            form = ParkingForm(request.POST)

            if form.is_valid():
                parking = form.save()
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
                parking.save()
                return redirect('/')
            else:
                return render(request, 'parking/edit_parking.html',
                              {'form': form, 'parking': parking})

        else:
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
            parking.save()
            messages.success(request, 'Saída permitida!')

        else:
            messages.warning(request,
                             'Saída não permitida. Pagamento em aberto!')

        return redirect('/')

    @staticmethod
    def payment(request, id: int):
        parking = get_object_or_404(Parking, pk=id)

        date_now = datetime.now()
        date_input = parking.date_input
        amount, total_hour = PaymentViewSet.amount_to_pay(date_input,
                                                          date_now)

        if request.method == 'POST':
            form = PaymentForm(request.POST, instance=parking)

            if form.is_valid():
                parking.value = amount
                parking.paid = True
                parking.save()

                return redirect('/')

        else:
            form = PaymentForm(instance=parking)

            parking.save()
            json_data = {'form': form,
                         'parking': parking,
                         "date_now": date_now.strftime("%d/%m/%Y %H:%M"),
                         "date_input": date_input.strftime("%d/%m/%Y %H:%M"),
                         "total_hour": total_hour,
                         "value": amount}

            return render(request, 'parking/payment.html', json_data)

        # if request.method == 'POST':
        #     form = PaymentForm(request.POST, instance=parking)
        #
        #     if form.is_valid():
        #         parking.save()
        #         return redirect('/')
        #
        # else:
        #     return render(request, 'parking/payment.html',
        #                   {'form': form, 'parking': parking,
        #                    "date_now": date_now, "date_input": date_input})

    @staticmethod
    def historic(request, plate):
        parkings_list = Parking.objects.filter(plate=plate)

        paginator = Paginator(parkings_list, 10)

        page = request.GET.get('page')

        parkings = paginator.get_page(page)

        return render(request, 'parking/historic.html', {"parkings": parkings})

# @staticmethod
# def newParking(request):
#     if request.method == "POST":
#         form = ParkingForm(request.POST)
#
#         if form.is_valid():
#             parking = form.save()
#             parking.save()
#             return redirect('/')
#     else:
#         form = ParkingForm()
#         return render(request, 'parking/add_input.html', {'form': form})
#
#
# def editParking(request, id):
#     parking = get_object_or_404(Parking, pk=id)
#     form = ParkingForm(instance=parking)
#
#     if request.method == 'POST':
#         form = ParkingForm(request.POST, instance=parking)
#
#         if form.is_valid():
#             parking.save()
#             return redirect('/')
#         else:
#             return render(request, 'parking/edit_parking.html',
#                           {'form': form, 'parking': parking})
#
#     else:
#         return render(request, 'parking/edit_parking.html',
#                       {'form': form, 'parking': parking})
#
#
# def deleteParking(request, id):
#     parking = get_object_or_404(Parking, pk=id)
#     parking.delete()
#
#     messages.info(request, 'Entrada deletada com sucesso.')
#
#     return redirect('/')
#
#
# def outParking(request, id):
#     parking = get_object_or_404(Parking, pk=id)
#
#     if parking.paid:
#         parking.left = True
#         parking.save()
#         messages.success(request, 'Saída permitida!')
#
#     else:
#         messages.warning(request, 'Saída não permitida. Pagamento em aberto!')
#
#     return redirect('/')
#
#
# def payParking(request, id):
#     parking = get_object_or_404(Parking, pk=id)
#     form = PaymentForm(instance=parking)
#
#     if request.method == 'POST':
#         form = PaymentForm(request.POST, instance=parking)
#
#         if form.is_valid():
#             parking.save()
#             return redirect('/')
#
#     else:
#         return render(request, 'parking/payment.html',
#                       {'form': form, 'parking': parking})
#
#
# def payment(request, id):
#     parking = Parking.objects.get(id=id)
#     now = datetime.now()
#
#     datetime_payment = now - timedelta(hours=parking.date_input.hour,
#                                        minutes=parking.date_input.minute,
#                                        seconds=parking.date_input.second)
#     total_hour = datetime_payment.hour
#
#     if total_hour <= 1:
#         parking.value = 2
#
#     if 3 >= total_hour > 1:
#         parking.value = 4
#
#     if total_hour > 3:
#         parking.value = 4
#
#     parking.paid = True
#     parking.date_output = now
#     parking.save()
#     return redirect('/')
#
#
# def historicParking(request, plate):
#     parkings_list = Parking.objects.filter(plate=plate)
#
#     paginator = Paginator(parkings_list, 10)
#
#     page = request.GET.get('page')
#
#     parkings = paginator.get_page(page)
#
#     return render(request, 'parking/historic.html', {"parkings": parkings})
