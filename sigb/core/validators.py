from django.core.exceptions import ValidationError

from .utils import apenas_digitos


def cpf_validator(cpf):
    cpf = apenas_digitos(cpf)
    for dv in (0, 1):
        soma = 0
        for char, multiplicador in zip(cpf[dv:], range(10, 1, -1)):
            soma += int(char) * multiplicador
        resto = soma % 11
        if len(cpf) < 11 or str(11 - resto if resto > 1 else 0) != cpf[dv+9]:
            raise ValidationError('CPF Inválido')
