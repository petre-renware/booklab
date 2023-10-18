#!pyenv/bin/python3

#=============================================================
# Script to render `book_mkdocs.yml` file
#   - this code SHOULD BE CALLED from HTTP server <wwww_root>
#       #NOTE this requirement reason: to guarantee right Python interpretor usage and because <www_root> is the only directory guranteed by any HTTP server)
#   - this code is NOT DESIGNED TO BE CALLED directly by http request
#-----------------------------------------
# Author: Petre Iordanescu, (c) RENware Softwre Sytems
#=============================================================


import os
import pysondb
import jinja2


my_name = __file__ # use `__file__` attribute which guarantees the full pth-and-name of current python file (ATTN if is in a library !)
my_crt_dir = os.getcwd() # normally this should be the site root directory (in production `docs/` & in dev `doc_src/`)
my_file_real_path = os.path.dirname(os.path.realpath(my_name))


# obtain book code from current directory name
splitted_my_real_dir = my_file_real_path.split(os.sep) # split directory path in its parts
book_directory_name = splitted_my_real_dir[-1] # get last list entry as being the book name where intend to obtain the book code (book dir name format: book_<code>)
book_database_code = book_directory_name[5:] # keep only characters after `book_`, sufix name of directory ((book dir name format: book_<code>))


# print(f"MY_REAL_DIR: {my_file_real_path}") #FIXME drop me - debug purpose
# print(f"MY_NAME: {my_name}") #FIXME drop me - debug purpose
# print(f"SPLITED PATH: {splitted_my_real_dir}") #FIXME drop me - debug purpose
# print(f"BOOK NAME: {book_directory_name}") #FIXME drop me - debug purpose
print(f"BOOK CODE: {book_database_code}") #FIXME drop me - debug purpose


# construct database full absolute path file name and open it
dbs_file = os.path.join(my_crt_dir, "data/books_catalog.json")
dbs_con = pysondb.db.getDb(dbs_file)
print(f"DBS CONNECTION: {dbs_con}") #FIXME drop me - debug purpose


# to get from JSON only the record you want:
search_criteria = dict(code = book_database_code)
bcat_records = dbs_con.getByQuery(search_criteria) # will return a list with all recorsd but allways keep only the first one as `code` key is UNIQUE
if not (type(bcat_records) == type(list())):
    bcat_records = list().append(bcat_records) # make it list if is not (possible case for 1 record)
if len(bcat_records) < 1: # if no records found then this ERROR is because somebody manually-edited the JSON dbs or changed the book directory name
    print(f"***ERROR (module bkcmd_render_cfg_file.py) no record found for key={book_database_code}. This ERROR could happen because somebody manually-edited the JSON dbs or changed the book directory name")
    exit(1)
bcat_records = bcat_records[0] # keep only the first one as `code` key is UNIQUE
print(f"QUERY RESULT: {bcat_records}") #FIXME drop me - debug purpose






#TODO - continue from here...
'''
templates_root = os.path.join(my_file_real_path, "") # here is the file that need to be renderend (book_mkdocs.yml)
with open(os.path.join(templates_root + "book_mkdocs.yml")) as f: # read file and load its content as template
    c = f.read()
bcat_jinja_tmpl = jinja2.Template(c) # load read file content as template
content = bcat_jinja_tmpl.render(bcat_data=bcat_records)
#FIXME here need to save back the rendered string (`content`) in the same file as the read one, so
#FIXME_CHANGE_WR_FILE_BACK_INSTEAD_PRINT ... write(content) --> `book_mkdocs.yml`
#FIXME_replace_with...write(content) --> `book_mkdocs.yml`... print(content)

'''

