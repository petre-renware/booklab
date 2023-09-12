#!pyenv/bin/python3
# #NOTE - clearly works - but create the `pyenv/` and up it to the git OR wvery time create it from `requirements.txt`

#-----------------------------------------------------------
#
# Test script care va executa "whoami" pentru a testa daca masina este live si informatiile vitale ale acesteia
#
#-----------------------------------------------------------

import os

# import urllib3 #TODO install it or use urllib which is built in

# import cgi #NOT this or next one? or both?
import cgitb

import pysondb



my_name = __name__
my_crt_dir = os.getcwd()
cgitb.enable() # this activate displaying errs on HTML page and log them...



# HTTP header section
print("Content-Type: text/html\n")
print()
print("<!doctype html><p>BookLab BCAT component in loading...</p>") #NOTE: this message could not appear for all HTTP servers; anyway will be replaced at final


#FIXME drop this after use knowledge
#print(f"<p>my code-name: {my_name}</p>")
print(f"<p>current directory: {my_crt_dir}</p>") #NOTE: DE RETINUT aici a afista dir crt ca ".../static_portal/" deci nu cgi-bin





''' # #TODO plan

- `bcat.md` books catalog which need to be rewritten with a Jinja *`for loop`* to render all books
- (DONE) remake `path(my_crt_dir, "data/books_catalog.json)` to be opened with `pysondb` (meaning "data" key) ATTN actual table loading in bcat.md will not work anymore so mk a copy for temporary use
- (DONE) get all recs of (key `"data"` but psyondb already did...)
- get file `/bcat/bcat.html` and  Jinja render it
- print the file content (will be avlb in STDIN and get of http server)

'''

# construct database full absolute path file name and open it
dbs_file = os.path.join(my_crt_dir, "data/books_catalog.json")
print(f"<p>--- database to open {dbs_file} </p>")
bcat_dbs = pysondb.db.getDb(dbs_file)
print(f"<p>---Data base opened. Here the JSON information: </p>")

bcat_records = bcat_dbs.getAll()
print(f"<p>{bcat_records} </p>") #FIXME this is a test printe all records







