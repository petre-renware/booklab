#!/usr/bin/bash
##
## script used to build the book from current directory
#@ Author: Petre Iordanescu (petre.iordanescu@gmail.com)
##

echo Start building book @ `date`
$(pdm venv activate)
BOOK_DIR=`pwd`/`dirname $0`
cd $BOOK_DIR
BOOK_CODE=$(basename `pwd`)

echo Working directory is $(pwd)
echo Book code is: $BOOK_CODE

# variant.w.filename.as.datetime
#OUT_FILENAME=$(date +%Y%m%dh%H%M)
# variant.w.filename.as.book_code
OUT_FILENAME=$BOOK_CODE

mkdocs build &>./builds/$OUT_FILENAME.out.txt
exit_code=$?

# notify some info at console
echo mkdocs finished with code $exit_code
echo $exit_code >./builds/$OUT_FILENAME.excode.txt

# create a tar archive with generated book (docs/)
if [ $exit_code -eq 0 ]; then
  tar -cvf ./builds/$OUT_FILENAME.site.tar ./docs/
fi

# call calpback url
curl -G http://localhost:5002/api/bbld/finbld/ -d code=$BOOK_CODE -d exit_code=$exit_code


deactivate
echo End of building book @ `date`

exit $exit_code
