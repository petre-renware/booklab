<!-- #NOTE

    * page dedicated for books catalog

    * for Jinja fields processable @ server-side use `{% raw %} ... {% endraw %}` construction to remain in resulted HTML afer 1st compilation with mkdocs

 -->


# Catalogul cartilor

Bine ati venit la *Catalogul cartilor dumneavoastra*. Aici puteti vizualiza cartile create de dumneavoastra si stadiul acestora, sa efectuati operatii asupra lor sau sa creati o carte noua. [Aici putei accesa manualul acestei functionalitati](../help/880.30-BCAT_usage.md).




## Lista cartilor


[Creare carte](newb/) <!-- #NOTE action for new book -->


{% raw %}

<table markdown>
<thead markdown>
<tr markdown>
<th>ID</th>
<th>Cod</th>
<th>Titlu scurt</th>
<th>Titlu lung</th>
<th>Note</th>
<th>creata de</th>
<th>data creare</th>
<th>actiuni</th>
</tr>
</thead>
<tbody markdown>
{% for book in bcat_data %}
<tr markdown>
<td markdown>{{ book.id }}</td>
<td markdown>{{ book.code }}</td>
<td markdown>{{ book.short_desc }}</td>
<td markdown>{{ book.description }}</td>
<td markdown>{{ book.notes }}</td>
<td markdown>{{ book.created_by }}</td>
<td markdown>{{ book.created_date }}</td>
<td markdown> <!-- #NOTE actions for edit, organize, assembly book -->
    [editare](edtb/) - [organizare](orgm/) - [vizualizare](prvb/) - [asamblare](dplb/)
</td>
</tr>
{% endfor %}
</tbody>
</table>

{% endraw %}






