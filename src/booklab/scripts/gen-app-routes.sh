#!/usr/bin/bash

# Bash script that generate a list with all
# `booklabd` registeres URI routes, their
# associated endpoints and accepted http modes
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)

$(pdm venv activate)

MY_DIR=`dirname $0`

TO_DIR=$MY_DIR/../doc_src/developer/
OFILE=810.05a-booklab_app_routes.md

echo Generating doc for booklabd exposed routes...

printf '# Booklab server routes' > $TO_DIR$OFILE
printf '\n\n' >> $TO_DIR$OFILE
printf 'Here you can find all active and available routes exposed by Booklab server (`booklabd`) component.' >> $TO_DIR$OFILE
printf '\n\n' >> $TO_DIR$OFILE
printf '``` console' >> $TO_DIR$OFILE
printf '\n' >> $TO_DIR$OFILE
flask routes >> $TO_DIR$OFILE
printf '\n' >> $TO_DIR$OFILE
printf '```' >> $TO_DIR$OFILE

echo End of routes doc generation.
deactivate
