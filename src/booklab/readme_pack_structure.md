# booklab package components

Booklab is composed from the following sub-packages:

* **booklabd** - the server API with role to serve dynamic pages which need interaction with system database
* **booklab_cli** - a command line application used to manage system
* **data** - contains the system database basically as JSON files
* **book_template** - contains the template (directory) to be used when create a new book 
* **conf** - contains various configuration files used by system components including infrastructure ones like WSGI web server (gunicorn), proxy server (nginx)
* **doc-technical** - contains techical system documentation (aka DLD, developer and administrator level)
* **docs** - the generated HTML static site
* **doc-src** - the static site raw source as Markdown files




