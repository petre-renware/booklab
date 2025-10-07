**BookLab by RENware Software Systems**

[TOC]


# CHANGELOG

## ... #TODO future things:
* tbd... Jupiter Notebooks
* tbd... ref command "Verificare" (code-name `bstatus`):






## ... [0.8] - unreleased Implement `bldb` and
update `book_template` (aka `btmpl`) functionalities:
* tbd... MyBook method to render `mkdocs_template.yml` --> `mkdocs.yml`
   chk if can render from a parent dir, ie `../my_books/<book_code>/docs/`
    or render from string by reading file
* tbd... mkdocs_template: upd nav secrion with Jinja data-items
* tbd... ref up iss, create MyBook method that render its mkdocs.yml




## ... [0.8] - unreleased
* tbd... update api_bstatus() to use MyBook.getBookURL() to show url path where book can be seen
* tbd... update api_bstatus() to use MyBook.getBookPath() to show location and drop that info from data/book_catalog.json
* [0.8a23] update my_books/books_catalog.json for "store_location" key and upd MyBook.getBook() method to fill in this key "on the fly" (not update of source json data)
* [0.8.dev22] update my_books/books_catalog.json making full flat structure: drop "status" key and move its keys one level up + "location" key that will be obtained through MyBook class
* [0.8.dev21] updateded project README.md with installation steps
* [0.8.dev20] fix db_init.py to return None for db_ystem (was dropped) to remain for future use and. Move this file to booklab root
* [0.8a19] MyBook.getBookPath() to chk if directory exists and if not return None
* [0.8.dev18] reorg project: drop dir data/ and mv books_catalog.json to my_books/. Update booklab.__init__.py for DATA_ROOT directory and db_init
* [0.8b17] MyBook: method `getBookURL()` to return MY_BOOK_URL and update routes.py function api_prvb()
* [0.8b16] create MyBook class methods that return paths and urls:
    * build doc + package + publish them
    * [0.8a16] use MyBoook property MY_BOOK_URL in routes.py on route /api/prvb/ (ie, book preview) to redirect to book site
    * [0.8.dev16] MY_BOOK_URL for root url to current book `EXTERNAL-<SERVER_NAME>/external-prefix_path/my-books/<book-code>/docs/`
* [0.8.dev15] clean project and improve adresability:
    * use `w3lib.url` to normalize urls at their construction in booklabd/routes.py
    * rollback commut [0.8.dev14] but replace /preview/ eith /my-books/
    * MY_BOOK_PATH as root (path) of a book directory
* [0.8.dev14] upd nginx config, let just /api/ location (but, in fact,is not needed)
* [0.8.dev13] booklab: MY_BOOKS_ROOT pointing to location where end user books location: .../src/booklab/my_books/
* [0.8b12] my_books:
    * fixed bstatus page with small formatting / display inconsistency between same info groups
    * upd `/api/bstatus/` & `/api/prvb/` to use MyBook.getBook method instrad of function getBook
    * move actual function `getBook` as method of class myBook
    * add class var `db` to have web app initialized database objec6
    * boklib: create my_books.MyBook class that manage my books. At init get a book code, Flak application that will use object and set them as instance variables
* [0.8a11] all scripts moved from booklab/ in booklab/scrpts/ directory
* [0.8.dev10] server-run.sh: upd PID save dir from /tmp to ~ and make file hidden
* [0.8.dev9] server-run.sh. upd loading config file to load it as Python module
* [0.8.dev8] server-run.sh: upd config file name and location + get at its load the PACKAGE_ROOT
* [0.8a7] booklab data & template: move "navigation" item entierly into a new JSON in book_template --> `book_navigation.json`
* [0.8a6] booklab static-site bcat_template.html
    * drop column ref actions
    * column book_code value, make as link to existing bcat_status
* [0.8.dev5] fixed 0.8.dev4 ref server-run.sh bug at restart option, PID file location
* [0.8.dev4] updated booklab/server-run.sh to run and load config file regardless of crt dir where is launchrd
* [0.8a2] make a script that generate API doc (ref PDM scripts) the append str "[TOC]" at the beginning (script "booklab/gen-api-doc.sh")
* [0.8a1] static site: review "About menu", clean it and make a page "About Booklab" with version, licence, author(s)
* [0.8a0] create script `src/booklab/master_site_build.sh/` to mkdocs-build the Booklab static site and hard-link resulted docs/ ditectory to project root (to be published  by GitHub on its servers)
* [0.8.dev3] enhance booklab/data/books_catalog.json book navigation structure with a right dict usable in nav section generation of mkdocs.yml
* [0.8.dev2] update booklab/data/books_catalog.json with a section dedicated to book navigation structure (orgm functionality) targeted to go in book configuration file (mkd9ks.yml)
* [0.8.dev1] create and update booklab/my_books/book_template/mkdocs_template.yml with Jinja fields to reflect current book config by rendering it at book build
* [0.8.dev0] review & plan-for all command scrips from book template (btmpl)




