#!/usr/bin/bash
##
## script used to build the book from current directory
#@ Author: Petre Iordanescu (petre.iordanescu@gmail.com)
##

echo Start building book @ `date`
$(pdm venv activate)
BOOK_DIR=`pwd`/`dirname $0`
cd $BOOK_DIR
echo Working directory is $(pwd)

mkdocs build &>./builds/$(date +%Y_%m_%d_%H_%M).stdout.txt

deactivate
echo End of building book @ `date`


