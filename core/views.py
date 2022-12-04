from django.shortcuts import render, redirect, get_object_or_404
from .models import Parking
from .forms import ParkingForm, PaymentForm
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    search = request.GET.get('search')

    if search:
        parkings = Parking.objects.filter(plate__icontains=search)

    else:
        parkings_list = Parking.objects.filter(left=False)

        paginator = Paginator(parkings_list, 10)

        page = request.GET.get('page')

        parkings = paginator.get_page(page)

    return render(request, 'home/index.html', {"parkings": parkings})


def parkingview(request, id):
    parking = get_object_or_404(Parking, pk=id)
    return render(request, "parking/info.html", {"parking": parking})


def newParking(request):
    if request.method == "POST":
        form = ParkingForm(request.POST)

        if form.is_valid():
            parking = form.save()
            parking.save()
            return redirect('/')
    else:
        form = ParkingForm()
        return render(request, 'parking/add_input.html', {'form': form})


def editParking(request, id):
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


def deleteParking(request, id):
    parking = get_object_or_404(Parking, pk=id)
    parking.delete()

    messages.info(request, 'Entrada deletada com sucesso.')

    return redirect('/')


def outParking(request, id):
    parking = get_object_or_404(Parking, pk=id)

    if parking.paid:
        parking.left = True
        parking.save()
        messages.success(request, 'Saída permitida!')

    else:
        messages.warning(request, 'Saída não permitida. Pagamento em aberto!')

    return redirect('/')


def payParking(request, id):
    parking = get_object_or_404(Parking, pk=id)
    form = PaymentForm(instance=parking)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=parking)

        if form.is_valid():
            parking.save()
            return redirect('/')

    else:
        return render(request, 'parking/edit_parking.html',
                      {'form': form, 'parking': parking})
