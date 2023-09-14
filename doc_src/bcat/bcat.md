<!-- #NOTE

    * page dedicated for books catalog

    * for Jinja fields processable @ server-side use `{% raw %} ... {% endraw %}` construction to remain in resulted HTML afer 1st compilation with mkdocs

 -->


# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.




## Lista cartilor

![wip page](../pictures/under_maintenance.png) <!--#FIXME drop me when finish -->


[Creare carte](newb/) <!-- #NOTE this button naturally stay here, before books table -->


{% raw %}

| ID  | Cod | Titlu scurt | Titlu lung | Note | creata de | data creare | actiuni |
| --- | --- | ----------- | ---------- | ---- | --------- | ----------- | ------- |



<!--#TODO
- Jinja for loop to display all sent rows
- in first version ignore actions which need to be links to an api routes with book id from st column
------ end of #TODO plan-->


{% for book in bcat_data %}

| {{ book.id }} | {{ book.code }} | {{ book.short_desc }} | {{ book.description }} | {{ book.notes }} | {{ book.created_by }} | {{ book.created_date }} | [edit](edtb/) - [organizare](orgm/) - [vizualizare](prvb/) - [asamblare](dplb/) |

{% endfor %}



{% endraw %}





### Varianta citita static - SECTIUNE CE VA DISPARE DUPA FINALIZARE COD <!--#FIXME this section will de dropped - kept just to compare -->

{{ read_json('../data/books_catalog_pandas_version.json', orient='records') }} <!--#FIXME this section will de dropped - kept just to compare -->
