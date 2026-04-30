from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

from apps.models import User


@login_required
def online_shop_viwe(request):
    return render(request, 'online-shop.html')



def login_template_viwe (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            user =queryset.first()
            if check_password(password , user.password):
                login(request, user)
                return redirect('online_shop')
            else:
                return render(request, 'home.html')
    else:
        return render(request, 'login.html')


def register_template_viwe(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(first_name=first_name,email=email)
        user.password =make_password(password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')


def add_to_cart(request, id):
    cart = request.session.get('cart', [])

    if id not in cart:
        cart.append(id)

    request.session['cart'] = cart
    return redirect('online_shop')



def logout_view(request):
    logout(request)
    return redirect('login')



