**BookLab by RENware Software Systems**

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- #NOTE sote publishing on `arint.renware.eu` from `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified






## ... #TODO [unreleased] BCAT extend book command center (...wip...)

* tbd... #TODO-ASAP__focus on Jupiter__
* tbd... try to execute book manipulation scripts from a Jupiter notebook (as part of application interface)
* tbd... init TMPL with a start `index.md` file && maybe 1, 2 examples markdown as "starter samples"

* tbd... ref command "Verificare" (code-name `bstatus`):
    * [ ] VIEW CONFIG FILE (to display `book_mkdocs.yml`)
    * [ ] SHOW STATUS of assembly (what did in `0.2.4`), check if exists `book_mkdocs.yml.tmpl` that meaning `bkcmd_assembly...sh` was xecuted but not `bkcmd_render...py`
    * [ ] update 810-DSGN with `bstatus` component






## [... 0.4] First booklabd as Flask web app to serve `/api/.../` routes
* ...tbd upd site with a chapter ref "Demo public site" where explain that public site contains data from more users and respect them managing only your data
### |0.4b1] - wip...
Create `db...` objects and a test `/api/bcat` route:
* ...tbd a test route for /api/bcat/ to write sone data in books catalog
* ...tbd init the 2 db objects
* ...tbd api_app set `templates` & `static` dirs to point to `<PJ-ROOT>/docs/`
* 250826 booklabd/routes.py created a route for /api/bcat/. Run OK. Need test efective route exec in browser
### [0.4a1] - 25.aug.2025
Create basic Flask structure:
* 250825 tested pyproject.toml PDM run script `build_doc` created to generate booklab technical documentation
* 250825 booklabd created `api_app` web app object in __init.py__. Impoeted `routes.py` where tested web app object addressibg = OK. tbd: d3fine routes
* 250825 improved pyprojects.toml with automation tools. NEED TEST, let commented
* 240825 created booklabd.app_init.py
* 250824 upd version and import req packages for Flask and old CGI structure (to access JSON files as a database)






## [0.3a1] - 24.aug.2025
Create raw structure of booklab package:
* 250824 created basic Flask dirs in `.../booklabd/`
* 250823 created  `.../booklabd/templates` directory for Flask/Quart rendering with files as symlinks to static site from `docs/` (genetated by mkdocs)
* 250823 release 0.3.dev2 into development branch and update version to 0.3a1






## [0.3.dev2] - 23.aug.2025
Restructure and clean project for PDM package management:
* 250823 updated `pyproject.toml` to get version from booklab package __init.py__.__version__
* 250823 clraned root project dorectory of not usable now files
* 250823 copied from old CFI model the route-directory `.../bcat/` for Jinja templates
* 250822 updated pyproject.toml with PDM backend
* 250822 copied from old CGI model various useful files (requirements.txt, py templates, ...) to /src/.../old-misc-files/
* 250822 moved old `cgi-bin/` directoey to reuse code
* 250822 wip cleaning old pj structure and move to new one all intended to keep or reuse
* 250821 copied KSON databases from old cgi-bin to new booklab dirs
* 250821 update project structure to python std. created basic init, main, version python files with empty content to be updated
* 250820 switched project on PDM management






## [0.3.1] BCAT group commands (231023 h07:00)

* 231023piu_b updated `RELNOTE.md` and published site
* 231023piu_a group commands in a dropdown
* 231022piu_a update `bcat.md`
    * [x] clean the `table HTML` section, drop `markdown` attribute and use normal link HTML tags
    * [x] add new command "Verificare" (status check / code-name `bstatus`)
* 231021piu_a small fixes in 'bcat.md`










# Archived CHANGELOGs

* [0.2 First version of BCAT (book catalog) and TMPL (book template)](version_history/CHANGELOG_v0.2.md)
* [0.1 First System Design](version_history/CHANGELOG_v0.1.md)


# [Release Notes](RELNOTE.md)


