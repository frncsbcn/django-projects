from django.utils import timezone
from datetime import datetime
from gestione import Libro


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
             "pagine" : [832, 328, 414, 141, 263],
             "date" : [timing(y, m, d) for y in range(2) for m in range(2) for d in range(2)]}

    for i in range(5):
        l = Libro()
        for k in libri:
            if k == "autori":
                l.autore = libri[k][i]
            if k == "titoli":
                l.titolo = libri[k][i]
            if k == "pagine":
                l.pagine = libri[k][i]
            if k == "date":
                l.data_prestito = libri[k][i]

        l.save()

    print(Libro.objects.all())
