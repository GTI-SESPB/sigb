from datetime import date

from django import forms

from ..models.bolsista import Bolsista
from ..models.edital import Edital


__all__ = [
    'BolsistaForm',
    'BolsistaAdminForm',
]


class BolsistaAdminForm(forms.ModelForm):
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


class BolsistaForm(BolsistaAdminForm):
    class Meta(BolsistaAdminForm.Meta):
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'max': date.today().isoformat()
            }),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pis_pasep': forms.TextInput(attrs={'class': 'form-control'}),
            'conta_bancaria': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
            'documentacao': forms.FileInput(attrs={'class': 'form-control'}),
        }


class BolsistaVincularEditalForm(forms.Form):
    edital = forms.ModelChoiceField(
        queryset=Edital.objects.all(),
        widget=forms.Select(attrs={ 'class': 'form-select' })
    )
