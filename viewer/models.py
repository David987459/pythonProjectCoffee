from django.db import models

# Create your models here.
from django.db.models import Model

class Uzivatel(Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    registrovan_dne = models.DateTimeField(auto_now_add=True)
    ulice = models.CharField(max_length=255)
    psc = models.CharField(max_length=10)
    mesto = models.CharField(max_length=100)
    oblibene_produkty = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class KategorieProduktu(Model):
    nazev = models.CharField(max_length=50)
    popis = models.TextField()

    def __str__(self):
        return self.nazev

class Produkt(Model):
    nazev_produktu = models.CharField(max_length=255)
    nahled = models.URLField()
    druh_produktu = models.CharField(max_length=255)
    zeme_puvodu = models.CharField(max_length=255)
    kategorie_produktu = models.BooleanField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    popis = models.TextField()
    ks_skladem = models.IntegerField()
    prumer_hodnoceni = models.FloatField(default=0.0)

    def __str__(self):
        return self.nazev_produktu

class Hodnoceni(Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    user = models.ForeignKey(Uzivatel, on_delete=models.CASCADE)
    hodnoceni = models.TextField()
    hvezdy = models.IntegerField()
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Hodnoceni {self.hvezdy} pro {self.produkt.nazev_produktu} user {self.user.jmeno}"

class Kos(Model):
    user = models.ForeignKey(Uzivatel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Kos {self.id} for {self.user.jmeno}"

class KosItem(Model):
    kos = models.ForeignKey(Kos, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cena_celkem = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.produkt.nazev_produktu} in kos {self.kos.id}"

class Objednavka(Model):
    user = models.ForeignKey(Uzivatel, on_delete=models.SET_NULL, null=True, blank=True)
    kos = models.ForeignKey(Kos, on_delete=models.CASCADE)
    datum_objednavky = models.DateTimeField(auto_now_add=True)
    cena_objednavky = models.DecimalField(max_digits=10, decimal_places=2)
    jmeno = models.CharField(max_length=255)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    ulice = models.CharField(max_length=255)
    psc = models.CharField(max_length=10)
    mesto = models.CharField(max_length=100)

    def __str__(self):
        return f"Objednavka {self.id} for {self.jmeno}"

class UzivatelOblibene(Model):
    user = models.ForeignKey(Uzivatel, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)

    def __str__(self):
        return f"Oblibene produkt {self.produkt.nazev_produktu} for user {self.user.jmeno}"
