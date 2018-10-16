from django.db import models
from django.utils import timezone


class Domande(models.Model):
    lingua = models.CharField(max_length=2) #ISO639 standardization, with 2 lowercase letters; list avaible here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    testo_domanda = models.TextField()
    categoria = models.CharField(max_length=30)
    suggerimento = models.TextField(default=None, blank=True, null=True)
    risposta = models.ForeignKey('Risposte', on_delete=models.CASCADE)
    immagine = models.TextField(default=None, blank=True, null=True)
    barra_img = models.TextField(default=None, blank=True, null=True)

    def submit(self):
        self.save()

    def __str__(self):
        return str(self.id)

class Risposte(models.Model):
    lingua = models.CharField(max_length=2) #ISO639 standardization, with 2 lowercase letters; list avaible here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    testo = models.TextField(default=None, blank=True, null=True)
    immagine = models.TextField(default=None, blank=True, null=True)
    booleano = models.BooleanField(default=None, blank=True, null=True)
    barra = models.TextField(default=None, blank=True, null=True)

    def submit(self):
        self.save()

    def __str__(self):
        return str(self.id)
