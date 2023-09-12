
**BookLab project**

***

***Table of contents***

[TOC]


# ROADMAP

## RMAP.001 - BCAT structure

* **Objective:** BCAT start for a new structure with python as CGI
* **Recorded at:** 230908
* **Updated at:** piu@230911
* **Recorded by:** piu
* **Detailed  description:**
    * [x] 1. main python file will be `cgi-bin/<component_name>/<component_name>.py` (_CONCLUSION_: `<crt_directory>` is HTTP server root `docs/`)
    * [x] 2. `index.html` file remain and _redirect_ to python (helps to keep route calling w/o file name for future WSGI full compatibility)
    * [x] 3. the template file `<component_name>.md` with raw Jinja to remain in markdown and becomes HTML (after mkdoc compile) as subject to be rendered by python script
    * [wip...] 3.a update template file `<component_name>.md` Jinja code
    * [wip...] 3.b open & load `bcat_catalog.json` database
    * [ ] 4. python script to render template, ways to render component html:
        * (4.1) load it as string, render and print it (including application type as in examples)
        * (4.2) set template dir in `<crt_directory>/<component_name>` (remember, current dir is the HTTP server root)
    * [ ] 5. file to render should be always `docs/<component_name>/<component_name>.html`
    * [ ] 6. update DSGN documentation (`810.02-System_Landscape.md`)
* **Recommendations:** -
* **Known dependencies:** -
* **Assigned to:** piu
* **References & notes:** -














## Template

```
## RMAP.item_code - -#NOTE `<give a hort human name of item>`

* **Objective:** -#NOTE `<the item objective>`
* **Recorded at:** -#NOTE `<date of recording this item>`
* **Updated at:** -#NOTE `<after Implementation start record here the status and last updated date>`
* **Recorded by:** -#NOTE `<who registered this item - this should identify that person as mail and phone, otherwise these should be written here>`
* **Detailed  description:**
    * -#NOTE `<here different items of description>`
    * -#NOTE `<here different items of description>`
* **Recommendations:**
    * -#NOTE `<here different hints / recommendations>`
    * -#NOTE `<here different hints / recommendations>`
* **Known dependencies:** -#NOTE `<if there are knwon dependencies of INTERNAL system components or other open / wip issues>`
* **Assigned to:** -#NOTE `<the person nominated to respond for this roadmap item>`
* **References & notes:**
    * -#NOTE `<more notes... (if use footnote like [^xxx]: ..., please do not mark as list entry because will appear at foonotes)>`

```

