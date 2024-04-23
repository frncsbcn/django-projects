from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from gestione.models import Libro
MATTONE_THRESHOLD = 300


def lista(request):
    template = 'gestione/lista.html'
    context = {"title": "Lista dei libri",
               "lista": Libro.objects.all()}
    return render(request, template, context)


def mattoni(request):
    template = 'gestione/lista.html'
    books = Libro.objects.filter(pagine__gte=MATTONE_THRESHOLD)
    context = {"title": "Lista dei mattoni",
               "lista": books}
    return render(request, template, context)


def lista_autore(request):
    try:
        template = 'gestione/lista.html'
        books = Libro.objects.filter(autore__icontains=request.GET["author"])
        context = {"title": "Lista dei libri di " + request.GET["author"],
                   "lista": books}
        return render(request, template, context)
    except:
        return HttpResponse("Scrivi un autore")


def lista_autore_path(request, author):
    template = 'gestione/lista.html'
    books = Libro.objects.filter(autore__icontains=author)
    context = {"title": "Lista dei libri di " + author,
               "lista": books}
    return render(request, template, context)


def crea_libro(request):
    message = ""

    if "autore" in request.GET and "titolo" in request.GET:
        author = request.GET["autore"]
        title = request.GET["titolo"]
        pages = 100
        try:
            pages = int(request.GET["pagine"])
        except:
            message = "Numero di pagine invalido. " + message

        libro = Libro(titolo=title, autore=author, pagine=pages, data_prestito=datetime.now())
        try:
            libro.save()
            message += "Libro aggiunto"
        except Exception as e:
            message = "Errore nella creazione del libro, " + str(e)

    return render(request, template_name="gestione/crealibro.html", context={"title": "crea libro", "message": message})
