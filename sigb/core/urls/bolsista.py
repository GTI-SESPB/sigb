from django.urls import path

from ..views.bolsista import *


urlpatterns = [
    path('list', BolsistaList.as_view(), name='bolsista_list'),
    path('detail/<pk>', BolsistaDetailView.as_view(), name='bolsista_detail'),
    path('update/<pk>', BolsistaUpdate.as_view(), name='bolsista_update'),
    path('create', BolsistaCreate.as_view(), name='bolsista_create'),
    path('download', BolsistaDownload.as_view(), name='bolsista_download'),
]
