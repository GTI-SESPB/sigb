from django.urls import path

from ..views.edital import *


urlpatterns = [
    path('list', EditalList.as_view(), name='edital_list'),
    path('create', EditalCreate.as_view(), name='edital_create'),
    path('update/<pk>', EditalUpdate.as_view(), name='edital_update'),
    path('vincular_bolsista/<bolsista_id>', EditalVincularBolsistaView.as_view(), name='edital_vincular_bolsista'),
]
