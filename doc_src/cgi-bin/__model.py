#!pyenv/bin/python3

#=============================================================
# Script to #TODO objective here...
#-----------------------------------------
# Author: Petre Iordanescu, (c) RENware Softwre Sytems
#=============================================================



import os
import cgi
import cgitb
import pysondb
import jinja2


my_name = __name__
my_crt_dir = os.getcwd()
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
# #NOTE read OS Environment variables
print ("<p>Environment</p><\br>");
for param in os.environ.keys(): # os.environ dictionary: keys() contains all ENV variables
   print ("<b>%20s</b>: %s<\br>" % (param, os.environ[param])) # in dictionary os.environ[key_...] contain the value of that ENV variable

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



