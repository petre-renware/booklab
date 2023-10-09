**BookLab by RENware Software Systems**

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- #NOTE sote publishing on `arint.renware.eu` from `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified



## 0.2 First System Design (...wip...)

* tbd... after BTMPL release 0.2 then focus on Jupiter








### 0.2.4 BTMPL Book Template 1st design (...wip...)

* tbd... now have enough information in JSON data to construct `book_tnpl/book_config_parts/cfg_01_head_yml_section.yml`:
    * site_name == short_desc
    * site_author == site_author
    * copyright == copyright

* tbd.. all CGI executables must accept as parameter the **Book IDENTIFIER** (_except NEWB corresponding operation_)

* tbd... move all book scripts from book template dor to CGI dir


* wip...

* --- #TODO test, review & publish upper me ---

* 231009piu_c reviewed & closed book configuration file assembler (`doc_src/book_tmpl/book_config_parts/bkcmd_assembly_cfg_file.sh`) & cleaned book tepmplate directory and files

* 231009piu_b created `cgi-bin/bash_model.sh` as model usable for bash scripts, containing reusable general code parts

* 231009piu_a NAMING RULE of all command book manipulation scripts: __all scripts prefixed with `bkcmd_...`__

* 231008piu_b created a script for book configuration file (`mkdocs.yml`) assembly ==> `doc_src/book_tmpl/book_config_parts/bkcmd_assembly_cfg_file.sh`

* 231008piu_a updated system overview doc with examples / references of BookLab usage

* 231007piu_b updated `doc_src/data/books_catalog.json` add at book level `copyright`, `site_author`, information intended to be used in **book mkdocs.yml** build process

* 231007piu_a more items:
    * updated `doc_src/make_env.sh` to make executable `*.sh` and `*.py` files
    * created and initialized `doc_src/libutil/` directory for general project specific reusable modules (used in CGI scripts execution)
    * published this updated version

* 231005piu_b updated `doc_src/` and `doc_src/cgi-bin/` made in git all `*.py, *.sh` files as EXECUTABLES
* 231005piu_a updated `doc_src/make_env.sh` with commented commands to make `*.py, *.sh` files as _Linux executables_ (for `CGI` purposes)
* 230918piu_c adjust CGI python model file, rename to `cgi-bin/python_model.py` and set how get b00k_catalog.json database and query parameters
* 230918piu_b review & update `cgi-bin/__model.py`. Publish
* 230918piu_a python template for CGI purposes ==> `cgi-bin/__model.py` basically containing:
    * write _HTTP header_ for different MIME types
    * accessing _ENV useful variables_




















### 0.2.3 HELP Update BCAT documentation (wip...)

* 230917piu_a updated `mkdocs.yml` make entry for `help/880.30-BCAT_usage.md`

* 230916piu_c updated `880.30-EUMA_catalog.md` make entry for `help/880.30-BCAT_usage.md`

* 230916piu_b updated `bcat/bcat.md` make a simple link @ top of page ref `help/880.30-BCAT_usage.md`




### 0.2.2 BCAT Books Catalog version that only show (230916 h06:00)

* 230916piu_a BCAT markdown template - actions column FIXED links that are not correct generated from markdown to html - fixed `<tbody>` element, dropped all `<table>` tag indentation to avoid generation of _code block_

* 230915piu_b more action:
    * [x] BCAT DSGN doc `810.05a-bcat_System_Process.md`- MOVE book template section && 810-DSGN/Landscape mv BCAT in its doc: __exists a dedicated module == BTMPL__
    * [x] BTMPL DSGN DOC `doc_src/810-DSGN/810.05a-btmpl_System_Process.md` updated with info from BCAT
    * [x] in Landscape, components DIAGRAM doc put BCAT under dynamic server

* 230915piu_a `bcat.md` template solve catalog table problem because was spitted in 2 different sections by Jinja statements

* 230914piu_e moved `cgi-bin/bcat/bcat.py` to `cgi-bin/` to be at exact 1 level under www-root as tem0late `bcat/bcat.md` to right address CSS ad JS scripts referred as relative paths to `../assets/...`

* 230914piu_d (RMAP.001 item 4): BCAT CGI script to prepare Jinja variables and render template `bcat/bcat.html` (!!! NOT MD)

* 230914piu_c FIXED BCAT script (`cgi-bin/bcat/bcat.py`) shows data but need to redesign all markdown template (`doc_src/bcat/bcat.md`) as it looks very ugly... 

* 230914piu_b ___WITH ERRORS - see code___ (RMAP.001 item 4): BCAT CGI script to prepare Jinja variables and render template `bcat/bcat.html`

* 230914piu_a reviewed & updated:
    * CODE (`cgi-bin/bcat/bcat.py`)
    * BCAT template (`doc_src/bcat/bcat.md`) books catalog set Jinja variables in `for loop` to render all books (closed RMAP.001 item 3.a)

* 230913piu_f cleanup project of no more needed files, obsolete todo(s), comments in docs && moved `app_info.json` to `doc_src/data/` and updated `810.05a-bcat_System_Process.md`

