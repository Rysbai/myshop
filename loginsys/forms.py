from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailField, TextInput, CharField
from django import forms
from loginsys.models import UserProfile
from django.utils.translation import ugettext, ugettext_lazy as _


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class UserCreateProfile(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username',]
        field_classes = {
            'first_name': CharField,
            'username': EmailField,
            'password1': TextInput,
            'password2': TextInput,
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateProfile, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': "Имя"})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': "Email", 'type': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "Пороль"})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "Потвердите пороль"})


class UserPasswordChange(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control',
                                          'placeholder': "введите старый пороль "}),
    )

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control',
                                          'placeholder': "введите новый пороль"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),

    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control',
                                          'placeholder': "повторите новый пороль"}),
        )
