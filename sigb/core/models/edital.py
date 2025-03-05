from django.db import models

from .bolsista import Bolsista


__all__ = [
    'Edital',
]


class Edital(models.Model):
    projeto = models.CharField(max_length=255)
    numero = models.IntegerField()
    nucleo_responsavel = models.CharField(max_length=255)
    vigencia = models.DateField()
    bolsistas = models.ManyToManyField(Bolsista)

    class Meta:
        ordering = ['projeto', 'numero']

    def __str__(self):
        return self.projeto
