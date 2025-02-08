from django.urls import path

from .views import (
    home,
    BolsistaCreate,
    BolsistaList,
    BolsistaUpdate,
)


urlpatterns = [
    path('', home, name='home'),
    path('bolsista/list', BolsistaList.as_view(), name='bolsista_list'),
    path('bolsista/update/<pk>', BolsistaUpdate.as_view(), name='bolsista_update'),
    path('bolsista/create', BolsistaCreate.as_view(), name='bolsista_create'),
]
