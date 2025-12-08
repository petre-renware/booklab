# BookLab (p/n: 0000-0163)

Booklab este o aplicatie destinata creari de manuale / documentatii in format electronic de tip "_site static_".

* p/n: `000-0163`
* start date: 2023-Aug-29

## Site-uri web dedicate:
- [Demo site, ultima versiune stabila](http://booklab.renware.eu)
- [Demo site, ultima versiune in development](http://dev.renware.eu/booklab/)
- [GitHub in development](https://github.com/petre-renware/booklab/)
- [GitHub versiune stabila](https://github.com/petre-renware/booklab/tree/master)


## Installation

**IMPORTANT:** Creati un director distinct unde veti instala sistemul Booklab.

Trebuie sa va asigurati inainte de instalare ca aveti instalat `python3` si `pip` si acestea pot fi rulate.
Nu va faceti griji privind versiunea de Python ci doar sa fie *Python 3*.

In pasul urmator trebuie sa finalizati instalarea prin configurarea versiunilor corecte si crearea unui mediu virtual.
Pentru a face acest lucru cit mai automat si cu minim de efort va recomandan sa instalati manageeul de aplicatii *PDN* astfel:
```shell
pip install pdm
```

Primul pas este instalarea Booklab care se face din siteul oficial Python pentru biblioteci (PyPi):
```shell
pdm add booklab
````

_**NOTA:**_ Daca nu doriti instalarea componentei de management PDM atunci puteti face
instalarea in mod "clasic" utilizind `pip inztall booklab` dar cade in sarcina
dvs de a crea mediu de izolare (python environment si sa asigurati activarea acestuia.


Descarcati fisierul de definire a proiectului `pypriject.toml` astfel:
```shell
booklab setup --get-project-definition
```
comanda care va aduce in directorul creat de dvs fisierul `pyproject.toml` care va fi utilizat de PDM pentru a continua instalarea. Apoi rulati:
```shell
pdm install
```

comanda care va crea un mediu virtual (python virtual environnent) cu toate dependentele necesare si cu versiunea de Python care permite rularea corecta a aplicatiei.


## Pornirea si oprirea serverului Booklab

Pentru a avea acces dun interfata UI (browser) trebuie pornit serverul de aplicatie astefe:
```shell
booklab server run
```

Pentru oprirea sau repornirea serverului se va folosi una din comenzile urmatoare:
```shell
booklab server stop
booklab server restart
```

**NOTE:**

* Serverul odata pornit va rula pina la oprirea explicita sau repornirea masinii hardware
* Pentru pornirea automata (la restart masina hardware) se poate folosi orice metoda standard Linux disponibila pe versiunea folosita de dvs.
  De exemplu prin internediul `cron` sau `systemd`sau chiar folosind alte instrumente dedicate cum ar fi `supervisor`. 


## Log modificari


* [CHANGELOG - last stable version](http://github.com/petre-renware/booklab/blob/master/CHANGELOG.md)
* [CHANGELOG - development version](http://github.com/petre-renware/booklab/blob/development/CHANGELOG.md)





