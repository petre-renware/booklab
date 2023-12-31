#!pyenv/bin/python3

#=============================================================
# Script to #TODO objective here...
#-----------------------------------------
# Author: Petre Iordanescu, (c) RENware Softwre Sytems
#=============================================================



import os
import cgi, cgitb
import pysondb
import jinja2


my_module_name = __name__ # the module name
my_name = __file__ # use `__file__` attribute which guarantees the full pth-and-name of current python file (ATTN if is in a library !)
my_crt_dir = os.getcwd() # normally this should be the site root directory (in production `docs/` & in dev `doc_src/`)
my_file_real_path = os.path.dirname(os.path.realpath(my_name))

# obtain book code from current directory name
splitted_my_real_dir = my_file_real_path.split(os.sep) # split directory path in its parts
book_directory_name = splitted_my_real_dir[-1] # get last list entry as being the book name where intend to obtain the book code (book dir name format: book_<code>)
book_database_code = book_directory_name[5:] # keep only characters after `book_`, sufix name of directory ((book dir name format: book_<code>))

cgitb.enable() # this activate displaying errs on HTML page and log them...



#
# #NOTE: HTTP header section for HTML content
print("Content-Type: text/html\n")
print()

""" #NOTE other HTTP header items

Content-type: String
* A MIME string defining the format of the file being returned. Example is Content-type:text/html

Expires: Date
* The date the information becomes invalid. It is used by the browser to decide when a page needs to be refreshed. A valid date string is in the format 01 Jan 1998 12:00:00 GMT.

Location: URL
* The URL that is returned instead of the URL requested. You can use this field to redirect a request to any file.

Last-modified: Date
* The date of last modification of the resource.

Content-length: N
* The length, in bytes, of the data being returned. The browser uses this value to report the estimated download time for a file.

Set-Cookie: String
* Set the cookie passed through the string
"""










#
# #NOTE construct database full absolute path file name and open it
dbs_file = os.path.join(my_crt_dir, "data/books_catalog.json")
bcat_dbs = pysondb.db.getDb(dbs_file)

bcat_records = bcat_dbs.getAll()
if not (type(bcat_records) == type(list())):
    bcat_records = list().append(bcat_records) # make it list if is not (possible case for 1 record)








#
# #NOTE Getting query parameters
#           - example for parameters `first_name` & `last_name`
#           - request URL: `.../cgi-bin/python_model.py?first_name=Malhar&last_name=Lathkar`
# Create instance of FieldStorage
query_data = cgi.FieldStorage()
# Get data from fields
first_name = query_data.getvalue('first_name')
last_name = query_data.getvalue('last_name')
print(f"<p><b>First name</b> = {first_name}</p>")
print(f"<p><b>Last name</b> = {last_name}</p>")








#
# #NOTE read OS Environment variables
print ("<h1>Environment</h1>");
for param in os.environ.keys(): # os.environ dictionary: keys() contains all ENV variables
   print ("<p><b>%20s</b>: %s</p>" % (param, os.environ[param])) # in dictionary os.environ[key_...] contain the value of that ENV variable

""" #NOTE OS all environment variables

CONTENT_TYPE
* The data type of the content. Used when the client is sending attached content to the server. For example, file upload.

CONTENT_LENGTH
* The length of the query information. It is available only for POST requests.

HTTP_COOKIE
* Returns the set cookies in the form of key & value pair.

HTTP_USER_AGENT
* The User-Agent request-header field contains information about the user agent originating the request. It is name of the web browser.

PATH_INFO
* The path for the CGI script.

QUERY_STRING
* The URL-encoded information that is sent with GET method request.

REMOTE_ADDR
* The IP address of the remote host making the request. This is useful logging or for authentication.

REMOTE_HOST
* The fully qualified name of the host making the request. If this information is not available, then REMOTE_ADDR can be used to get IR address.

REQUEST_METHOD
* The method used to make the request. The most common methods are GET and POST.

SCRIPT_FILENAME
* The full path to the CGI script.

SCRIPT_NAME
* The name of the CGI script.

SERVER_NAME
* The server's hostname or IP Address

SERVER_SOFTWARE
* The name and version of the software the server is running.
"""







#NOTE ------------


#NOTE ------------



