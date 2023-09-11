#!/usr/bin/python3

#-----------------------------------------------------------
#
# Test script care va executa "whoami" pentru a testa daca masina este live si informatiile vitale ale acesteia
#
#-----------------------------------------------------------

import os

# import urllib3 #TODO install it or use urllib which is built in

# import cgi #NOT this or next one? or both?
import cgitb 

# import pysondb #NOTE ck if can be used with a dbs as string...
#NOTE the JSON file is obtained by mk a request to `data/books_catalog.json` which return a response obtainable as resp.get_json() - see requests or urllib(3) module ref how to get json from response (or cosana)




my_name = __name__
my_crt_dir = os.getcwd()
cgitb.enable() # this activate displaying errs on HTML page and log them...


# HTTP header section
print("Content-Type: text/html\n")
print()



''' # #TODO plan

- `bcat.md` books catalog which need to be rewritten with a Jinja *`for loop`* to render all books

- remake `path(my_crt_dir, "data/books_catalog.json)` to be opened with `pysondb` (meaning "data" key) ATTN actual table loading in bcat.md will not work anymore so mk a copy for temporary use

- TRY THIS: get all recs of (key `"data"` but psyondb already did...)
- OR DO: request to `data/books_catalog.json`

- get file `/bcat/bcat.html` and  Jinja render it

- print the file content (will be avlb in STDIN and get of http server)

'''


#FIXME drop this after use knowledge

print("<!doctype html><p>BookLab BCAT component in loading...</p>")


print(f"<p>my code-name: {my_name}</p>")
print(f"<p>current directory: {my_crt_dir}</p>") #NOTE: DE RETINUT aici a afista dir crt ca ".../static_portal/" deci nu cgi-bin






