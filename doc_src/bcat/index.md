<!-- #NOTE

    * page dedicated for books catalog

    * for Jinja fields processable @ server-side use `{% raw %} ... {% endraw %}` construction to remain in resulted HTML afer 1st compilation with mkdocs

 -->


# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.




## Lista cartilor

![wip page](../pictures/under_maintenance.png) <!--#FIXME drop me when finish -->


<!-- -#TODO plan for this page

* [ ] @1st compile use `PysonDB` cmd line to cvt `.../books_catalog.json` to `csv` to have an initial dataset
* [ ] JS to request `bcat` data
* [x] table with all books
* [ ] hidden col with book ID
* [ ] opers on each line
* [x] global NEW book button
* [ ] for opers use small icons

---(page plan) -->





[Creare carte](newb/) <!--  buton ce trebyyie sa fie inainte de tabel cu lista carti -->




<!--#TODO --- Pyodide code ---
    * should display books catalog data set in table
    * #NOTE attn the JSON with data is at server and should be get with a request to server `bcat`, ie something like `http://localhost:7111/bcat/get_books_catalog`
---(Pyodide code) --

```pyodide
import micropip

print("Installing cowsay...")
await micropip.install("cowsay")

print("done!") # this print will appear in D9M sequence in page, so right here ==> print HTML and draw table here

```


<!-- #NOTE does not help too much - is static execuyed only at mkdocs build compilation...
```python exec="on"
print("***Hello Python - See a random number here***")
import random
num = random.random()
print(num)
```
-->


### Varianta citita static, la compilare din books_catalog. json**

{{ read_json('../data/books_catalog.json', orient='records') }} <!--#NOTE current dire tory is bcat/ here so need go up 1 level to access data/ -->




### Varianta ce va fi citita dinamic la run time si doar variabile Jinja

{% raw %}

| Id carte | Cod carte | Denumire carte | Note       | Operatii |
| -------- | --------- | -------------- | ---------- | ------- |
| hidde me | {{ xxx }} | {{ xxx }}      | {{ xxx }}  | [edit](edtb/) - [organizare](orgm/) - [view bk](prvb/) - [asamblare](dplb/) ... |

{% endraw %}


