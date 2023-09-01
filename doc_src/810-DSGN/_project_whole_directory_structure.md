﻿# Whole project directory structure

Leaving from `<PROJECT ROOT>`


``` tree

PROJECT_ROOT
|   requirements.txt
|       
+---.env		# specific Python environment files and directories
|       
+---booklab_app
|       .gitkeep
|       
+---docs
|   |   .gitkeep
|   |   404.html
|   |   bkcmd_new_book.py
|   |   CNAME
|   |   index.html
|   |   print_page.html
|   |   requirements.txt.ck_if_need_it
|   |   sitemap.xml
|   |   sitemap.xml.gz
|   |   wip.html
|   |   
|   +---810-DSGN
|   |       810.02-System_Landscape.html
|   |       
|   +---assets	# specific CSS, JS, image, ... files and directories (for site rendering)
|   |           
|   +---bk_tmpl
|   |   |   bkcmd_gen_final_book.py
|   |   |   bkcmd_start_book_preview.py
|   |   |   bk_CNAME_domain
|   |   |   mkdocs.yml.new_name
|   |   |   
|   |   +---book_config_parts
|   |   |       cfg_01_head_yml_section.yml
|   |   |       cfg_02_nav_yml_section.yml
|   |   |       cfg_03_dirs_yml_section.yml
|   |   |       cfg_03_extension_yml_section.yml
|   |   |       readme.txt
|   |   |       
|   |   +---my_book
|   |   |       readme_and_keep_me.txt
|   |   |       
|   |   +---preview_book    # temp directory for previews & tests 
|   |   |       readme.txt
|   |   |       
|   |   \---raw_source_docs
|   |           CNAME
|   |           index.md.txt
|   |           print_page.md.txt
|   |           readme_and_keep_me.txt
|   |           
|   +---css		# `print-site` plug in extension PDF books generator
|   |       
|   +---help
|   |       130.02-Overview.html
|   |       880.30-ADMA_catalog.html
|   |       880.30-EUMA_catalog.html
|   |       
|   +---js		# `print-site` plug in extension PDF books generator
|   |       
|   +---pdfs
|   |   +---810-DSGN
|   |   |   \---810.02-System_Landscape.html
|   |   |           810.02-System_Landscape.pdf
|   |   |           
|   |   +---help
|   |   |   +---130.02-Overview.html
|   |   |   |       130.02-Overview.pdf
|   |   |   |       
|   |   |   +---880.30-ADMA_catalog.html
|   |   |   |       880.30-ADMA_catalog.pdf
|   |   |   |       
|   |   |   \---880.30-EUMA_catalog.html
|   |   |           880.30-EUMA_catalog.pdf
|   |   |           
|   |   +---index.html
|   |   |       index.pdf
|   |   |       
|   |   +---print_page.html
|   |   |       print_page.pdf
|   |   |       
|   |   \---wip.html
|   |           wip.pdf
|   |           
|   +---pictures
|   |       booklab_logo.png
|   |       REN_stamp_logo_transparent.fodg
|   |       REN_stamp_logo_transparent.png
|   |       REN_stamp_logo_transparent.svg
|   |       under_maintenance.png
|   |       
|   \---search		# sote seacrch index
|           
\---doc_src
    |   .gitkeep
    |   bkcmd_new_book.py
    |   CNAME
    |   index.md
    |   print_page.md
    |   requirements.txt.ck_if_need_it
    |   wip.md
    |   
    +---810-DSGN
    |       .gitkeep
    |       810.02-System_Landscape.md
    |       
    +---bk_tmpl
    |   |   .gitkeep
    |   |   bkcmd_gen_final_book.py
    |   |   bkcmd_start_book_preview.py
    |   |   bk_CNAME_domain
    |   |   mkdocs.yml.new_name
    |   |   
    |   +---book_config_parts
    |   |       .gitkeep
    |   |       cfg_01_head_yml_section.yml
    |   |       cfg_02_nav_yml_section.yml
    |   |       cfg_03_dirs_yml_section.yml
    |   |       cfg_03_extension_yml_section.yml
    |   |       readme.txt
    |   |       
    |   +---my_book
    |   |       .gitkeep
    |   |       readme_and_keep_me.txt
    |   |       
    |   +---preview_book
    |   |       .gitkeep
    |   |       readme.txt
    |   |       
    |   \---raw_source_docs
    |           CNAME
    |           index.md.txt
    |           print_page.md.txt
    |           readme_and_keep_me.txt
    |           
    +---help
    |       .gitkeep
    |       130.02-Overview.md
    |       880.30-ADMA_catalog.md
    |       880.30-EUMA_catalog.md
    |       
    \---pictures
            booklab_logo.png
            REN_stamp_logo_transparent.fodg
            REN_stamp_logo_transparent.png
            REN_stamp_logo_transparent.svg
            under_maintenance.png
           


```
