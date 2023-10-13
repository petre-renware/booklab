#!/usr/bin/bash

#
# script to assembly mkdocs configuration file from parts
#
# - author: Petre Iordanescu, RENware Software Systems, petre.iordanescu@gmail.com
# - location: <a book directory>/book_config_parts/assembly_cfg_file.sh
#


# change directory in location where this script is located
cd "$(dirname "${BASH_SOURCE[0]}")/book_config_parts"


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
mv -f tmp_config.yml ../book_mkdocs.yml


# give a message of finish & exit script
echo "Finished book configuration file assembly..."


# #TODO here you can call the python script to Jinja render the resulted YAML file
cd .. # do not call rendering Python script before changing directory one level up




