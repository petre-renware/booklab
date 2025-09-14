<!-- #NOTE
    * page dedicated for books catalog
    * for Jinja fields processable @ server-side use `{% raw %} ... {% endraw %}` construction to remain in resulted HTML afer 1st compilation with mkdocs
 -->

# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.

## Lista cartilor

[Creare carte](http://localhost:8000/api/newb/) <!--#NOTE action for new book -->


{% include './local-page.css' %} <!--#NOTE contains dropdown commands button CSS -->

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
                <a href="http://localhost:8000/bstatus/?code={{ book.code }}">Starea cartii</a><br/>
                <a href="http://localhost:8000/api/edtb/?code={{ book.code }}">Editare materiale</a><br/>
                <a href="http://localhost:8000/api/orgm/?code={{ book.code }}">Sectiuni carte</a><br/>
                <a href="http://localhost:8000/api/prvb/?code={{ book.code }}">Pre-Vizualizare carte</a><br/>
                <a href="http://localhost:8000/api/dplb/?code={{ book.code }}">Asamblare carte</a>
            </td>
        </tr>
        {% endfor %}
        {% endraw %}
    </tbody>
</table>


## [Help](../help/880.30-BCAT_usage.md)





