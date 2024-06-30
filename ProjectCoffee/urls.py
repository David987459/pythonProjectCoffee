"""ProjectCoffee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import viewer
from orders.views import order_summary, create_order
from viewer import views
from viewer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('create/', create_order, name='create_order'),
    path('summary/',order_summary, name='order_summary'),
    path('products/', products, name='products'),
    path('o_nas/', o_nas, name='o_nas')
]

