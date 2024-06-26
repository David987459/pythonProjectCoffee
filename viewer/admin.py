from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Uzivatel, KategorieProduktu, Produkt, Hodnoceni, Kos, KosItem, Objednavka, UzivatelOblibene

admin.site.register(Uzivatel)
admin.site.register(KategorieProduktu)
admin.site.register(Produkt)
admin.site.register(Hodnoceni)
admin.site.register(Kos)
admin.site.register(KosItem)
admin.site.register(Objednavka)
admin.site.register(UzivatelOblibene)



