<!-- #NOTE
    * page dedicated for books catalog
    * for Jinja fields processable @ server-side use `{% raw %} ... {% endraw %}` construction to remain in resulted HTML afer 1st compilation with mkdocs
 -->

# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.

## Lista cartilor

[Creare carte](newb/) <!--#NOTE action for new book -->


{% include './bcat.css' %} <!--#NOTE contains dropdown commands button CSS -->

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
            <td> <!-- #NOTE actions for edit, organize, assembly book -->
                <!--<div class="dropdown">
                    <button onclick="activateDropdown()" class="dropbtn">OP &#x2BC6;</button>
                    <div id="IDcmds-{{ book.code }}" class="dropdown-content"> -->
                        <a href="/bstatus?code={{ book.code }}">Starea cartii</a>
                        <a href="/edtb?code={{ book.code }}">Editare materiale</a>
                        <a href="/orgm?code={{ book.code }}">Sectiuni carte</a>
                        <a href="/prvb?code={{ book.code }}">Pre-Vizualizare carte</a>
                        <a href="/dplb?code={{ book.code }}">Asamblare carte</a>
                    <!-- </div>
                </div> -->
            </td>
        </tr>
        {% endfor %}
        {% endraw %}
    </tbody>
</table>


## [Help](../help/880.30-BCAT_usage.md)







{% include './bcat.js' %} <!--#NOTE contains dropdown commands button JS -->


