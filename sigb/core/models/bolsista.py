from django.db import models


__all__ = [
    'Bolsista',
]


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
    documentacao = models.FileField(null=True, blank=True, upload_to='bolsista_documentacao')

    class Meta:
        ordering = ['nome', 'cpf']

    def __str__(self):
        return self.cpf
