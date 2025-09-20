"""
This Python file contains external access URL information.
By external access is understood all URL parts necessary to expose Booklab application:

* EXT_SERVER - the external exposed server name (example: "booklab.mydomain.ro")
* EXT_PORT - the external exposed server port; defaults to "80" if unspecified (example: "5002")
* EXT_PATH - the external exposed URL configured start locations through a LAN main proxy (example: "/booklab/" for a complete external URL like http://booklab.mydomain.ro:5002/booklab/)

_NOTE: all information are of string type_

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

EXT_SERVER = ""  # blank preserve source
EXT_PORT = ""  # blank preserve source
EXT_PATH = "booklab/"


