![booklab_logo](pictures/booklab_logo.png){ width="300" }


<!-- #NOTE -- TEST HTML FORM ------------------------------------------------
---pui un div cu markdown ? Better...
<form action="XXX_TEST_ROUTE/xxxfile">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname" value="John"><br>

  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>

# Note si explicatii rezultat:

    - caz 0: util acces **`booklab_app`**: `<form method="POST" action="http://localhost:8000">` unde 8000 este portul ales
    - caz 1: cu `action="/XXX_TEST_ROUTE"` ==> raspunsul a fost request catre `/XXX_TEST_ROUTE?fname=John&lname=Doe` url ABSOLUT
    - caz 2: cu `action="XXX_TEST_ROUTE"` ==> raspunsul a fost request catre `http://server_name.../XXX_TEST_ROUTE?fname=John&lname=Doe` url RELATIV la servername
    - caz 3: cu `action="XXX_TEST_ROUTE/xxxfile"` ==> raspunsul a fost request catre `http://server_name.../XXX_TEST_ROUTE/xxxfile?fname=John&lname=Doe` url RELATIV la servername

------------------------------------------------------------------------->




# BookLab

<small markdown>by RENware Software Systems</small>

Welcome to **BookLab** world, your personal assistant in putting your ideas in practice and making your books as you dreamed them.

Bine ai venit in lunea **BookLab**, asistentul tau personal in punerea ideilor tale in practica si realizarea cartlior si materialelor tale asa cum le-ai visat.

Ce poti face mai departe:

* **[sa vezi catalogul cartilor tale](bcat/)**
* **[sa incepi o noua carte](newb/)**

Daca inca nu esti sigur sau hotarit, poti sa revezi doumentatia sistemului:

* **[sa citesti "Vederea de ansamblu" a BookLab](help/130.02-Overview.md){ target="_blank" }**
* **[sa revezi manualele de utilizare](help/880.30-EUMA_catalog.md){ target="_blank" }**
* **[sa revezi manualele de configurare](help/880.30-ADMA_catalog.md){ target="_blank" }**


!!! warning "Versiunea publica demo"
    Versiunea _publica_ (demonstrativa) a aplicatiei Booklab (accesibila la adresa `booklab.renware.eu`) are scop _pur demonstrativ_.
    In aceaata aplicatie se pot face teste in mod public si neidentificat (anonim) drept pentru care puteti gasi diverse date / carti create de catre alte persoane decit dumneavoastra.
    De aceea va rugam sa nu alterati carti sau date care nu stiti ca le-ati creat dumneavostra.
    Creati-va propriile carti asupra carora sa faceti orice teste dorite.





