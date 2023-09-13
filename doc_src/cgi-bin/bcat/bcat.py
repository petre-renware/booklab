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
print("<!doctype html><p>BookLab BCAT component in loading...</p>") #FIXME: this message is for debbuging; anyway will be replaced at final


#FIXME drop this after use knowledge
#print(f"<p>my code-name: {my_name}</p>")
print(f"<p>current directory: {my_crt_dir}</p>") #NOTE: DE RETINUT aici a afista dir crt ca ".../static_portal/" deci nu cgi-bin





''' # #TODO plan **** WORKS PERFECTLY - 10xAva - GO AHEAD ...

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
if not (type(bcat_records) == type(list())):
  bcat_records = list().append(bcat_records) # make it list if is not (possible case for 1 record)
bcat_data = bcat_records # this variable should be send in Jinja rendering process . NOT NEEDED but will be assigned to in calling render function. JUST TO REMEMBER...
#TODO ...nxt actions...
#TODO here to render as Jinja template. WHO: `docs/bcat/bcat.html`
#TODO and just print it after (to go to STDOUT)

''' #NOTE retrieved data from JSON file
  [
      {
          'id': 0, 'code': 'BCAT',
          'short_desc': 'bk_tmpl', 
          'description': 'Sablonul implicit pentru o carte noua', 
          'created_date': '2023-08-01', 
          'created_by': 'system', 
          'notes': 'Inregistrare obligatorie de la instalare sistem. Non editabila.'
      }
  ]
'''




