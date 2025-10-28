
# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.

## Lista cartilor

[Creare carte noua](/booklab/api/newb/)

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Cod</th>
            <th>Titlu scurt</th>
            <th>Titlu lung</th>
            <th>Copyright</th>
            <th>Autorul cartii</th>
            <th>Note</th>
            <th>creata de</th>
            <th>data creare</th>
        </tr>
    </thead>
    <tbody>
        {% raw %}
        {% for book in bcat_data %}
        <tr>
            <td>{{ book.id }}</td>
            <td>
                <a href="/booklab/api/bstatus/?code={{ book.code }}">{{ book.code }}</a>
            </td>
            <td>{{ book.short_desc }}</td>
            <td>{{ book.description }}</td>
            <td>{{ book.copyright }}</td>
            <td>{{ book.site_author }}</td>
            <td>{{ book.notes }}</td>
            <td>{{ book.created_by }}</td>
            <td>{{ book.created_date }}</td>
        </tr>
        {% endfor %}
        {% endraw %}
    </tbody>
</table>


## [Help](../help/880.30-BCAT_usage.md)


## Catalogul in format JSON

Mai jos este prezentat catalogul cartilor in forma sa "bruta" de fisier-date JSON:

```json
{% include '../developer/books_catalog.json' %}
```

