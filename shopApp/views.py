from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import OrderForm
from django.views.generic import CreateView
from .models import Dish, Room


def home(request):
    return render(request, 'shopApp/home.html')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'shopApp/signup.html'


def order(request):
    default()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            name = order_form.cleaned_data['name']
            date = order_form.cleaned_data['date']
            time = order_form.cleaned_data['time']
            people_num = order_form.cleaned_data['people_num']
            agree = order_form.cleaned_data['agree']
            return redirect('home')
    else:
        order_form = OrderForm()
        dishes = Dish.objects.all()
        rooms = Room.objects.all()
        return render(request, 'shopApp/order.html', {'form': order_form, 'dishes': dishes, 'rooms': rooms})


def default():
    if Dish.objects.all().count() == 0:
        Dish.objects.create(name='pasta')
        Dish.objects.create(name='meat')
        Dish.objects.create(name='soup')
        Dish.objects.create(name='vegetables')
        Dish.objects.create(name='fruits')
    if Room.objects.all().count() == 0:
        Room.objects.create(numberOfRoom=1)
        Room.objects.create(numberOfRoom=2)
        Room.objects.create(numberOfRoom=3)
