from django import forms
from django.contrib.admin.options import widgets


from ..models.bolsa import Bolsa
from ..models.edital import Edital


class BolsaAdminForm(forms.ModelForm):
    SITUACAO_BOLSISTA = (
        ('', 'Selecionar'),
        ('Ativo', 'Ativo'),
        ('Afastado', 'Afastado'),
        ('Desistente', 'Desistente'),
        ('Desligado', 'Desligado'),
        ('Bolsa Concluída', 'Bolsa Concluída'),
    )

    situacao = forms.ChoiceField(
        label='Situação',
        choices=SITUACAO_BOLSISTA
    )

    class Meta:
        model = Bolsa
        exclude = [ 'bolsista' ]

        labels = {
            'modalidade': 'Modalidade',
            'funcao': 'Função',
            'carga_horaria': 'Carga horária',
            'valor': 'Valor',
            'dt_desligamento': 'Data de desligamento',
            'vigencia_outorga': 'Vigência da outorgação',
            'data_outorga': 'Data de outorgação',
            'termo_outorga': 'Termo de outorga'
        }


class BolsaForm(BolsaAdminForm):
    situacao = forms.ChoiceField(
        label='Situação',
        choices=BolsaAdminForm.SITUACAO_BOLSISTA,
        widget=forms.Select(attrs={ 'class': 'form-select' })
    )
    edital = forms.ModelChoiceField(
        queryset=Edital.objects.all(),
        widget=forms.Select(attrs={ 'class': 'form-select' })
    )

    class Meta(BolsaAdminForm.Meta):
        widgets = {
            'modalidade': forms.TextInput(attrs={ 'class': 'form-control' }),
            'funcao': forms.TextInput(attrs={ 'class': 'form-control' }),
            'carga_horaria': forms.TextInput(attrs={ 'class': 'form-control' }),
            'valor': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'dt_desligamento': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }),
            'vigencia_outorga': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }),
            'data_outorga': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }),
            'termo_outorga': forms.FileInput(attrs={'class': 'form-control'})
        }
