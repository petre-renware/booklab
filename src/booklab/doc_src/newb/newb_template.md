
# Carte noua

Introduceti mai jos informatiile despre carte.

{% raw %}

{% from "/developer/form_macro.jinja" import render_field %}

<form method=post>
  <dl>
    {{ render_field(form.short_desc) }}
    {{ render_field(form.description) }}
    {{ render_field(form.copyright) }}
    {{ render_field(form.site_author) }}
    {{ render_field(form.notes) }}
    {{ render_field(form.closed) }}
    {{ render_field(form.save) }}  
  </dl>
  <p><input type=submit value=Save>
</form>

{% endraw %}

