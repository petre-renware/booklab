#!/usr/bin/bash

#
# script to assembly mkdocs configuration file from parts
#


# change directory in location where this script is located (...)
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR


# assembly files
echo "Start to assembly configuration file..."
#TODO change directory in <book_dir>/book_config_parts/
rm tmp_config.yml
touch tmp_config.yml
cat cfg_01_head_yml_section.yml >> tmp_config.yml
cat cfg_02_nav_yml_section.yml >> tmp_config.yml
cat cfg_03_extension_yml_section.yml >> tmp_config.yml
cat cfg_04_dirs_yml_section.yml >> tmp_config.yml




# copy file to destination
echo "Copy assembled file to destination..."
#TODO_ATTN_to_name_of_book_config_file_(is_mkdocs.yml__???)
# cp tmp_config.yml ../mkdocs.yml



# give a message of finish & exit script
echo "Finished book configuration file assembly..."

