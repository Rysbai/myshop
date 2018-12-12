from django.contrib import auth
from django.shortcuts import redirect
from loginsys.forms import UserCreateProfile

def auth_info(request):
    username = auth.get_user(request).username
    form = UserCreateProfile()

    if request.POST:
        newuser_form = UserCreateProfile(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])

            auth.login(request, newuser)

        else:
            form = newuser_form

    return locals()
