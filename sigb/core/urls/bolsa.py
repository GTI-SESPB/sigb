from django.urls import path

from ..views.bolsa import *


urlpatterns = [
    path('create/<bolsista_id>', BolsaCreate.as_view(), name='bolsa_create'),
    path('update/<pk>', BolsaUpdate.as_view(), name='bolsa_update')
]
