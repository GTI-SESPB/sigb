from datetime import date

from django import forms

from ..models.bolsista import Bolsista
from ..validators import cpf_validator


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
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'municipio': 'Cidade',
            'uf': 'UF',
            'documentacao': 'Documentação',
        }


class BolsistaForm(BolsistaAdminForm):
    cpf = forms.CharField(
        label='CPF',
        required=True,
        max_length=11,
        validators=[cpf_validator],
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'onkeyup': 'mascaraCPF(event)'
        })
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
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'documentacao': forms.FileInput(attrs={'class': 'form-control'}),
        }
