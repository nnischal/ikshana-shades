from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def products(request):
    return render(request, 'core/products.html')

def contact(request):
    return render(request, 'core/contact.html')

def cart(request):
    return render(request, 'core/cart.html')

def checkout(request):
    return render(request, 'core/checkout.html')

def login_view(request):
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')

def orders(request):
    return render(request, 'core/orders.html')
