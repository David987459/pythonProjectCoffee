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
### ORM
Modely vytváříme v souboru `models.py` v dané aplikaci.

DŮLEŽITÉ: Po každé změně v modelech (tj. v souboru `models.py`) musíme migrovat databázi:

vytvoření migračního skriptu: `python manage.py makemigrations`
aplikujeme migraci: `python manage.py migrate`
DŮLEŽITÉ: Migrační skripty vkládáme do repozitáře (git), databázi ne (obsahuje mimo jiné i hesla všech uživatelů)

### shell
Použití pro rychlou práci s databází -> Django shell `python manage.py shell`




