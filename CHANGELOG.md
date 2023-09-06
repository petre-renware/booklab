**BookLab by RENware Software Systems**

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with (F) are marked those changes that are features in order to be copied in a RELNOTE file
- #NOTE sote publishing on `arint.renware.eu` from `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context)
- `<APP_ROOT>/` is the application root directory, as default `booklab_app/`



## 0.1 First System Design (FUTURE...)

* -#NOTE@IMPORTANT at a moment __publish `booklab.renware.eu` in RENware catalog & main portal__

* tbd...cu ce faci [editarea textului markdown "clasic"](https://blog.miguelgrinberg.com/post/flask-pagedown-markdown-editor-extension-for-flask-wtf). Also Jupiter notebook PLUG IN has editor, check it

* #NOTE... HTML form in markdown and what POST is sent on submit - see commented section at beg of project `index.md`
* #NOTE... here too, at each component _markdown_ use _Jinja raw block or simple escaping_ to allow for server 2nd processing (for ex at FormsWTF)







### 0.1.3 System Detailed Design (LLD) BCAT component - catalog data and client UI (wip...#TODO)

* -NOTE (vezi daca faci si client UI in aceast pach...)

* ...#NOTE TESTUL CORECT: toate comenzile shell merg din directorul fiecarei carti (`bk_tmpl/` acum), individual pentru acea carte si numai pentru ea

* tbd... finish `books_metainfo/bk_tmpl/bkcmd_start_book_preview.sh`:
    * [ ] give it a final clean form (#NOTE consider to make both versions, Linux SHELL and Windows CMD)
    * [ ] insert _shebang `!#`_ directive
    * [ ] Linux shell version make executable
    * [ ] move it to `<BOOK ROOT>/` to be available to run IN FINAL ASSEMBLED APP (for dev project in `<PROJECT ROOT>`


* wip...


* ---#TODO publish all up ---

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


