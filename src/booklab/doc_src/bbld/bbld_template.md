# Generare carte

{% raw %}

Aici puteti gestiona siteul cartii **{{ book_data.short_desc }}** (cod `{{ book_data.code }}`):

- sa generati acest site (cartea in format ekectronic internet)
- sa vedeti rezultatule ultimei generari de carte facuta

[Generare carte](/booklab/api/bbld/startbld/?code={{ book_data.code }}){ .md-button .md-button--primary }

## Date generale:

- Ultima generare de carte facuta in data: **`{{ book_data.last_build_date }}`**
- Proces terminat cu codul: **{{ book_data.excode }}**

## Consola rezultata in urma executiei:

```
{{ book_data.console_out }}
```




...#tbd... restul trebuie updated ...






{% endraw %}

