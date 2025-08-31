"""**routes** module desined to assure exposion of all `booklabd` interface as HTTP routes

Important variables:
    - `bkd.api_app` - web application object (aka Flask.app)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created: 250825
"""

from booklab.booklabd import api_app
from booklab.booklabd import db_books, db_system


# 4dbg... print(f"*** booklabd.routes.py *** here is api_app variable {api_app}")

@api_app.route("/api/bcat/")
def api_bcat():
    """ ...wip...
    CODE HERE IS A TEST. NEED TB UPDATED TO cgi-bin varsion, but first need create `db` objects
    to be upd to my std (google std)
    """
    return "This is a test of /api/bcat/ route"




