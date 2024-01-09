from django.shortcuts import render
from .models import CarModel, Category
# Create your views here.


def index(request):
    category = Category.objects.all()
    car_model = CarModel.objects.all()
    return render(request, 'index.html', context={
            'category':category,
            'car_model':car_model,
    })