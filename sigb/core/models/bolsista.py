from django.db import models

from .bolsa import Bolsa
from .edital import Edital


class Bolsista(models.Model):

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    dt_nascimento = models.DateField()
    nome_mae = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    pis_pasep = models.CharField()
    conta_bancaria = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    documentacao = models.FileField(upload_to='bolsista_documentacao')

    def __str__(self):
        return f'{self.nome} - {self.cpf}'


class BolsistaBolsa(models.Model):

    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    bolsa = models.ForeignKey(Bolsa, null=True, blank=True, on_delete=models.CASCADE)

    funcao = models.CharField(max_length=255)
    situacao = models.CharField(max_length=255)
    dt_desligamento = models.DateField(blank=True, null=True)

    # Outorga
    vigencia_outorga = models.DateField()
    data_outorga = models.DateField()
    termo_outorga = models.FileField(null=True, blank=True, upload_to='termo_outorga')
