<!-- #NOTE

    * page dedicated for books catalog

    * for Jinja fields processable @ server-side use `{% raw %} ... {% endraw %}` construction to remain in resulted HTML afer 1st compilation with mkdocs

 -->


# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.




## Lista cartilor

![wip page](../pictures/under_maintenance.png) <!--#FIXME drop me when finish -->


<!-- -#TODO plan for this page

---(page plan) -->





[Creare carte](newb/) <!-- #FIXME_DROP_ME buton ce trebuie sa fie inainte de tabel cu lista carti -->

### Varianta citita static, la compilare din books_catalog. json**

{{ read_json('../data/books_catalog.json', orient='records') }} <!--#NOTE current dire tory is bcat/ here so need go up 1 level to access data/ -->




### Varianta ce va fi citita dinamic la run time si doar variabile Jinja

{% raw %}

| Id carte | Cod carte | Denumire carte | Note       | Operatii |
| -------- | --------- | -------------- | ---------- | ------- |

<!--#TODO

- Jinja for loop to display all sent rows

- in first version ignore buttons which need to be links to an api routes with book id from st column

------ end of #TODO plan-->


{% for line_data in bcat_data %}

| hidde me | {{ line_data["xxx"] }} | {{ line_data["xxx"] }}      | {{ line_data["xxx"] }}  | [edit](edtb/) - [organizare](orgm/) - [view bk](prvb/) - [asamblare](dplb/) ... |

{% endfor %}



{% endraw %}


