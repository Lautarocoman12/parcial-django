from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()

            # Enviar correo de bienvenida
            send_mail(
                '¡Bienvenido!',
                f'Hola {usuario.username}, gracias por registrarte.',
                None,  # Usa DEFAULT_FROM_EMAIL
                [usuario.email],
            )

            messages.success(request, 'Usuario creado correctamente. Revisa tu correo.')
            return redirect('login')  # Ajustá según tu URL
    else:
        form = RegistroForm()
    return render(request, 'cuentas/registro.html', {'form': form})

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'cuentas/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required

@login_required
def perfil(request):
    return render(request, 'cuentas/perfil.html')
