from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # 👈 LOGIN/LOGOUT

    path('', include('alumnos.urls')),          
    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),
    path('informes/', include('informes.urls')),
    path('scraper/', include('scraper.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
