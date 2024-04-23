from threading import Timer

from django.utils import timezone
from datetime import datetime, timedelta
from gestione.models import Libro, Copia


def erase_db():
    print('Erasing DB')
    Libro.objects.all().delete()
    return


def init_db():
    print('Initializing DB')
    if len(Libro.objects.all()) != 0:
        return

    def timing(off_year=None, off_month=None, off_day=None):
        tz = timezone.now()
        out = datetime(tz.year - off_year, tz.month - off_month, tz.day - off_day, tz.hour, tz.minute, tz.second)
        return out

    libri = {"autori" : ["Alessandro Manzoni", "George Orwell", "Omero", "George Orwell", "Omero"],
             "titoli" : ["I Promessi Sposi", "1984", "Odissea", "La Fattoria Degli Animali", "Iliade"],
             "pagine" : [832, 328, 414, 141, 263]}
    date = [timing(y, m, d) for (y, m, d) in range(2, 2, 2)]

    for i in range(5):
        l = Libro()
        for k in libri:
            if k == "autori":
                l.autore = libri[k][i]
            if k == "titoli":
                l.titolo = libri[k][i]
            if k == "pagine":
                l.pagine = libri[k][i]
            l.save()
        for d in date:
            c = Copia()
            c.scaduto = False
            c.libro = l
            c.data_prestito = d
            c.save()

    print(Libro.objects.all())


def controllo_scadenza():
    MAX_PRESTITO_GIORNI = 15

    print("Controllo copie scadute...")
    for l in Libro.objects.all():
        s0 = l.copie.filter(scaduto=False).exclude(data_prestito=None)
        for c in s0:
            dt = datetime(timezone.now().year, timezone.now().month, timezone.now().day).date()
            if (dt - c.data_prestito) > timedelta(days=MAX_PRESTITO_GIORNI):
                c.scaduto = True
                c.save()
                print(c)


def start_controllo_scadenza(check_time_in_seconds):
    Timer(check_time_in_seconds, controllo_scadenza).start()