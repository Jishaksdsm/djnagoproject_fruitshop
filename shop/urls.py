from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fruits/', views.fruit, name='fruits'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('add_to_cart/<int:fruit_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
   
]

