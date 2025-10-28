#!/usr/bin/bash
##
## script used to build the book from current directory
#@ Author: Petre Iordanescu (petre.iordanescu@gmail.com)
##

echo Start building Booklab master static site @ `date`
$(pdm venv activate)
cd `dirname $0`
cd ..

# build site
mkdocs build

# remove project root docs/ directory and copy the fresh built one
rm -r ../../docs/

# duplicate (as hard link) to project root docs/ which is used by GitHub to publish site on their servers
cp -lR docs/ ../../docs/
echo End of building Booklab master static site  @ `date`

deactivate
