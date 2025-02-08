from datetime import date

from django import forms
from django.forms import widgets

from .models import Bolsista


class BolsistaForm(forms.ModelForm):

    nome = forms.CharField(
        label='Nome',
        widget=widgets.TextInput(attrs={ 'class': 'form-control' })
    )
    dt_nascimento = forms.CharField(
        label='Data de Nascimento',
        widget=widgets.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'max': date.today()
        })
    )
    nome_mae = forms.CharField(
        label='Nome da mãe',
        widget=widgets.TextInput(attrs={
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label='E-mail',
        widget=widgets.EmailInput(attrs={
            'class': 'form-control'
        })
    )
    cpf = forms.CharField(
        label='CPF',
        widget=widgets.TextInput(attrs={
            'class': 'form-control'
        })
    )
    pis_pasep = forms.CharField(
        label='PIS/PASEP',
        widget=widgets.TextInput(attrs={
            'class': 'form-control'
        })
    )
    dados_bancarios = forms.CharField(
        label='Dados Bancários',
        widget=widgets.TextInput(attrs={
            'class': 'form-control'
        })
    )
    cep = forms.CharField(
        label='CEP',
        widget=widgets.TextInput(attrs={
            'class': 'form-control'
        })
    )
    endereco = forms.CharField(
        label='Endereço',
        widget=widgets.TextInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Bolsista
        fields = '__all__'
