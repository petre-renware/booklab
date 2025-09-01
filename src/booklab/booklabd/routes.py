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
    """**api_bca** serveve route `/api/bcat`
    _NOTE:_ as exposed through nginx on this server the requestable route is `/bcat` (/api/ part is add by nginx)

    Author: Petre Iordanescu (petre.iordanescu@gmail.com)
    Last update: Sep.2025
    """

    # get list of book records ad list even 1rec
    bcat_records = db_books.getAll()
    if not (type(bcat_records) == type(list())):
        bcat_records = list().append(bcat_records)  # make it list if is not (when just 1 record)
    str_bcat_records = f"{bcat_records=}"  # 4dbg...

    #... #TODO render template as nxt line
    # Fkask_render_template_function_w.params (bcat_data=bcat_records)

    ret_str = "bcat records is:<br>" + str_bcat_records  # 4dbg
    return ret_str




