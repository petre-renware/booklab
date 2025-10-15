
# Detalii despre carte

{% raw %}

Aici puteti consulta detaliile cartii **{{ book_data.short_desc }}** (cod `{{ book_data.code }}`).


## Date generale

* Cod: **`{{ book_data.code }}`**
* Titlu: `{{ book_data.short_desc }}`
* Descriere: `{{ book_data.description }}`
* Copyright: `{{ book_data.copyright }}`
* Autor: `{{ book_data.site_author }}`
* Note: `{{ book_data.notes }}`
* Creata de: `{{ book_data.created_by }}`
* Creata la data: `{{ book_data.created_date }}`

## Date de stare curenta

* Ultima actualizare: `{{book_data.last_update_date}}`
* Ultima generare carte: `{{book_data.last_build_date}}`
* Locatia stocare: `{{book_data.store_location}}`
* Locatia previzualizare: `{{book_data.preview_url}}`
    * [Previzualizare carte](/booklab/api/prvb/?code={{ book_data.code }}){ .md-button .md-button--primary }
* Locatia publicare: `{{book_data.published_location}}`
* Carte inchisa editarii: `{{book_data.closed}}`

## Date volumetrice

* Numar pagini fizice (fisiere): ...urmeaza... 
* Numar pagini logice (intrari in meniu): ...urmeaza...
* Numar fisiere poze: ...urmeaza...


## Actiuni

<!-- include './local-page.css' -->

[Creare carte noua](/booklab/api/newb/){ .md-button .md-button--primary }

[Editare materiale](/booklab/api/edtb/?code={{ book_data.code }}){ .md-button .md-button--primary }
[Sectiuni carte](/booklab/api/orgm/?code={{ book_data.code }}){ .md-button .md-button--primary }

[Generare carte](/booklab/api/bbld/?code={{ book_data.code }}){ .md-button .md-button--primary }
[Livrare carte](/booklab/api/dplb/?code={{ book_data.code }}){ .md-button .md-button--primary }


## [Help](../help/880.30-BSTATUS_usage.md)



{% endraw %}


