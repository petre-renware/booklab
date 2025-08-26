"""**routes** module desined to assure exposion of all `booklabd` interface as HTTP routes

Important variables:
    - `bkd.api_app` - web application object (aka Flask.app)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created: 250825
"""
from booklab.booklabd import api_app


# ...nxt dbg lin. drop it
print(f"*** booklabd.routes.py *** here is api_app variable {api_app}")


'''
@api_app.route("/api/bcat")
def api_bcat():
    """ ...wip...to be upd to my std (google std)
    """
    return "This is a test of /api/bcat/ route"
'''



