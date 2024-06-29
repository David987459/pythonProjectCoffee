### pythonProjectCoffee - Django
Django -> instalace pomocí příkazu (verze 4.1.1):
`python -m pip install django==4.1.1`

Důležité -> Všichni v týmu musí mít stejnou verzi.
### Vytvoření nového projektu

Vytvořen nový projekt pomocí příkazu:
`django-admin startproject ProjectCoffee .`

V `.\ProjectCoffee\setting.py` máme nastavení našeho projektu. Vložit unikátní kód -> v kolonce : SECRET_KEY

V `.\ProjectCoffee\path.py` máme nastavené cesty.

### Seznam nainstalovaných balíčků
`pip freeze > requirements.txt`

### GitHub
Následně zveřejnit projekt na GitHub -> pozvat ostatní členy týmu jako spolupracovníky.

### Seznam nainstalovaných balíčků
pip freeze > requirements.txt

### Spuštění
`python manage.py runserver`
-- spustí standardně na adrese http://127.0.0.1:8000/

Pokud potřebujeme spustit více serverů najednou, tak můžeme změnit port: `python manage.py runserver` 8001 -- server poběží na portu 8001, tedy na adrese http://127.0.0.1:8001/

### Vytvoření aplikace

Pomocí příkazu : `python manage.py startapp viewer`


`
migrations -- složka, která obsahuje migrace
admin.py -- administrační část
apps.py -- nastavení aplikace (necháme beze změn)
models.py -- zde jsou definované modely (tabulky databáze)
tests.py -- zde řešíme testování
views.py -- zde bude logika (propojení databáze a template)
`

### Registrace aplikace
Aplikaci můžume zaregistrovat v souboru .\ProjectCoffee\settings.py:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # our applications
    'viewer',
]
```

### Template pre base.html a templates s home.html
- pridala som zložku templates s base.html, nav.html a footer.html,
- podom som pridala do viewer zložku templates pre domovú stránku s názvom home.html,
- do views som vložila funkciu pre home stránku, 
- do urls.py som pridala path pre funkciu,
- a v settings.py časť TEMPLATES r. 60 som nadstavila 'DIRS' na [BASE_DIR / 'templates'],.

Pri otvorení stránky zobrazí: Welcome to CoffeShop!

### Create admin 
Pomocí příkazu `admin manage.py createsuperuser` vytvoříme admin panel s přihlašováním.


### Vytvoření aplikace `orders`
Ve složce `ProjectCoffee/settings/installed apps napojena cesta 'orders',` .
```INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # our applications
    'viewer',
    'orders',
]
```
Ve složce `orders/admin` zaregistrovány modely.
`admin.site.register(Product)`
`admin.site.register(OrderItem)`





### Create admin 
Pomocí příkazu `admin manage.py createsuperuser` vytvoříme admin panel s přihlašováním.


### Vytvoření aplikace `orders`
Ve složce `ProjectCoffee/settings/installed apps napojena cesta 'orders',` .
```INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # our applications
    'viewer',
    'orders',
]
```
Ve složce `orders/admin` zaregistrovány modely.
`admin.site.register(Product)`
`admin.site.register(OrderItem)`

### VYTVOŘENÍ - 

