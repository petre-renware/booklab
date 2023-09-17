
**BookLab project**

***

***Table of contents***

[TOC]


# ROADMAP

## RMAP.001 - BCAT structure (closed)

* **Objective:** BCAT start for a new structure with python as CGI
* **Recorded at:** 230908
* **Updated at:** closed @ 230916
* **Recorded by:** piu
* **Detailed  description:**
    * [x] 1. main python file will be `cgi-bin/<component_name>/<component_name>.py` (_CONCLUSION_: `<crt_directory>` is HTTP server root `docs/`)
    * [x] 2. `index.html` file remain and _redirect_ to python (helps to keep route calling w/o file name for future WSGI full compatibility)
    * [x] 3. the template file `<component_name>.md` with raw Jinja to remain in markdown and becomes HTML (after mkdoc compile) as subject to be rendered by python script
    * [x] 3.a update template file `<component_name>.md` Jinja code
    * [x] 3.b open & load `bcat_catalog.json` database
    * [x] 4. python script to render template, ways to render component html:
        * [OK]==> (4.1) load it as string, render and print it (including application type as in examples)
        * [NO]==> (4.2) set template dir in `<crt_directory>/<component_name>` (remember, current dir is the HTTP server root)
    * [x] 5. file to render should be always `docs/<component_name>/<component_name>.html`
    * [x] 6. update DSGN documentation (`810.02-System_Landscape.md`)
* **Recommendations:** -
* **Known dependencies:** -
* **Assigned to:** piu
* **References & notes:** -

