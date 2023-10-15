#!pyenv/bin/python3

#=============================================================
# Script to render `book_mkdocs.yml` file
#   - this code is normally called from assembling script (bkcmd_assembly_cfg_file.sh)
#   - this code is NOT DESIGNED TO BE CALLED directly by http request
#-----------------------------------------
# Author: Petre Iordanescu, (c) RENware Softwre Sytems
#=============================================================



import os
import pysondb
import jinja2


my_name = __name__
my_crt_dir = os.getcwd() # normally this should be the site root directory (in production `docs/` & in dev `doc_src/`)
cgitb.enable() # this activate displaying errs on HTML page and log them...

print(f"DIRECTOR: {my_crt_dir}") #FIXME drop me - debug purpose

'''

# construct database full absolute path file name and open it
dbs_file = os.path.join(my_crt_dir, "data/books_catalog.json")
bcat_dbs = pysondb.db.getDb(dbs_file)

bcat_records = bcat_dbs.getAll()
if not (type(bcat_records) == type(list())):
    bcat_records = list().append(bcat_records) # make it list if is not (possible case for 1 record)

templates_root = os.path.join(my_crt_dir, "")
with open(os.path.join(templates_root + "bcat/bcat.html")) as f: # read file and load its content as template
    c = f.read()
bcat_tmpl = jinja2.Template(c) # load read file content as template
content = bcat_tmpl.render(bcat_data=bcat_records)
print(content)


'''

