#!/usr/bin/bash

#
# Used to generate booklab technical 
# (API-DLD) docomentation from all code files docstring(s)
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)
#

$(pdm venv activate)

# run mardown to build site
pydoc-markdown -p booklab >/tmp/810.05a-booklab_DLD_specs.md

# add [TOC] string to start of file
printf '# Booklab API\n\n[TOC]\n\n' 1<> /tmp/810.05a-booklab_DLD_specs.md

# move generated file to static site at its place
mv /tmp/810.05a-booklab_DLD_specs.md `dirname $0`/../doc_src/developer/810.05a-booklab_DLD_specs.md

deactivate



