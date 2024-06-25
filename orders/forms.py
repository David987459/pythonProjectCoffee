from django.forms import forms, ModelForm

from orders.models import OrderItem


class OrderItemModelForm(ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'
