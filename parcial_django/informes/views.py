from django.shortcuts import render

# Create your views here.

import io
from reportlab.pdfgen import canvas
from django.http import FileResponse
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect
from alumnos.models import Alumno
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def generar_pdf(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica", 14)
    p.drawString(100, 800, f"Ficha del alumno: {alumno.nombre}")
    p.setFont("Helvetica", 12)
    p.drawString(100, 770, f"Email: {alumno.email}")
    p.drawString(100, 750, f"Curso: {alumno.curso}")
    p.drawString(100, 730, f"Creado: {alumno.fecha_creacion.strftime('%Y-%m-%d %H:%M')}")
    p.showPage()
    p.save()
    buffer.seek(0)

    email_to = request.user.email
    email = EmailMessage(
        subject=f'Ficha de {alumno.nombre}',
        body='Adjunto tienes la ficha en PDF.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email_to],
    )
    email.attach(f'ficha_{alumno.pk}.pdf', buffer.getvalue(), 'application/pdf')
    email.send(fail_silently=False)
    return redirect('dashboard')

@login_required
def lista_informes(request):
    return render(request, 'informes/lista.html')