* 230913piu_e reviewed & updated `cgi-bin/bcat/bcat.py` with a comment regarding info retrieved from JSON file (exactly how looks like @ print)

* 230913piu_d (RMAP.001 item 3.a): BCAT CGI `bcat.md` books catalog set Jinja received variable & update `810.05a-bcat_System_Process.md` section "Catalogul cartilor - interfata UI"

* 230913piu_c updated `810.05a-bcat_System_Process.md` described _Books Catalog_ database (`/data/books_catalog.json`): keys, types and rules




### 0.2.1 BCAT setup a Python CGI running environment (230913 07:30)

* 230913piu_b reorganized left navigation for HELP zone

* 230913piu_a made Linux executables (`chmod +x`) all required `*.sh` & `*.py` files

* 230912piu_e fix small bugs, comments. Archive 1.0 Changelog

* 230912piu_d more items:
    * installed in doc_src/ an env for HTTP srv CGI part ==> __`<http srv root/pyenv>`__ (attn not hidden & start in doc_src/)
    * created `setup/booklab_install.sh` for sys install and put some important comments ref TODOs when you start its development

* 230912piu_c fixed `raw - endraw` Jinja section in DSGN `810.05a-bcat_System_Process.md` document

* 230912piu_b update BCAT `810-DSGN/810.05a-bcat_System_Process` to show (link or in doc ?) the template doc (`doc_src/bcat/bcat.md`) ...OPTIONAL put this item on RMAO.001

* 230912piu_a **BUGS2FIX** (RMAP.001 item 3.b) BCAT python script open database file raise error `ERROR: ModuleNotFoundError: No module named 'pysondb'` and changing the shebang to `../../.env/bin/python3` raise `[Errno 2] No such file or directory: '/mnt/d/_T0_PROJECTS/0000-0163 BookLab/830-DEV/static_portal/cgi-bin/bcat/bcat.py'` && publish to have on git in `docs/`

* 230911piu_c (RMAO.001 item 3.a) BCAT template (bcat/bcat.md) sketch and notes ref how make the table rows loop

* 230911piu_b fixed BCAT `bcat/index.md` redirect URL to be agnostic to server & port (set to a relative path to `url='../cgi-bin/bcat/bcat.py'`)

* 230911piu_a (RMAP.001 item 4): BCAT CGI `bcat.md` books catalog first attempt, combined `bcat/index.html` redirect to `cgi-bin/bcat/bcat.py` ==> PASS

* 230910piu_c work to RMAP.001:
    * [x] 2. BCAT `index.html` file remain and _redirect_ to `cgi-bin/bcat/bcat.py` (helps to keep route calling w/o file name for future WSGI full compatibility)
    * [x] 3. old `index.md` renamed to `bcat.md` (RMAP spec: the component template file `<component_name>.md` with raw Jinja to remain in markdown and becomes HTML (after mkdoc compile) as subject to be rendered by python script
    * [x] 4. partial, made a plan in `cgi.../bcat.py`

* 230910piu_b created `cgi-bin/bcat/test.py` as copy fo `cgi-bin/whoami.py` to test crt dir when use subdirs, also initialized as python modules (`__init__.py`) and  created a `cgi-bin/libutil/bl_lib.py` to accommodate various misc general python objects ==> *CONCLUSION*: crt dir is the same, the HTTP server root `static_portal/` in test - publish this version

* 230910piu_a created `cgi-bin/whoami.py` to test CGI scripts running. Use that script as start template in scripting. Test cmd `localhost:8000/cgi-bin/whoami.py`.
    >**IMPORTANT CONCLUSION:** current directory at script level is HTTP server root directory == **`docs/`**

* 230909piu_f more actions:
    * [x] some clarification ref `PRVB` process ref HTTP server that will serve the book for preview ==> this should run on a port DIFFERENT than 80 which is reserved for main application
    * [x] cleared the pair of `(start)(stop)_(static)(dyn)_server.sh` and let just one pair for _start_ & _stop_ the same BookLab HTTP server (just one with CGI option) ==> `start_booklab_server.sh` & `stop_booklab_server.sh`

* 230909piu_e more actions:
    * [x] refactored `book_tmpl/` directory moved under `doc_src/` (`docs/` in production)
    * [x] updated DSGN documents: `810.02-System_Landscape.md` & `810.05a-sysInit_System_Process.md`
    * [x] created directory `doc_src/cgi-bin/` (`docs/cgi-bin/` in production) for Python scripts to be run on server-side

* 230909piu_d test `bcat/index.md` Pyodide run in markdown for what is generated as HTML page - FACTS:
    * no script to run `pyodide` include neither in header or in other place
    * pyodice section is almost like any block code - something is not correct initialized for plugin (remeber, files and python execution fences work)

* 230909piu_c save 0.1.3 tag and last site built zip rename to 0.1.3











# Archived CHANGELOGs

* [0.1 First System Design](version_history/CHANGELOG_v0.1.md)


