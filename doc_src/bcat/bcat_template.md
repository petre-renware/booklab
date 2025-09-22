
# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.

## Lista cartilor

[Creare carte](/booklab/api/newb/)

{% include './local-page.css' %}

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
            <th>actiuni</th>
        </tr>
    </thead>
    <tbody>
        {% raw %}
        {% for book in bcat_data %}
        <tr>
            <td>{{ book.id }}</td>
            <td>{{ book.code }}</td>
            <td>{{ book.short_desc }}</td>
            <td>{{ book.description }}</td>
            <td>{{ book.copyright }}</td>
            <td>{{ book.site_author }}</td>
            <td>{{ book.notes }}</td>
            <td>{{ book.created_by }}</td>
            <td>{{ book.created_date }}</td>
            <td>
                    <a href="/booklab/api/bstatus/?code={{ book.code }}">* Starea cartii</a>
                <br><a href="/booklab/api/edtb/?code={{ book.code }}">* Editare materiale</a>
                <br><a href="/booklab/api/orgm/?code={{ book.code }}">* Sectiuni carte</a>
                <br><a href="/booklab/api/prvb/?code={{ book.code }}">* Vizualizare carte</a>
                <br><a href="/booklab/api/dplb/?code={{ book.code }}">* Asamblare carte</a>
            </td>
        </tr>
        {% endfor %}
        {% endraw %}
    </tbody>
</table>


## [Help](../help/880.30-BCAT_usage.md)





