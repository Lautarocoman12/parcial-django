def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()

            # 🔴 DESACTIVAR ESTO PORQUE GENERA ERROR EN RENDER
            # send_mail(
            #     '¡Bienvenido!',
            #     f'Hola {usuario.username}, gracias por registrarte.',
            #     None,
            #     [usuario.email],
            # )

            messages.success(request, 'Usuario creado correctamente.')
            return redirect('cuentas:login')

    else:
        form = RegistroForm()
    return render(request, 'cuentas/registro.html', {'form': form})
