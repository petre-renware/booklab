#!/usr/bin/bash
##
## script used to build the book from current directory
#@ Author: Petre Iordanescu (petre.iordanescu@gmail.com)
##

echo Start building Booklab master static site @ `date`
# ATTN: script is located in .../booklab/scripts/ dir
cd `dirname $0`
cd ..

pdm run mkdocs build

# remove project root docs/ directory and copy the fresh built one
rm -r ../../docs/


cp -lR docs/ ../../docs/
echo End of building Booklab master static site  @ `date`


