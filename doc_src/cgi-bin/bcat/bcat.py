#!/usr/bin/python3

#-----------------------------------------------------------
#
# Test script care va executa "whoami" pentru a testa daca masina este live si informatiile vitale ale acesteia
#
#-----------------------------------------------------------

import os
import pysondb

my_name = __name__
my_crt_dir = os.getcwd()


# HTTP header section
print("Content-Type: text/html\n")
print()



''' # #TODO plan

- `bcat.md` books catalog which need to be rewritten with a Jinja *`for loop`* to render all books

- remake `path(my_crt_dir, "data/books_catalog.json)` to be opened with `pysondb` (meaning "data" key) ATTN actual table loading in bcat.md will not work anymore so mk a copy for temporary use

- get all recs of (key `"data"` but psyondb already did...)

- get file `/bcat/bcat.html` and  Jinja render it

- print the file content (will be avlb in STDIN and get of http server)
'''


#FIXME drop this after use knowledge

print("<!doctype html><title>Hello</title><h2>BookLab - BCAT component</h2>")


print(f"<p>my code-name: {my_name}</p>")
print(f"<p>current directory: {my_crt_dir}</p>") #NOTE: DE RETINUT aici a afista dir crt ca ".../static_portal/" deci nu cgi-bin






