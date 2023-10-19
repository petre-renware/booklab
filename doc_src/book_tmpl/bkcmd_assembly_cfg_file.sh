#!/usr/bin/bash

#
# script to assembly mkdocs configuration file from parts
#
# - author: Petre Iordanescu, RENware Software Systems, petre.iordanescu@gmail.com
# - location: <a book directory>/book_config_parts/assembly_cfg_file.sh
#


# change directory in location where this script is located
cd "$(dirname "${BASH_SOURCE[0]}")/book_config_parts"

# ****************************** FROM HERE YOU ARE IN `book_<book_code>/book_config_parts/` directory

# assembly files
echo "Start to assembly configuration file..."
rm tmp_config.yml.tmpl
touch tmp_config.yml.tmpl
cat cfg_01_head_yml_section.yml >> tmp_config.yml.tmpl
cat cfg_02_nav_yml_section.yml >> tmp_config.yml.tmpl
cat cfg_03_extension_yml_section.yml >> tmp_config.yml.tmpl
cat cfg_04_dirs_yml_section.yml >> tmp_config.yml.tmpl


# copy file to destination
echo "Move assembled file to destination..."
mv -f tmp_config.yml.tmpl ../book_mkdocs.yml.tmpl


# give a message of finish & exit script
echo "Finished book configuration file assembly..."
cd ..

# ****************************** FROM HERE YOU ARE BACK IN `book_<book_code>/` directory

