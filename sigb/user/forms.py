from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.forms import widgets


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        widget=widgets.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'email@teste.com'
        })
    )
    senha = forms.CharField(
        label='Senha',
        widget=widgets.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'senha'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        senha = cleaned_data.get('senha')
        user = authenticate(username=email, password=senha)
        if not user or not user.is_active:
            raise ValidationError(
                'Login inválido, tente novamente ou entre em contato com o suporte',
                code='invalid'
            )

        return cleaned_data
