from django.shortcuts import render, get_object_or_404, redirect
from .models import Fruit, Cart
from django.http import HttpResponseBadRequest
from django.shortcuts import  redirect


def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def fruit(request):
    fruits = Fruit.objects.all()
    return render(request, 'fruit.html', {'fruits': fruits})

def add_to_cart(request, fruit_id):
    user = request.user
    fruit = get_object_or_404(Fruit, id=fruit_id)
    
    cart_item, created = Cart.objects.get_or_create(user=user, fruit=fruit)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Redirect to the 'cart' view after adding to the cart

    
def cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    
    for item in cart_items:
        item.total_price = item.fruit.price * item.quantity
    
    total_amount = sum(item.total_price for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'cart.html', context)

def remove_from_cart(request, cart_item_id):
    user = request.user
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()  # Save the updated quantity
    else:
        cart_item.delete()

    return redirect('cart')






