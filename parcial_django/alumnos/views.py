from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Alumno
from .forms import AlumnoForm


@login_required
def dashboard(request):
    alumnos = Alumno.objects.filter(usuario=request.user)
    return render(request, 'alumnos/dashboard.html', {'alumnos': alumnos})


@login_required
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.usuario = request.user
            alumno.save()
            return redirect('alumnos:dashboard')  # ✅ con namespace
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/crear_alumno.html', {'form': form})


@login_required
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumnos:dashboard')  # ✅ corregido con namespace
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/editar_alumno.html', {'form': form})


@login_required
def borrar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumnos:dashboard')  # ✅ corregido con namespace
    return render(request, 'alumnos/borrar_confirm.html', {'alumno': alumno})
