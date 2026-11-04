# Generare carte

{% raw %}

Aici puteti gestiona siteul cartii **{{ book_data.short_desc }}** (cod `{{ book_data.code }}`):

- sa generati acest site (cartea in format electronic internet)
- sa vedeti rezultatule ultimei generari de carte facuta

[Generare carte](/booklab/api/bbld/startbld/?code={{ book_data.code }}){ .md-button .md-button--primary }

## Date generale:

- Ultima generare de carte facuta in data: **`{{ book_data.last_build_date }}`**
- Proces terminat cu codul: **{{ book_data.excode }}**
- Arhiva site static cu ultima generare carte: **`{{ book_data.last_build_location }}{{book_data.code}}.site.tar`**

## Consola rezultata in urma executiei:

```
{{ book_data.console_out }}
```



{% endraw %}

