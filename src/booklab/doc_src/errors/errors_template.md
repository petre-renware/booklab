# Rezultatele  executiei

{% raw %}


## Erori de procesare

In urma executiei au fost semnalate urmatoarele **erori**:

{% for err in errors %}
1. {{ err }}
{% endfor %}




## Consola executiei

```
{{ console_out }}
```




{% endraw %}

