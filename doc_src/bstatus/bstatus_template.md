
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

* Ultima actualizare: {{ book_data.status.last_update_date  }}
* Ultima generare carte: {{ book_data.status.last_build_date }}

* ... locatia relativ la /docs (si / my_books ?)
* ... alte info gen:
* ... numar pagini
* ...etc...




## Optiuni suplimentare

<!-- {% include './local-page.css' %} -->

<a href="/booklab/api/newb/"><button>Creare carte</button></a>

<a href="/booklab/api/edtb/?code={{ book_data.code }}"><button>Editare materiale</button></a>

<a href="/booklab/api/orgm/?code={{ book_data.code }}"><button>Sectiuni carte</button></a>

<a href="/booklab/api/prvb/?code={{ book_data.code }}"><button>Vizualizare carte</button></a>

<a href="/booklab/api/dplb/?code={{ book_data.code }}"><button>Asamblare carte</button></a>


## [Help](../help/880.30-BSTATUS_usage.md)



{% endraw %}


