from django.db import models

from .bolsista import Bolsista
from .edital import Edital


__all__ = [
    'Bolsa'
]


class Bolsa(models.Model):
    modalidade = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    valor = models.FloatField()
    situacao = models.CharField(max_length=255)
    dt_desligamento = models.DateField(null=True, blank=True)
    vigencia_outorga = models.DateField()
    data_outorga = models.DateField()
    termo_outorga = models.FileField(null=True, blank=True, upload_to='termo_outorga')
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)

    class Meta:
        ordering = ['situacao']

    def __str__(self):
        return self.modalidade
