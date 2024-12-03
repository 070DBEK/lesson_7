from django.shortcuts import render, redirect
from .models import Car


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        Car.objects.create(name=name, model=model, year=year)
        return redirect('car_list')
    return render(request, 'cars/add_car.html')
