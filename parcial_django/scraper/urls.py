from django.urls import path
from . import views

app_name = 'scraper'  # ✅ Esto registra el namespace

urlpatterns = [
    path('', views.buscar, name='buscar'),
]
