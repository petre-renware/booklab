# BookLab (p/n: 0000-0163)

Booklab este o aplicatie destinata creari de manuale / documentatii in format electronic de tip "_site static_".

* p/n: `000-0163`
* start date: 2023-Aug-29

## Site web dedicat:
- [Ultima versiune stabila](http://booklab.renware.eu)
- [Versiune curenta in development](http://dev.renware.eu/booklab/)


## Installation

**IMPORTANT:** Creati un director distinct unde veti instala sistemul Booklab.

Primul pas este instalarea Booklab care se face din siteul oficial Python pentru biblioteci (PyPi):
```shell
pip install booklib
````

Trebuie sa va asigurati inainte de instalare ca aveti instalat `python3` si `pip` si acestea pot fi rulate.
Nu va faceti griji privind versiunea de Python ci doar sa fie *Python 3*.

In pasul urmator trebuie sa finalizati instalarea prin configurarea versiunilor corecte si crearea unui mediu virtual.
Pentru a face acest lucru cit mai automat si cu minim de efort va recomandan sa instalati manageeul de aplicatii *PDN* astfel:
```shell
pip install pdm
```

Descarcati fisierul de definire a proiectului `pypriject.toml` astfel:
```shell
bokklab setup --get-project-definition
```
comanda care va crea in directorul creat fisierul `pypriject.toml` care va fi utilizat de ODM ppentru a continua instalarea.
Apoi rulati
```shell
pdm install
```

comanda care va crea un mediu virtual (python virtual environnent) cu toate dependentele necesare si cu versiunea de CPython care permite rularea corecta a aplicatiei.










## Referinte

Web site versiune stabila: booklab.renware.eu
Web site development: dev.renware.eu/booklab
GitHub: ...tbd...

