
# Detalii despre carte

Aici puteti consulta detaliile cartii **{{ book.code  }}**.

* ... de adus coloanele din tavelul BCAT +
* ... alte info gen:
* numar pagini
* locatia de stocare relativ la /docs (web root)
* ...etc...

SI PUI SI BUTOANE CU ALTE OPERATII din cele posibile din BCAT



<<!-- Petre@250917:
comented to keep good parts &update it


## Lista cartilor

[Creare carte](/booklab/api/newb/)

{% include './local-page.css' %}

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
                <a href="/booklab/api/bstatus/?code={{ book.code }}">* Starea cartii</a><br>
                <a href="/booklab/api/edtb/?code={{ book.code }}">* Editare materiale</a><br>
                <a href="/booklab/api/orgm/?code={{ book.code }}">* Sectiuni carte</a><br>
                <a href="/booklab/api/prvb/?code={{ book.code }}">* Vizualizare carte</a><br>
                <a href="/booklab/api/dplb/?code={{ book.code }}">* Asamblare carte</a>
            </td>
        </tr>
        {% endfor %}
        {% endraw %}


___END OF PETRE COMMENT -->

## [Help](../help/880.30-BSTATUS_usage.md)





