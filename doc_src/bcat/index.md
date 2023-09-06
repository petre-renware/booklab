<!-- #NOTE

    * page dedicated for books catalog

    * for Jinja fields processable @ server-side use `{% raw %} ... {% endraw %}` construction to remain in resulted HTML afer 1st compilation with mkdocs

 -->


# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.




## Lista cartilor

![wip page](../pictures/under_maintenance.png) <!--#FIXME drop me when finish -->

-#TODO plan for this page

* [ ] @1st compile use `PysonDB` cmd line to cvt `.../books_catalog.json` to `csv` to have an initial dataset
* [ ] JS to request `bcat` data
* [x] table with all books
* [ ] hidden col with book ID
* [ ] opers on each line
* [x] global NEW book button
* [ ] for opers use small icons





[Creare carte](newb/)

<!--                #TODO ---(Pyodide code)---
                        * here code to execute Pyodide code before render table
                        * should books catalog data set in table

```pyodide
import micropip

print("Installing cowsay...")
await micropip.install("cowsay")
print("done!")
```
                     #TODO ---(EOF Pyodide code) -->


{% raw %}

| Id carte | Cod carte | Denumire carte | Note       | Operatii |
| -------- | --------- | -------------- | ---------- | ------- |
| hidde me | {{ xxx }} | (( xxx ))      | {{ xxx }} | [:material-book-edit:](edtb/) - [organizare](orgm/) - [view bk](prvb/) - [asamblare](dplb/) ... |

{% endraw %}



