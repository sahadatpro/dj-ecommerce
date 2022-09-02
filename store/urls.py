from django.urls import path
from store.views import *

urlpatterns = [
     path('', index, name='store'),
     path('cart/', cart, name='cart'),
     path('checkout/', checkout, name='checkout'),
]