from django.db import models

from .bolsista import Bolsista
from .edital import Edital


__all__ = [
    'Bolsa'
]


class Bolsa(models.Model):
    projeto = models.CharField(max_length=255)
    numero_edital = models.IntegerField()
    vigencia_edital = models.DateField()
    nucleo_responsavel = models.CharField(max_length=255)
    modalidade = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    valor = models.FloatField()
    situacao = models.CharField(max_length=255)
    dt_desligamento = models.DateField(null=True, blank=True)
    vigencia_outorga = models.DateField(null=True, blank=True)
    data_outorga = models.DateField(null=True, blank=True)
    termo_outorga = models.FileField(null=True, blank=True, upload_to='termo_outorga')
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE)

    class Meta:
        ordering = ['projeto', 'numero_edital']

    def __str__(self):
        return self.projeto
