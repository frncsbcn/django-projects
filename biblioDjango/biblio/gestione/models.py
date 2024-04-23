from django.db import models


class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.CharField(max_length=50)
    pagine = models.IntegerField(default=100)
    data_prestito = models.DateField(default=None)

    def __str__(self):
        out = self.titolo + " - " + self.autore
        if self.data_prestito is not None:
            out += " - in prestito dal " + str(self.data_prestito)
        else:
            out += " - attualmente non in prestito"
        return out
