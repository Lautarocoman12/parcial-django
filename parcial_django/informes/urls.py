from django.urls import path
from . import views

app_name = 'informes'

urlpatterns = [
    path('pdf/<int:pk>/', views.generar_pdf, name='generar_pdf'),
    path('lista/', views.lista_informes, name='lista'),  # ✅ nueva ruta
]
