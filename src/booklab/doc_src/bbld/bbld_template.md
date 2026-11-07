# Generare carte

{% raw %}

Aici puteti gestiona siteul cartii **{{ book_data.short_desc }}** (cod `{{ book_data.code }}`):

- sa generati acest site (cartea in format electronic internet)
- sa vedeti rezultatule ultimei generari de carte facuta

[Generare carte](/booklab/api/bbld/startbld/?code={{ book_data.code }}){ .md-button .md-button--primary }

## Date generale despre ultima generare:

- Ultima generare de carte facuta in data: **`{{ book_data.last_build_date if book_data.last_build_date is not none else 'Nu exista inca date' }}`**
- Proces terminat cu codul: **`{{ book_data.excode }}`**
- Arhiva site static cu ultima generare carte: **`{{ book_data.site_archive_file if book_data.site_archive_file is not none else 'Nu exista inca date.' }}`**

## Consola rezultata in urma executiei:

```
{{ book_data.console_out }}
```



{% endraw %}

