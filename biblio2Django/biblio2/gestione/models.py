from django.db import models


class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.CharField(max_length=50)
    pagine = models.IntegerField(default=100)

    def __str__(self):
        out = str(self.titolo) + " di " + str(self.autore) + " ha " + str(self.copie.all().count()) + " copie"
        return out

    class Meta:
        verbose_name_plural = "Libri"


class Copia(models.Model):
    data_prestito = models.DateField(default=None, null=True)
    scaduto = models.BooleanField(default=False)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="copie")

    def __str__(self):
        out = "copia di " + str(self.libro.titolo) + " di " + str(self.libro.autore) + ": "
        if self.scaduto:
            out += "copia scaduta"
        else:
            out += "copia valida"

        return out

    class Meta:
        verbose_name_plural = "Copie"

