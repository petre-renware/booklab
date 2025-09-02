# Booklab - source code

Booklab is composed from the following sub-packages:

* **booklabd** which is the server API with role to serve dynamic pages which need interaction with system database
* **booklab-cli** which is a command line application used to manage system
* **data** which contains the system database basically as JSON files
* **conf** which contains various configuration files used by system components including infrastructure ones like WSGI web server (gunicorn), proxy server (nginx)
* **doc** which contains techical system documentation (developer and administrator level)
* **docs** (note 1) is the generated HTML static site
* **doc-src** (note 1) is the static site raw source as Markdown files


#### note 1 - ref components physical organization
- Source code is structured as Python3 package and sub-packages are organized as distinct directories.
- Static site components reside outside if `src/` directory (but still in project root). Reason is the need to publish static site through _GitHub_ public system.


