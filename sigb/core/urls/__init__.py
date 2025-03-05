from django.urls import include, path

from ..views import home



urlpatterns = [
    path('', home, name='home'),
    path('bolsa/', include('core.urls.bolsa')),
    path('bolsista/', include('core.urls.bolsista')),
    path('edital/', include('core.urls.edital')),
]
