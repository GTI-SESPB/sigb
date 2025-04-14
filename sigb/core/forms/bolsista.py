from datetime import date

from django import forms

from ..models.bolsista import Bolsista
from ..validators import cpf_validator
from ..utils import apenas_digitos


__all__ = [
    'BolsistaForm',
    'BolsistaAdminForm',
]


class BolsistaAdminForm(forms.ModelForm):
    UF_CHOICES = [
        ('', 'Selecionar'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PR', 'Paraná'),
        ('PB', 'Paraíba'),
        ('PA', 'Pará'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RJ', 'Rio de Janeiro'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    ]

    cpf = forms.CharField(
        label='CPF',
        required=True,
        max_length=11,
        validators=[cpf_validator]
    )
    cep = forms.CharField(
        label='CEP',
        required=True,
        max_length=8,
    )
    municipio = forms.CharField(
        label='Município',
        required=True,
    )
    uf = forms.ChoiceField(
        label='UF',
        required=True,
        choices=UF_CHOICES,
    )

    class Meta:
        model = Bolsista
        fields = '__all__'

        labels = {
            'nome': 'Nome',
            'dt_nascimento': 'Data de Nascimento',
            'nome_mae': 'Nome da mãe',
            'email': 'E-mail',
            'pis_pasep': 'PIS/PASEP',
            'conta_bancaria': 'Conta Bancária',
            'cep': 'CEP',
            'municipio': 'Cidade',
            'uf': 'UF',
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'documentacao': 'Documentação',
        }


class BolsistaForm(BolsistaAdminForm):
    cpf = forms.CharField(
        label='CPF',
        required=True,
        max_length=14,
        validators=[cpf_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'onkeyup': 'mascaraCPF(event)'
        })
    )
    cep = forms.CharField(
        label='CEP',
        required=True,
        max_length=9,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'onkeyup': 'mascaraCEP(event)'
        })
    )
    municipio = forms.CharField(
        label='Município',
        required=True,
        widget=forms.Select(attrs={ 'class': 'form-select' })
    )
    uf = forms.ChoiceField(
        label='UF',
        required=True,
        choices=BolsistaAdminForm.UF_CHOICES,
        widget=forms.Select(attrs={ 'class': 'form-select' })
    )
    
    class Meta(BolsistaAdminForm.Meta):
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'max': date.today().isoformat()
            }),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pis_pasep': forms.TextInput(attrs={'class': 'form-control'}),
            'conta_bancaria': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'documentacao': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_cep(self):
        return apenas_digitos(self.cleaned_data['cep'])

    def clean_cpf(self):
        return apenas_digitos(self.cleaned_data['cpf'])
