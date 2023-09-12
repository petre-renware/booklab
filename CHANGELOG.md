**BookLab by RENware Software Systems**

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- #NOTE sote publishing on `arint.renware.eu` from `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context)
- `<APP_ROOT>/` is the application root directory, as default `booklab_app/`



## 0.2 First System Design (...)


* tbd... after mk run python scripts as CGI, rlse 0.2 then focus on Jupiter




### 0.2.1 BCAT ... (wip...#TODO)

* wip.@.290911piu_c...  (RMAP.001 item 4): BCAT CGI `bcat.md` books catalog which need to be rewritten with a Jinja *`for loop`* to render all books

* tbd... BCAT python script open database file raise error `ERROR: ModuleNotFoundError: No module named 'pysondb'` (for dtls see `230912piu_a`)


* wip...

* ---#NOTE review and publish all up

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










-#FIXME to archive

## 0.1 First System Design

### 0.1.3 BCAT & books catalog data - first raw sketch (230909 h04:00)

* 230909piu_b load BCAT table with `mkdocs-table-reader-plugin` (installed & requirements.txt updated) and plugin `table-reader` (mkdocs.yml updated). PUBLISHED site

* 230909piu_a created project `ISSUES.md` and moved all open / tbd items in it

* 230908piu_c make 230908piu_b` shell files executable `chmod +x` & publish app

* 230908piu_b created in PROJECT ROOT:
    * [x] `start_staticbl_server.sh` that start in bck the static server (**`staticbl`**)
    * [x] `start_dynbl_server.sh` that start in bck the dynamic server (**`dynbl`**)
    * [x] `stop_staticbl_server.sh` that stop static server (**`staticbl`**)
    * [x] `stop_dynbl_server.sh` that stop dynamic server (**`dynbl`**)
    * [x] updated 810-DSGN `810.02-System_Landscape.md` ref the 2 servers `code-name`(s)

* 230908piu_a created in static server area (`doc_scr/` in development & `docs/` in production) and moved in `books_catalog.json` - objective: for future data improvements, ads, etc o have a dedicated directory and to keep static server root clean

* 230907piu_c more actions:
    * [x] clean `doc_src/data_copy/` dir created on `230907piu_a`
    * [x] move `books_catalog.json` from `books_metainfo/` to `doc_src/data/` (`docs/` in production after mkdocs compilation)
    * [x] move `app_info.json` from `books_metainfo/` to project root and drop this directory
    * [x] update 810-DSGN `810.02-System_Landscape.md`
    * [x] update 810-DSGN `810.05a-bcat_System_Process.md`

* 230907piu_b updated doc `810-DSGN/810.02-System_Landscape.md` show on graphical landscape as separated the STATIC & DYNAMIC parts of app

* 230907piu_a created `doc_src/data_copy/` directory which is intended to keep data copies (for rendering data in UI markdown files with Pyodide or JS). There is a todo NOTE (`NOTE_BCAT_table`) that is posted for future implementation

* 230906piu_e more actions:
    * [x] refactored `books_metainfo/` by moving directory `book_tmpl/` out in `<PROJECT ROOT>`
    * [x] created a new component **`book_tmpl`** from `bk_tmpl/`
    * [x] updated doc `810.02-System_Landscape.md`
    * [x] created corresponding detailed design doc `810.05a-btmpl_System_Process.md`
    * [x] created navigation entry & updated `mkdocs.yml`

* 230906piu_d update `doc_src/bcat/index.md` UI page with comments ref `Pyodide` to load catalog data table

* 230906piu_c #NOTE_IMP_#NOTE INSTALLED CHROME (file mvd to `setup/INSTALL-CHROME-On_WSL.md` dir) and WORKS MKDOCS GENERATION ON Linux - tested and published OK/PASS

* 230906piu_b raw update of `doc_src/bcat/index.md` with some intro text and skeleton for effective buttons, content and Jinja variable places

* 230906piu_a updated command `bkcmd_start_book_preview`, created `.sh` version (in dir `books_metainfo/bk_tmpl/`) to start a _light python HTTP server_ (NOTE: python version was renamed using `bkcmd_PY_...` in name)

* 230905piu_b more actions:
    * updated structure of `books_catalog.json`
    * installed `PysonDB` a JSON based lightweight Database for Python - testat rezultat pe `books_catalog.json` cu executabilul local (vezi mai jos) si testat si bblioteca python
    ```
    +----+------+------+-----------------+-------+------+--------------------------+
    | id | code | shor |   description   | creat | crea |          notes           |
    |    |      | t_de |                 | ed_da | ted_ |                          |
    |    |      |  sc  |                 |  te   |  by  |                          |
    +----+------+------+-----------------+-------+------+--------------------------+
    | 0  | BCAT | bk_t | Sablonul implic | 2023- | syst | Inregistrare obligatorie |
    |    |      | mpl  | it pentru o car | 08-01 |  em  |  de la instalare sistem. |
    |    |      |      |     te noua     |       |      |      Non editabila.      |
    +----+------+------+-----------------+-------+------+--------------------------+
    ```
    * publicat actualizarile din doc design detaliat BCAT

* 230905piu_b split database from `books_metainfo/` in 2 dbs, one for books and one for app itself data (meta data and configurations data) && updated doc `810.05a-bcat_System_Process.md`

* 230905piu_a `810.05a-bcat_System_Process.md` creare varianta de lucru cu informatii despre sectiuni si schelet cu ce contin acestea






### 0.1.2 System Landscape (HLD) (230904 20:00)

* 230904piu_e updated `810.02-System_Landscape.md` with a short presentation ref `Application Software Organization (810.05b)` as distinct section

* 230904piu_d add in doc_src file `ERR_LINUX_CHROME_PDF_FIXSOLVE.md `

* 230904piu_c made a short explanation ref to system FIRST INSTALL (PRIMA INSTALARE a sistemului), ref `setup/` directory in doc `810.02-System_Landscape.md` component `sysInit` + updated doc `810.05a-sysInit_System_Process.md` with same info

* 230904piu_b updated `810.02-System_Landscape.md` with BCAT component

* 230904piu_a updated all `...booklab.renware.eu.../xroute` routes to `...xroute/` in order to be agnostic to SERVER_NAME and to suppose that endpoint has a construction like `.../xroute/index.html`, ie directory containing an index.html fle

* 230903piu_e created "wip...upcoming" UI code-file for BCAT component as `doc_src/bcat/index.md` and referred as new app menu entry in `mkdocs.yml`

* 230903piu_d temporary created `component_XXX_UI_template/index.html` as model of how will need (WARNING: asap after use will be dropped)
to be client-side UI of each component

* 230903piu_c fixed bugs ref SERVER & CLIENT `code-name`(s) in doc `810.02-System_Landscape.md` as *it is the same* but only the `<server_name>` from URL route has different ports, ie `80` for client and `7111` for server

* 230903piu_b simple reorg of information in doc `810.02-System_Landscape.md`

* 230903piu_a create a `sysInit` component:
    * populate it with minimum files to make it usable module
    * created a detailed design document `810.05a-sysInit_System_Process.md`
    * updated `810.02-System_Landscape.md`
    * referred in navigation
    * published

* 230902piu_f review, fix, update and publish for `230902piu_d`, `230902piu_e`

* 230902piu_e updated `810.02-System_Landscape.md`:
    * add component BCAT catalogul cartilor (`books_metainfo/`) and summary description
    * new doc  `810.05a-bcat_System_Process.md` ref in navigation
    * updated all components ref to detailed docs to admonition style

* 230902piu_d updated `810.02-System_Landscape.md`, section _HLPS help asistenta si manuale_

* 230902piu_c created new components design documents as empty-wip files to be completed latter for:
    * newb --> `810.05a-newb_System_Process.md`
    * edtm --> `810.05a-edtm_System_Process.md`
    * orgm --> `810.05a-orgm_System_Process.md`
    * prvb --> `810.05a-prvb_System_Process.md`
    * dplb --> `810.05a-dplb_System_Process.md`
    * referred all of them in `Landscape` document and in navigation (`mkdocs.yml`)






### 0.1.1 System Landscape drafts (230902 17:45)

* 230902piu_b created a dir `books_metainfo/` and move move `bk_tmpl/` dir in + create an empty JSON: `books_catalog.json` for books catalog with meta data & information (@tested, generated new `docs/`)

* 230902piu_a create `setup/` directory for first application setup

* 230901piu_c created in `bk_tmpl/` a directory dedicated to *`mkdocs` configuration parts as `book_config_parts/`* that will be assembled in book master `bk_XXX_config.yml` (easier to `cat xxx >> bk_XXX_confif.yml`)

* 230901piu_b generate and publish new app (230901 h10:00)

* 230901piu_a more actions:
    * [x] renamed files of `bk_tmpl/doc_src/` to `raw_source_docs/` and let a note in corresponding `mkdocs.yml.new_name` (@cmd `mkdocs build --site-dir my_book/`)
    * [x] created `bk_tmpl/preview_book/` directory that will used for temporary book generation (@cmd `mkdocs build --site-dir raw_source_docs/`)

* 230831piu_g `810.02-System_Landscape.md` section dedicated to system start

* 230831piu_f more actions:
    * [x] `810.02-System_Landscape.md` add whole project directory tree to keep what consider
    * [x] add requirements.txt in `doc_src/` to make environment after deployment
    * [x] `mkdocs.yml` commented out `exclude_docs:` configuration up to clearing specs because it will not deploy `bk_*/` directories
    * [x] FILES (from `../bk_tmpl/`) `index.md.txt` & `print_page.md.txt` should remain with this extension. Just when NEWB oper (new book) will be renamed to `.md` altfel se transforma automat in HTML la construirea insasi BookLab
0831piu_e renamed all user command scripts with extension `.py` as intention to make them as Python code instead of OS shells (more OS agnostic)

* 230831piu_d renamed files of `bk_tmpl/docs/` to `my_book/` and let a note in corresponding `mkdocs.yml.new_name`

* 230831piu_c reorganized `doc_src/bk_tmpl/` directory as:
    * [x] its own `doc_src/` & `docs/` renamed inside `.readme.txt` hidden files to `readme_and_keep_me.txt` to have generation on their `docs/` at that book build (ie, its own `mkdocs build`)
    * [x] mv `bk_tmpl/index.md` file to `bk_tmpl/doc_src/`
    * [x] mv `bk_tmpl/print_page.md` file to `bk_tmpl/doc_src/`
    * [x] created `bk_tmpl/doc_src/CNAME` as empty file to be filled at NEWBook operation
    * [x] upd project `mkdocs.yml` to ignore `bk_*/` dirs at project build and let them as is (ie, will be user books and part of deployed apps as are they now)

* 230831piu_b made a test ref HTML form in markdown and what POST is sent un submit - see commented section at beg of `index.md` (saved this note on major version TBD section)

* 230831piu_a review all system, update links, fixed misspellings and publish

* 230830piu_k updated navigation, replaced About entry with first product page and a new about was created for "appendix" entries (contact, support, ...)
* 220830piu_j updated _System Overview_ ref type of usable content (product ASIS, no extension)

* 230830piu_i created as empty files (for future use) in ``doc_src/help/` files `880.30-EUMA_catalog.md` and `880.30-ADMA_catalog.md` and referenced them in NAVIGATION