## [0.7] - 27.sep.2025
Implement  `prvb` and update `book_template` (aka `btmpl`) functionalities:
* [0.7rc0] test, build doc, build package, publish
* [0.7a2] 250927 routes.py:
    * code for preview route (`/api/prvb/`) for a book resulted static-site as route /preview/<my_book_code>/docs/
    * make a new `prefix_URL_path` dedicated to `my_books` as **`<SERVER PREFIX URL>/preview/`**
* [0.7a1] routes.py: make route `/api/bbld/` as TODO-skeleton for book build (cmd mkdocs build)
* [0.7a0] bstatus_template: change Edit action, disable it for closed books && mk cmd link for build book
* [0.7.dev6] created in my_books/book_template shell `bk_build.sh` that build mkdocs site. Shell self-auto change directory to the book directory for which it exists assuring a correct building with mkdoks build cmd
* [0.7.dev5] copy Booklab mkdocs.yml to make a test of my 1st book generation and manual preview of it
* [0.7.dev4] my_books/: continue skeleton with directories `doc_src/`& `docs/` with minimum files to be kept on git and to be useful
* [0.7.dev3] configure nginx for /preview route/ pointing to .../booklab/my_books/  
* [0.7.dev2] define and set directory layout for book TMPLT (ie, book `code` from books_catalog.json`) directory under package book_template. This will become the "structure" created for any new book
* [0.7.dev1] refactor sub-package `book_template` to sub-package `my_books` containig it
* [0.7.dev0] create a new sub-package boooklab.book_template to be used for a new book creation as base template "decorated" with Jinja params
* [0.7b0] 250924 clean project and permanetly keep a copy of `.../src/booklab/docs/` in project root




## [0.6] - 24.sep.2025
Refactor WSGI app (booklabd), move static site (docs/) from booklab project root to package root
* [0.6b1] 250924 drop /<PROJECT ROOT>/docs/ dir & update booklab code to change all hard-coded (in clear) file-path refs to `data/` with `api_app.static_path` variable
* [0.6b0] 250924
    * update booklab code to use PACKAGE_ROOT instead of PROJECT_ROOT when define paths to static/docs
    * update booklab.__init__.py STATIC_SITE_ROOT with new location under paxkage root
* [0.6a0] 250923
    * move static site inside booklab package. Keep name as `docs/`
    * make a sym-link in project root directory to preseve publishing through GitHub
    * move doc-src and mkdocs.yaml to make right compilation in new directory where moved




## [0.5] - 22.sep.2025
Implement `bstatus` functionality:
* [0.5rc1] make menu link in "technical area" to data/book_catalog.json (see 0.5a0)
* [0.5rc0] 250922
    *  update all redirects using EXT_PATH
    * created gh-workflow to publish booklab package on PyPi
    * bstatus_template.md increase "clarity" of cmd  buttons
* [0.5b3] 250921
    * update bstatus_template to a presentable firm of information
    * import external URLs at booklab.__init__.py level
    * construct a FULL_EXT_URL from parts
    * create booklab-config-file  `.../booklab/conf/booklab_ext_url.py` for external access URL parts
* [0.5b2] 250919 render bstatus_tenplate.md as a first proof of concept and test
* [0.5b1] create lib function `getBook(bk_code)`
* [0.5b0] `booklab` refactor: move db_init.py from module `booklabd` to module `booklib`
* [0.5a2] 250917 create `booklab.booklib` module for Booklab app general purpose functions
* [0.5a1] 250917
    * bcat/bcat_template.md -copy-to-> bstatus_bstat_template.md
    * update page header and explana in text
* [0.5a0] 250917
    * clean all technical documentation and modules docstring
    * update 810-DSGN with `bstatus` component and change text CGI with WSGI
* [0.5.dev2] 250916 update `books_catalog.json` with data requured by `bstatus` functionality
* [0.5.dev1] 250916 clean prj docstrings and dirs & files
* [0.5.dev0] 250916 init 0.5 version




## [0.4] - 16.sep.2025
First booklabd as Flask web app to serve `/api/.../` routes:
* [0.4rc4] 250916 static site: upd with a note/chapter ref "Demo public site" where explain that public site contains data from more users and respect them managing only your data
* [0.4rc3] 250915 FIRST OPS DRAFT: booklabd make all opers `/api/xxx/` routes showing `code` query param and `wip.md` page and comment to get querry parameters
* [0.4rc2] 250913
    * booklabd index route, keep that w.<any_path> and for param as "" (blank) go to docs/index otherwise display act msg except url_for to see what user tried to access
    * booklabd-run.sh improved operating interface / commands follow POSIX specs
* [0.4rc1] 250912
    * static site: `bcat_template.md` upd all ops refs with full booklabd addressing to correspunding dir index.html preserving query parameters
    * all ops dirs uncomment `index.html` meta tag and upd right /api/... address
    * static stite: copy custom CSS from bcat/ to all book ops dir-pages
* [0.4rc0] 250911-a on static site:
    * all book opers except bcat & newb make index auto redirect to bcat (duplicate index.html from .../bcat/)
    * upd root page ref to ops keep only /bcat/ and /new/
* [0.4b14] 250910-b static site: create all book-operations directories with a fake index.html copy from /bcat/index.html and a "_todo...txt" file to mark that need updated
* 250910-a cleaned project
* [0.4b13] 250910-a static site: left nav keep as operations only "Catalog carti" and "Creare carte"
* [0.4b12] 250909-c bugfix ref [0.4b10] need to update docs/bcat/bcat.js that control in table dropdown. Drop it and replace with a simple links list
- 250909-b cleaned project
* [0.4b11] 250909-a fixed mkdocs to run and dropped PDF creation for pages
* [0.4b10] upd site /bcat/bcat_template.md dropdown in table mk unique its ID with book_code because is the same button regardless of table row
    - closed as NOT acceptable. Need future review and mkdocs upd config to be able to run w/o errors
* [0.4b9] make gunicorn to save PID & make command `k` to kill it ++ cmd `s` to show gunicorn processes pid
* [0.4b8] 250908 booklab.__init__.py create api_app.config[...] for all directory constants
* [0.4b7] 250908 booklabd.routes.py create `/` route to be able to access booklab app also with simple / not obly by /docs/
* [0.4b6] 250908 booklabd created route "/" for static site root to avoid "/docs/" =ath but dosn't work because is set by host proxy ...
* [0.4b5] 250907 configure Flask proxy middleware to eliminate need of `/booklab/` specify in module URL redirections:
    - closed as NOT acceptable. let code as comment in `booklabd.app_init.py`. need to determine where specify # of proxies
* [0.4b4] 250905-a upd booklabd app to right access static site when addressed from booklabd (ex when access menu from /api/bcat page)
* [0.4b3] 250904-b booklabd create index route "/" to server static site as being. TEST.OK except CSS theme rendering
* 250904-a upd nginx conf with prixy params to be used for a clean proxy (not "hiding" source info)
* 250902-b upd bcat/index.html to redirect to booklabd route
* 250902-a clean project files
* 250901-c booklabd.templates render bcat
* 250901-b update version string and set Flask root directory as project dir (to be able to address docs/ dir as template dir)




## |0.4b2] - 01.sep.2025
Create database (aka `db*`) objects for JSON files and a test `/api/bcat` route:
* 250901-a a test route for /api/bcat/ to write sone data in books catalog
* 250831-c init the `db` objects to JSON databases:
    * `init_db.py` module and ref it in `__init__.py`
    * `db_books` for booklab.DATA_ROOT --> books_catalog.json
    * `db_system` for booklab.DATA_ROOT --> app_info.json
* 250831-b `booklab.booklabd.__init__` imported working directories (created in prev change)
* 250831-a `booklab.__init__` create constants: PACKAGE _ROOT, DATA_ROOT, CONF_ROOT
* 250830-b make gunicorn config python module in `booklab.conf` module (as new one)
* 250830-a config for for gunicorn in serving `booklabd` server web app. file is symlinked to project root to be correct executed with pdm run as tool script




## [0.4b1] - 29.aug.2025
Update Flask structure to be able to have exposed basic objects (app, db, ...l and to be served by gunicorn as daemin:
* 250829-d cleaned and update `booklabd` code. Prep route `/api/bcat/` with a sample test return
* 250829-c updated `booklab/booklabd-run.sh` to listen on `port 8000` and to reload when app files changes
* 250829-b made `bklab_srv` PDM script to start booklabd server. TEST.OK
* 250829-a updated `booklab/booklabd-run.sh` to allow exec as daemon if arg#1 id "d"
* 250828-a created `booklab/booklabd-run.sh` to start booklad web server on _port 5003_
* 250827-a installed `gunicorn` as pj depedency. TEST run from pj root with obj `booklab.booklabd:api_app` TEST.PASS
* 250826-d booklabd.api_app set `static_folder` to same as tenplates (booklab static site ref <PJ-ROOT>/docs/)
* 250826-c booklabd.api_app set `templates` dir to point to `<PJ-ROOT>/docs/`
* 250826-b started booklab/booklabd-run.py intended to run web application. TESTED.OK address of `api_app` object
* 250826-a booklabd/routes.py created a route for /api/bcat/. Run OK. Need test efective route exec in browser




## [0.4a1] - 25.aug.2025
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




## [0.3.1] - 03.oct.2023
BCAT group commands:
* 231023piu_b updated `RELNOTE.md` and published site
* 231023piu_a group commands in a dropdown
* 231022piu_a update `bcat.md`
    * [x] clean the `table HTML` section, drop `markdown` attribute and use normal link HTML tags
    * [x] add new command "Verificare" (status check / code-name `bstatus`)
* 231021piu_a small fixes in 'bcat.md`




## [0.2] - sep.2023
First version of BCAT (book catalog) and TMPL (book template)




## [0.1] - aug.2023
First System Design





