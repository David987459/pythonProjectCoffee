from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderItemModelForm


def create_order(request):
    if request.method == 'POST':
        form = OrderItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_summary')
    else:
        form = OrderItemModelForm()
    return render(request, 'orders/create_order.html', {'form': form})

def order_summary(request):
    order_items = OrderItem.objects.all()
    total_cost = sum(item.get_cost() for item in order_items)
    return render(request, 'orders/order_summary.html', {'order_items': order_items, 'total_cost': total_cost})


# Create your views here.
