from django.shortcuts import render
from .models import User, Order

# Create your views here.


def home_page(request):
    return render(request, 'vegedible/home_page.html')


def orders(request):
    orders = Order.objects.filter(customer=request.user.id)
    context = {
        'orders': orders
    }
    return render(request, 'vegedible/orders.html', context)


def create_order(request):
    return render(request, 'vegedible/create_order.html')
