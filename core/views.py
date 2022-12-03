from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Parking


def home(request):
    plates = Parking.objects.all()
    return render(request, 'index.html', {"plates": plates})


def salvar(request):
    plate = request.POST.get("plate")
    date_input = request.POST.get("date_input")
    Parking.objects.create(plate=plate, date_input=date_input)
    plates = Parking.objects.all()

    return render(request, "index.html", {"plates": plates})


def editar(request, id):
    plate = Parking.objects.get(id=id)
    return render(request, "update.html", {"plate": plate})


def update(request, id):
    vplate = request.POST.get("plate")
    plate = Parking.objects.get(id=id)

    plate.plate = vplate
    plate.save()
    return redirect(home)


def delete(request, id):
    plate = Parking.objects.get(id=id)
    plate.delete()

    return redirect(home)
