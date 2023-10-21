<!-- #NOTE

    * page dedicated for books catalog

    * for Jinja fields processable @ server-side use `{% raw %} ... {% endraw %}` construction to remain in resulted HTML afer 1st compilation with mkdocs

 -->

# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua.

## Lista cartilor

[Creare carte](newb/) `<!-- #NOTE action for new book -->`

{% raw %}

<table markdown="1">
<thead markdown="1">
<tr markdown="1">
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
<tbody markdown="1">
{% for book in bcat_data %}
<tr markdown="1">
<td markdown="1">{{ book.id }}</td>
<td markdown="1">{{ book.code }}</td>
<td markdown="1">{{ book.short_desc }}</td>
<td markdown="1">{{ book.description }}</td>
<td markdown="1">{{ book.copyright }}</td>
<td markdown="1">{{ book.site_author }}</td>
<td markdown="1">{{ book.notes }}</td>
<td markdown="1">{{ book.created_by }}</td>
<td markdown="1">{{ book.created_date }}</td>
<td markdown="1"> <!-- #NOTE actions for edit, organize, assembly book -->
    [editare](edtm/) - [organizare](orgm/) - [vizualizare](prvb/) - [asamblare](dplb/)
</td>
</tr>
{% endfor %}
</tbody>
</table>

{% endraw %}

## [Help](../help/880.30-BCAT_usage.md)
