from django.db import models


class Bolsista(models.Model):

    nome = models.CharField(max_length=255)
    dt_nascimento = models.DateField()
    nome_mae = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    pis_pasep = models.CharField()
    dados_bancarios = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} {self.cpf}'


class Edital(models.Model):

    nome = models.CharField(max_length=255)
    identificador = models.CharField(max_length=255)
    dt_assinatura = models.DateField()
    data_final = models.DateField()
    bolsistas = models.ManyToManyField(Bolsista)

    def __str__(self):
        return f'{self.nome} {self.identificador}'
    # nucleo_responsavel


class Bolsa(models.Model):

    nome = models.CharField(max_length=255)
    modalidade = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    valor = models.FloatField()
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE)
