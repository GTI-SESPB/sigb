from django.shortcuts import redirect

from .bolsista import (
    BolsistaList,
    BolsistaCreate,
    BolsistaUpdate,
    BolsistaDownload,
    AdicionarBolsaBolsista,
)
from .bolsa import (
    BolsaList,
    BolsaCreate,
    BolsaUpdate,
)
from .edital import (
    EditalList,
    EditalCreate,
    EditalUpdate
)

def home(_):
    return redirect('bolsista_list')


__all__ = [
    'BolsistaList',
    'BolsistaCreate',
    'BolsistaUpdate',
    'BolsistaDownload',
    'BolsaList',
    'BolsaCreate',
    'BolsaUpdate',
    'AdicionarBolsaBolsista',
    'EditalList',
    'EditalCreate',
    'EditalUpdate',
    'home',
]
