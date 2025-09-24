
# Detalii despre carte

{% raw %}

Aici puteti consulta detaliile cartii **{{ book_data.short_desc }}** (cod *{{ book_data.code }}*).


## Date generale

* Titlu: {{ book_data.short_desc }}
* Descriere: {{ book_data.description }}
* Copyright: {{ book_data.copyright }}
* Autor: {{ book_data.site_author }}
* Note: {{ book_data.notes }}
* Creata de: {{ book_data.created_by }}
* Creata la data: {{ book_data.created_date }}

## Date de stare curenta

* Ultima actualizare: {{book_data.status.last_update_date}}
* Ultima generare carte: {{book_data.status.last_build_date}}
* Locatia stocare: {{book_data.status.location_dir}}
* Locatia publicare: {{book_data.status.published_location}}
* Carte inchisa editarii: {{book_data.status.closed}}

## Date volumetrice

* Numar pagini fizice (fisiere): ...urmeaza... 
* Numar pagini logice (intrari in meniu): ...urmeaza...
* Numar fisiere poze: ...urmeaza...


## Optiuni suplimentare

<!-- {% include './local-page.css' %} -->

* <a href="/booklab/api/newb/">Creare carte</a>
* <a href="/booklab/api/edtb/?code={{ book_data.code }}">Editare materiale</a>
* <a href="/booklab/api/orgm/?code={{ book_data.code }}">Sectiuni carte</a>
* <a href="/booklab/api/prvb/?code={{ book_data.code }}">Vizualizare carte</a>
* <a href="/booklab/api/dplb/?code={{ book_data.code }}">Asamblare carte</a>


## [Help](../help/880.30-BSTATUS_usage.md)



{% endraw %}


