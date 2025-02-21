from django.db import models


class Bolsa(models.Model):

    modalidade = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    valor = models.FloatField()

    def __str__(self):
        return str(self.modalidade)
