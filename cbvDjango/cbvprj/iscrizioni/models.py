from django.db import models


class Studente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)

    def __str__(self):
        return "ID: " + str(self.pk) + ": " + str(self.nome) + " " + str(self.cognome)

    class Meta:
        verbose_name_plural = "Studenti"


class Insegnamento(models.Model):
    titolo = models.CharField(max_length=100)
    studenti = models.ManyToManyField(Studente, default=None)

    def __str__(self):
        return "ID: " + str(self.pk) + ": " + str(self.titolo)

    class Meta:
        verbose_name_plural = "Insegnamenti"
