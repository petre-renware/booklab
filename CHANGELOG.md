**BookLab by RENware Software Systems**

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with (F) are marked those changes that are features in order to be copied in a RELNOTE file
- #NOTE sote publishing on `arint.renware.eu` from `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context)
- `<APP_ROOT>/` is the application root directory, as default `booklab_app/`



## 0.1 First System Design


* tbd... rules how to deploy **BookLab** app in order to be used by client (what dir to copy and where - app dire, docs ref help dir...)

* tbd...cu ce faci [editarea textului markdown "clasic"](https://blog.miguelgrinberg.com/post/flask-pagedown-markdown-editor-extension-for-flask-wtf)

* @IMP#NOTE@230831piu_b made a test ref HTML form in markdown and what POST is sent un submit - see commented section at beg of `index.md`


### (#NOTE-next) 0.1.2 System Landscape first HLD
* ...DO NOT USE YET...




### 0.1.1 System Landscape drafts (#TODO-wip)

* tbd... the directory structure for new module: 2 dirs, UI and srv side. Just enum them and will mk doc `Sys_Landscape_DLD` for each

* tbd... directory for a new book will have (the template `bk_tmpl/`) name and generator cfg files "imported" from book name, or make a map file im doc_src route for `book.name ---> dir.name`

* tbd... a master index for user space (to keep all books) makes sense? NOT TOO MUCH because this is another sys job, for ex, min.edu LMS, sys al unei edituri sau cel al managerului meu  e se ocupa de afcerea mea de scris carti !

* tbd... update Landscape doc ref new objects created in `230830piu_e`

* wip...

* 230831piu_s renamed files of `bk_tmpl/docs/` to `my_book/` and let a note in corresponding `mkdocs.yml.new_name`

* 230831piu_c reorganized `doc_src/bk_tmpl/` directory as:
    * [x] its own `doc_src/` & `docs/` renamed inside `.readme.txt` hidden files to `readme_and_keep_me.txt` to have generation on their `docs/` at that book build (ie, its own `mkdocs build`)
    * [x] mv `bk_tmpl/index.md` file to `bk_tmpl/doc_src/`
    * [x] mv `bk_tmpl/print_page.md` file to `bk_tmpl/doc_src/`
    * [x] created `bk_tmpl/doc_src/CNAME` as empty file to be filled at NEWBook operation
    * [x] upd project `mkdocs.yml` to ignore `bk_*/` dirs at project build and let them as is (ie, will be user books and part of deployed apps as are they now)

* -#NOTE--- revw & publish up from here ---

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


