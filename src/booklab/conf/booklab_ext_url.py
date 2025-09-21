"""
This Python file contains external access URL information.
By external access is understood all URL parts necessary to expose Booklab application:

* EXT_SERVER - the external exposed server name and port if diffrent than standard default (80 or 443) (example: "booklab.mydomain.ro")
* EXT_PATH - the external exposed URL of configured start locations through a LAN main proxy (example: "/booklab/" for a complete external URL like http://booklab.mydomain.ro:5002/booklab/)

_NOTE: all information are of string type_

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from urllib.parse import urljoin


EXT_SERVER = ""  # blank preserve source
EXT_PATH = "/booklab/"

FULL_EXT_URL = urljoin(EXT_SERVER, EXT_PATH)
#4dbg... print(f"{FULL_EXT_URL=}")



