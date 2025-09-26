#!/usr/bin/bash
##
## script used to build the book from current directory
#@ Author: Petre Iordanescu (petre.iordanescu@gmail.com)
##

echo Start building book @ `date`
BOOK_DIR=`pwd`/`dirname $0`
cd $BOOK_DIR
echo Building directory  `pwd`
pdm run mkdocs build
echo End of building book @ `date`


