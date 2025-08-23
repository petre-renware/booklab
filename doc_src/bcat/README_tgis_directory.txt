## Note ref this directory content;

- All CSS, JS, Jinja HTML template files are subject to be l
moved, rendered and served by `booklabd` application.

- `index.html` should redirect to booklabd corresponding route exactly as in old CGI architecture redirects to a python code locatd in `cgi-bin/`
OR
- this redirection is solved from nginx root location *listening on other port*.
In this case, this directory shold be completely dropped, and referred only in navigator area (subject of `mkdocs.yaml` config)

