#!/usr/bin/bash
##
## script used to build the book from current directory
#@ Author: Petre Iordanescu (petre.iordanescu@gmail.com)
##


echo Start building book

pdm run mkdocs build

echo End of building book


