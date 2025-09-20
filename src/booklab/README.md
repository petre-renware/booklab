# Booklab - source code

Booklab is composed from the following sub-packages:

* **booklabd** - the server API with role to serve dynamic pages which need interaction with system database
* **booklab-cli** - a command line application used to manage system
* **data** - contains the system database basically as JSON files
* **conf** - contains various configuration files used by system components including infrastructure ones like WSGI web server (gunicorn), proxy server (nginx)
* **doc-technical** - contains techical system documentation (aka DLD, developer and administrator level)
* **docs** (note 1) - the generated HTML static site
* **doc-src** (note 1) - the static site raw source as Markdown files


#### note 1 - ref components physical organization
- Source code is structured as Python3 package and sub-packages are organized as distinct directories under `.../src/booklab/`
- Static site components reside outside if `src/` directory (but still in project root). Reason is the need to publish static site through _GitHub_ public system


