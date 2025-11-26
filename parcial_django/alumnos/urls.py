from django.urls import path
from . import views

app_name = 'alumnos'  # ✅ Esta línea registra el namespace

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('crear/', views.crear_alumno, name='crear_alumno'),
    path('<int:pk>/editar/', views.editar_alumno, name='editar_alumno'),
    path('<int:pk>/borrar/', views.borrar_alumno, name='borrar_alumno'),
]
