from django.db import models

from .utils import TimestampMixin


__all__ = [
    'Bolsista',
    'AnexoBolsista'
]


class Bolsista(TimestampMixin):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    dt_nascimento = models.DateField()
    nome_mae = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    pis_pasep = models.CharField()
    conta_bancaria = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    municipio = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    documentacao = models.FileField(upload_to='bolsista_documentacao')

    class Meta:
        ordering = ['nome', 'cpf']

    def __str__(self):
        return self.cpf


class AnexoBolsista(models.Model):
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='bolsista_documentos')
    anexo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