* 230830piu_h mv `810.02-System_Landscape.md` doc + any future design docs to `doc_src/810-DSGN`

* 230830piu_g fixed `230830piu_e` by updating created files and adding new ones (shell cmd for creating new book in `doc_src/`)

* 230830piu_f populated `doc_src/bk_tmpl` with `print_page.md` which is mandatory

* 230830piu_e create `doc_src/bk_tmpl` as first of directories DEDICATED TO 1 USER BOOK & prep files that will be modified latter but just to there including command shell ones

* 230830piu_d reviewed new system start page (index,md file) and published (230830 h08:15)

* 230830piu_c redesign system `index.md` as it will be the starting point of **BookLab system**

* 230830piu_b change theme color and publish site

* 230830piu_a drop prefix 810-DSGN - is in name as 810 and for other dlvbs (chk for adma, euma but if need prefix them with 880...):
    * [x] (1) file `810-DSGN-130.02-Overview.md`
    * [x] (2) file `810-DSGN-810.02-System_Landscape.md`

* 230829piu_i make navigation entry for `810-DSGN-810.02-System_Landscape.md`

* 230829piu_h updated `810-DSGN-810.02-System_Landscape.md` ref _Introducere_ by briefly re-iterating the general landscape from `System_overview.md`

* 230829piu_g created and initialized `810-DSGN-810.02-System_Landscape.md`






### 0.1.0 System Overview (12:30)

* 230829piu_f reviewed & published 230829 h12:30

* 230829piu_e create dir & move all documents from `doc_src` under `doc_src/help/` to "let place for application under `booklab.renware.eu` for application" and keep just `index.md` file which will guide for application start - reorganizare navigation bar so all docs will be the HELP module in future application

* 230829piu_d set new app logo `pictures/booklab_logo.png`

* 230829piu_c update `810-DSGN-130.02-Overview.md` with a very structural HLD Architecture

* 230829piu_b uploaded a logo picture

* 230829piu_a initialized directory for application `booklab_app/` as empty, just to lock application code-name













# Archived CHANGELOGs

* n/a


