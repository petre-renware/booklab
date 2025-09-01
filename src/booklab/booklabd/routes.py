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


    # code extracted from cgi-bin version
    bcat_records = db_books.getAll()
    if not (type(bcat_records) == type(list())):
        bcat_records = list().append(bcat_records)  # make it list if is not (when just 1 record)
    print(f"{bcat_records=}")  # 4dbg...
    '''
    # here was read "bcat/bcat.html"
    #   to create Jina template instance
    #   then render it
    content = Fkask_render_template_function_w.params (bcat_data=bcat_records)
    print(content)
    '''


    return "This is a test of /api/bcat/ route"




