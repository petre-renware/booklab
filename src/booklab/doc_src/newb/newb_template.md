
# Carte noua

Introduceti mai jos informatiile despre carte.

{% raw %}

{% from "/developer/form_macro.jinja" import render_field %}

<form method='POST'>
  {{ form.csrf_token }}
  {{ form.hidden_tag() }}
  <dl>
    {{ render_field(form.short_desc) }}
    {{ render_field(form.description) }}
    {{ render_field(form.copyright) }}
    {{ render_field(form.site_author) }}
    {{ render_field(form.notes) }}
    {{ render_field(form.closed) }}
  </dl>
  <p><input type=submit value=Save>
</form>

{% endraw %}

