from datetime import date

from django import forms
from django.forms import widgets

from .models import Bolsista, Bolsa, Edital, BolsistaBolsa


SITUACAO_BOLSISTA = (
    ('', 'Selecionar'),
    ('Ativo', 'Ativo'),
    ('Afastado', 'Afastado'),
    ('Desistente', 'Desistente'),
    ('Desligado', 'Desligado'),
    ('Bolsa Concluída', 'Bolsa Concluída'),
)

class BolsistaForm(forms.ModelForm):
    class Meta:
        model = Bolsista
        fields = '__all__'

        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'dt_nascimento': 'Data de Nascimento',
            'nome_mae': 'Nome da mãe',
            'email': 'E-mail',
            'pis_pasep': 'PIS/PASEP',
            'conta_bancaria': 'Conta Bancária',
            'cep': 'CEP',
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'cidade': 'Cidade',
            'uf': 'UF',
            'documentacao': 'Documentação',
        }

        widgets = {
            'nome': widgets.TextInput(attrs={'class': 'form-control'}),
            'cpf': widgets.TextInput(attrs={'class': 'form-control'}),
            'dt_nascimento': widgets.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'max': date.today().isoformat()
            }),
            'nome_mae': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'pis_pasep': widgets.TextInput(attrs={'class': 'form-control'}),
            'conta_bancaria': widgets.TextInput(attrs={'class': 'form-control'}),
            'cep': widgets.TextInput(attrs={'class': 'form-control'}),
            'logradouro': widgets.TextInput(attrs={'class': 'form-control'}),
            'numero': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cidade': widgets.TextInput(attrs={'class': 'form-control'}),
            'uf': widgets.TextInput(attrs={'class': 'form-control'}),
            'documentacao': widgets.FileInput(attrs={'class': 'form-control'}),
        }


class BolsaForm(forms.ModelForm):
    class Meta:
        model = Bolsa
        fields = '__all__'

        labels = {
            'modalidade': 'Modalidade',
            'carga_horaria': 'Carga horária',
            'valor': 'Valor',
        }

        widgets = {
            'modalidade': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'carga_horaria': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'valor': widgets.NumberInput(attrs={ 'class': 'form-control' }),
        }


class EditalForm(forms.ModelForm):
    class Meta:
        model = Edital
        fields = '__all__'

        labels = {
            'numero': 'Número',
            'vigencia': 'Vigência',
            'descricao': 'Descrição',
        }

        widgets = {
            'numero': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'vigencia': widgets.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }),
            'descricao': widgets.TextInput(attrs={ 'class': 'form-control' }),
        }


class BolsistaBolsaForm(forms.ModelForm):
    edital = forms.ModelChoiceField(
        label='Edital',
        queryset=Edital.objects.all(),
        widget=widgets.Select(attrs={'class': 'form-select'})
    )
    bolsa = forms.ModelChoiceField(
        label='Bolsa',
        queryset=Bolsa.objects.all(),
        widget=widgets.Select(attrs={'class': 'form-select'})
    )
    situacao = forms.ChoiceField(
        label='Situação',
        choices=SITUACAO_BOLSISTA,
        widget=widgets.Select(attrs={'class': 'form-select'})
    )
    class Meta:
        model = BolsistaBolsa
        fields = '__all__'

        labels = {
            'bolsista': 'Bolsista',
            'bolsa': 'Bolsa',
            'funcao': 'Função',
            'dt_desligamento': 'Data de desligamento',
            'vigencia_outorga': 'Vigência da outorgação',
            'data_outorga': 'Data de outorgação',
            'termo_outorga': 'Termo de outorga'
        }

        widgets = {
            'bolsista': widgets.TextInput(attrs={'class': 'form-control'}), 
            'bolsa': widgets.TextInput(attrs={'class': 'form-control'}),
            'funcao': widgets.TextInput(attrs={'class': 'form-control'}),
            'dt_desligamento': widgets.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'max': date.today().isoformat(),
                'disabled': '',
            }),
            'vigencia_outorga': widgets.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'max': date.today().isoformat()
            }),
            'data_outorga': widgets.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'max': date.today().isoformat()
            }),
            'termo_outorga': widgets.FileInput(attrs={'class': 'form-control'}),
        }
