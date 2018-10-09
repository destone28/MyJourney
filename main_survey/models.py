from django.db import models
from django.utils import timezone


class Domande(models.Model):
    lingua = models.CharField(max_length=2) #ISO639 standardization, with 2 lowercase letters; list avaible here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    numero = models.PositiveSmallIntegerField()
    testo_domanda = models.TextField()
    categoria = models.CharField(max_length=30)
    suggerimento = models.TextField(default=None, blank=True, null=True)
    risposta = models.ForeignKey('Risposte', on_delete=models.CASCADE)

    def submit(self):
        self.save()

    def __str__(self):
        return str(self.numero)

class Risposte(models.Model):
    lingua = models.CharField(max_length=2) #ISO639 standardization, with 2 lowercase letters; list avaible here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    numero_domanda = models.PositiveSmallIntegerField()
    testo = models.TextField(default=None, blank=True, null=True)
    data = models.DateField(default=None, blank=True, null=True)
    booleano = models.BooleanField(default=None, blank=True, null=True)
    intero = models.PositiveSmallIntegerField(default=None, blank=True, null=True)

    def submit(self):
        self.save()

    def __str__(self):
        return str(self.numero_domanda)

class Logtable(models.Model):
    #id = models.AutoField() automatically created
    quando = models.DateTimeField(default=timezone.now)
    lingua = models.CharField(max_length=2) #ISO639 standardization, with 2 lowercase letters; list avaible here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    uno = models.TextField(default=None, blank=True, null=True)
    due = models.TextField(default=None, blank=True, null=True)
    tre = models.TextField(default=None, blank=True, null=True)
    quattro = models.TextField(default=None, blank=True, null=True)
    cinque = models.TextField(default=None, blank=True, null=True)
    sei = models.DateField(default=None, blank=True, null=True)
    sette = models.DateField(default=None, blank=True, null=True)
    otto = models.BooleanField(default=None, blank=True, null=True)
    nove = models.TextField(default=None, blank=True, null=True)
    dieci = models.BooleanField(default=None, blank=True, null=True)
    undici = models.TextField(default=None, blank=True, null=True)
    dodici = models.BooleanField(default=None, blank=True, null=True)
    tredici = models.BooleanField(default=None, blank=True, null=True)
    quattordici = models.BooleanField(default=None, blank=True, null=True)
    quindici = models.TextField(default=None, blank=True, null=True)
    sedici = models.BooleanField(default=None, blank=True, null=True)
    diciassette = models.TextField(default=None, blank=True, null=True)
    diciotto = models.TextField(default=None, blank=True, null=True)
    diciannove = models.BooleanField(default=None, blank=True, null=True)
    venti = models.BooleanField(default=None, blank=True, null=True)
    ventuno = models.BooleanField(default=None, blank=True, null=True)
    ventidue = models.TextField(default=None, blank=True, null=True)
    ventitre = models.BooleanField(default=None, blank=True, null=True)
    ventiquattro = models.BooleanField(default=None, blank=True, null=True)
    venticinque = models.BooleanField(default=None, blank=True, null=True)
    idoneo = models.BooleanField(default=None, blank=True, null=True)

    def submit(self):
        self.save()

    def __str__(self):
        return self.id #TO-DO CHECK SU QUESTA FUNZIONE
