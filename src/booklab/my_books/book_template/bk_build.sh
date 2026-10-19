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


OUT_FILENAME=$(date +%Y%m%dh%H%M)

mkdocs build &>./builds/$OUT_FILENAME.out.txt
exit_code=$?

echo mkdocs finished with code $exit_code
echo $exit_code >./builds/$OUT_FILENAME.excode.txt
# create a tar archive with generated book (docs/)
if [ $exit_code -eq 0 ]; then
  tar -cvf ./builds/$OUT_FILENAME.site.tar ./docs/
fi

#TODO call url /booklab/finish ?code=<book-code>
# ...


deactivate
echo End of building book @ `date`

exit $exit_code
