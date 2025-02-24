from django.urls import path

from .views import home
from .views.bolsista import *
from .views.bolsa import *
from .views.edital import *


urlpatterns = [
    path('', home, name='home'),
    path('bolsista/list', BolsistaList.as_view(), name='bolsista_list'),
    path('bolsista/detail/<pk>', BolsistaDetailView.as_view(), name='bolsista_detail'),
    path('bolsista/update/<pk>', BolsistaUpdate.as_view(), name='bolsista_update'),
    path('bolsista/create', BolsistaCreate.as_view(), name='bolsista_create'),
    path('bolsista/download', BolsistaDownload.as_view(), name='bolsista_download'),
    path('bolsista/<bolsista_id>/adicionar_bolsa', AdicionarBolsaBolsista.as_view(), name='vinculo_bolsista_create'),
    path('bolsista/<bolsista_id>/atualizar_bolsa/<pk>', AtualizarBolsaBolsista.as_view(), name='vinculo_bolsista_update'),

    path('bolsa/list', BolsaList.as_view(), name='bolsa_list'),
    path('bolsa/create', BolsaCreate.as_view(), name='bolsa_create'),
    path('bolsa/update/<pk>', BolsaUpdate.as_view(), name='bolsa_update'),

    path('edital/list', EditalList.as_view(), name='edital_list'),
    path('edital/create', EditalCreate.as_view(), name='edital_create'),
    path('edital/update/<pk>', EditalUpdate.as_view(), name='edital_update'),
]
