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


#-------------
# #NOTE: HTTP header section for HTML content
print("Content-Type: text/html\n")
print()

""" #NOTE other HTTP header items
------
Content-type: String
* A MIME string defining the format of the file being returned. Example is Content-type:text/html

------
Expires: Date
* The date the information becomes invalid. It is used by the browser to decide when a page needs to be refreshed. A valid date string is in the format 01 Jan 1998 12:00:00 GMT.

------
Location: URL
* The URL that is returned instead of the URL requested. You can use this field to redirect a request to any file.

------
Last-modified: Date
* The date of last modification of the resource.

------
Content-length: N
* The length, in bytes, of the data being returned. The browser uses this value to report the estimated download time for a file.

------
Set-Cookie: String
* Set the cookie passed through the string
"""




#NOTE ------------

"""
CONTENT_TYPE

The data type of the content. Used when the client is sending attached content to the server. For example, file upload.

2	
CONTENT_LENGTH

The length of the query information. It is available only for POST requests.

3	
HTTP_COOKIE

Returns the set cookies in the form of key & value pair.

4	
HTTP_USER_AGENT

The User-Agent request-header field contains information about the user agent originating the request. It is name of the web browser.

5	
PATH_INFO

The path for the CGI script.

6	
QUERY_STRING

The URL-encoded information that is sent with GET method request.

7	
REMOTE_ADDR

The IP address of the remote host making the request. This is useful logging or for authentication.

8	
REMOTE_HOST

The fully qualified name of the host making the request. If this information is not available, then REMOTE_ADDR can be used to get IR address.

9	
REQUEST_METHOD

The method used to make the request. The most common methods are GET and POST.

10	
SCRIPT_FILENAME

The full path to the CGI script.

11	
SCRIPT_NAME

The name of the CGI script.

12	
SERVER_NAME

The server's hostname or IP Address

13	
SERVER_SOFTWARE

The name and version of the software the server is running.
"""







#NOTE ------------


#NOTE ------------



