# Parcial Django — Gestión de Alumnos, PDF y Scraper

Proyecto desarrollado por **Lautaro Colman** como entrega del parcial final de Programación.  
Incluye autenticación, dashboard de alumnos, generación de PDF, scraping educativo y despliegue en Render.

---

## Funcionalidades

- Registro y login con correo de bienvenida
- Dashboard de alumnos (CRUD por usuario autenticado)
- Generación de PDF con datos del alumno y envío por correo
- Scraper educativo con resultados en tabla y envío por email
- Deploy en Render con configuración de producción

---

## Instalación local

```bash
git clone https://github.com/Lautarocoman12/parcial-django.git
cd parcial-django
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt


⚙️ Variables de entorno (.env)
env
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.tu_proveedor.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_correo
EMAIL_HOST_PASSWORD=tu_contraseña
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=tu_correo
🛠️ Comandos útiles
bash
python manage.py migrate
python manage.py runserver
python manage.py collectstatic --noinput
🌐 Deploy en Render
Web: https://parcial-django-52y2.onrender.com

Repo: https://github.com/Lautarocoman12/parcial-django