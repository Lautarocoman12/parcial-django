from django.shortcuts import render, redirect
from .forms import BuscarForm
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
import csv
import io
from django.conf import settings

@login_required
def buscar(request):
    resultados = []
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['q']
            # Forzar resultados de búsqueda en Wikipedia
            url = f'https://es.wikipedia.org/w/index.php?search={q}&ns0=1&fulltext=1'

            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/119.0.0.0 Safari/537.36'
                }
                r = requests.get(url, headers=headers, timeout=10)
                r.raise_for_status()
                soup = BeautifulSoup(r.text, 'html.parser')

                # Buscar resultados
                items = soup.select('ul.mw-search-results li a')[:10]
                if not items:
                    # Si no hay resultados, tomar el título de la página
                    titulo = soup.select_one('#firstHeading')
                    if titulo:
                        resultados.append({
                            'titulo': titulo.get_text(strip=True),
                            'link': url,
                        })

                print(f'Se encontraron {len(resultados) + len(items)} resultados para "{q}"')

                for it in items:
                    resultados.append({
                        'titulo': it.get_text(strip=True),
                        'link': 'https://es.wikipedia.org' + it.get('href'),
                    })

                # generar CSV en memoria y enviar por email
                csv_buffer = io.StringIO()
                writer = csv.writer(csv_buffer)
                writer.writerow(['Titulo', 'Link'])
                for row in resultados:
                    writer.writerow([row['titulo'], row['link']])
                csv_buffer.seek(0)

                email = EmailMessage(
                    subject=f'Resultados de scraping para "{q}"',
                    body='Adjunto CSV con resultados',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[request.user.email],
                )
                email.attach(f'resultados_{q}.csv', csv_buffer.getvalue(), 'text/csv')
                email.send(fail_silently=False)

            except Exception as e:
                print(f'Error al hacer scraping: {e}')
    else:
        form = BuscarForm()
    return render(request, 'scraper/buscar.html', {'form': form, 'resultados': resultados})
