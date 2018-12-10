from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib import auth

from cart.cart import Cart
from loginsys.forms import UserCreateProfile, UserPasswordChange
from orders.models import Order, OrderItem
from shop.models import Category


def login(request):
    args = dict()
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['error_login'] = 'Вы ввели не правильный логин или пороль'


    return render(request, 'loginsys/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    args = dict()
    args.update(csrf(request))
    args['form'] = UserCreateProfile()
    if request.POST:
        newuser_form = UserCreateProfile(request.POST)
        if newuser_form.is_valid():
            try:
                newuser_form.save()
            except:
                args['form'] = newuser_form
                return render(request, 'loginsys/register.html', args)
            else:
                newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                            password=newuser_form.cleaned_data['password2'])
                auth.login(request, newuser)
                return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'loginsys/register.html', args)


def password_change(request):
    args = dict()
    args.update(csrf(request))
    if request.user.is_ananymous():
        return redirect('/')
    if request.POST:
        new_pass_ch = UserPasswordChange(user=request.user, data=request.POST)
        if new_pass_ch.is_valid():
            new_pass_ch.save()
            update_session_user_hash(request, new_pass_ch.user)
            return redirect('/')
    else:
        args['form'] = UserPasswordChange(request.user)
    return render(request, 'registration/password_change.html', args)


def password_change_done(request):
    return render(request, 'registration/password_change_done.html')

def personal_area(request):
    orders = Order.objects.filter(user_id=auth.get_user(request).id)
    data = {
        'orders': orders
    }
    return render(request, 'loginsys/personal_area.html', data)
