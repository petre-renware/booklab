[TOC]

# Detalii despre carte

{% raw %}

Aici puteti consulta detaliile cartii **{{ book_data.short_desc }}** (cod `{{ book_data.code }}`).


## Date generale

* Cod: **`{{ book_data.code }}`**
* Titlu: `{{ book_data.short_desc }}`
* Descriere: `{{ book_data.description }}`
* Note: `{{ book_data.notes }}`
* Copyright: `{{ book_data.copyright }}`
* Autor: `{{ book_data.site_author }}`


## Date de stare

* **Carte inchisa editarii: `{{book_data.closed}}`**
* Creata de: `{{ book_data.created_by }}`
* Creata la data: `{{ book_data.created_date }}`
* Ultima actualizare: `{{book_data.last_update_date}}`
* Ultima generare carte: `{{book_data.last_build_date}}`

## Date locatii

* **Locatia stocare: `{{book_data.store_location}}`**
* Locatia previzualizare: `{{book_data.preview_url}}`
  [(_Previzualizare_)](/booklab/api/prvb/?code={{ book_data.code }})
* Locatia publicare: `{{book_data.published_location}}`
* Sectiunea de navigare in carte: `{{book_data.nav_file_location}}`

## Date volumetrice

* Numar pagini fizice (fisiere): ...urmeaza... 
* Numar pagini logice (intrari in meniu): ...urmeaza...
* Numar fisiere poze: ...urmeaza...


## Actiuni

[Creare carte noua](/booklab/api/newb/){ .md-button .md-button--primary }
[Previzualizare](/booklab/api/prvb/?code={{ book_data.code }}){ .md-button .md-button--primary }

[Editare materiale](/booklab/api/edtb/?code={{ book_data.code }}){ .md-button .md-button--primary }
[Sectiuni carte](/booklab/api/orgm/?code={{ book_data.code }}){ .md-button .md-button--primary }

[Generare carte](/booklab/api/bbld/?code={{ book_data.code }}){ .md-button .md-button--primary }
[Livrare carte](/booklab/api/dplb/?code={{ book_data.code }}){ .md-button .md-button--primary }


## [Help](../help/880.30-BSTATUS_usage.md)


## Vedere avansata sectiunea nevigare

### Format JSON


```
{{ nav.fjson }}

```

### Format YAML

***NOTA:*** Acest fisier este generat automat in timpul executiei sistemului din 
fisierul JSON (de mai sus) care este considerat "primar / master".

```
{{ nav.fyaml }}
```




{% endraw %}




