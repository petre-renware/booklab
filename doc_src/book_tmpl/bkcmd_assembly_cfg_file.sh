#!/usr/bin/bash

#
# script to assembly mkdocs configuration file from parts
#
# - author: Petre Iordanescu, RENware Software Systems, petre.iordanescu@gmail.com
# - location: <a book directory>/book_config_parts/assembly_cfg_file.sh
#


# change directory in location where this script is located
cd "$(dirname "${BASH_SOURCE[0]}")/book_config_parts"

# ****************************** FROM HERE YOU ARE IN `book_tmpl/book_config_parts/` directory

# assembly files
echo "Start to assembly configuration file..."
rm tmp_config.yml
touch tmp_config.yml
cat cfg_01_head_yml_section.yml >> tmp_config.yml
cat cfg_02_nav_yml_section.yml >> tmp_config.yml
cat cfg_03_extension_yml_section.yml >> tmp_config.yml
cat cfg_04_dirs_yml_section.yml >> tmp_config.yml


# copy file to destination
echo "Move assembled file to destination..."
mv -f tmp_config.yml ../book_mkdocs.yml #TODO_#FIXME_just_simple_NOT_REQUIRED_intent aici faci un temporar (book_mkdocs.yml.tmp) care isi schimba numele dupa rendering


# give a message of finish & exit script
echo "Finished book configuration file assembly..."
cd ..

# ****************************** FROM HERE YOU ARE BACK IN `book_tmpl/` directory

# here you can call the python script to Jinja render the resulted YAML file
echo "Start book configuration file rendering"
./bkcmd_render_cfg_file.py
#-#TODO ... to be continued


#TODO_#FIXME_just_simple_NOT_REQUIRED_intent - daca ai facut fisier temporar (book_mkdocs.yml.tmp) ii schimbi numele inapoi la `book_mkdocs.yml`


