from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('alumnos.urls')),          # raíz apunta al dashboard
    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),  # ✅ esto ya incluye /cuentas/perfil/
    path('informes/', include('informes.urls')),
    path('scraper/', include('scraper.urls')),
]

# Solo en desarrollo (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
