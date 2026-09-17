from django.urls import path
from . import views

app_name = 'juegos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('juego/<int:id>/', views.detalle, name='detalle'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juegos.urls')),
]