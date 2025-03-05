from django import forms

from ..models.edital import Edital


__all__ = [
    'EditalAdminForm',
    'EditalForm',
    'EditalVincularBolsistaForm'
]


class EditalAdminForm(forms.ModelForm):
    class Meta:
        model = Edital
        exclude = [ 'bolsistas', ]

        labels = {
            'projeto': 'Projeto',
            'numero': 'Número',
            'nucleo_responsavel': 'Núcleo Responsável',
            'vigencia': 'Vigência',
        }


class EditalForm(EditalAdminForm):
    class Meta(EditalAdminForm.Meta):
        widgets = {
            'projeto': forms.TextInput(attrs={ 'class': 'form-control' }),
            'numero': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'nucleo_responsavel': forms.TextInput(attrs={ 'class': 'form-control' }),
            'vigencia': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }),
        }


class EditalVincularBolsistaForm(forms.Form):
    edital = forms.ModelChoiceField(
        queryset=Edital.objects.all(),
        widget=forms.Select(attrs={ 'class': 'form-select' })
    )
