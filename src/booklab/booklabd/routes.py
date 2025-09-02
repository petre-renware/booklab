"""**routes** module desined to assure exposion of all `booklabd` interface as HTTP routes

Important variables:
    - `bkd.api_app` - web application object (aka Flask.app)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created: 250825
"""

from flask import render_template
from booklab.booklabd import api_app
from booklab.booklabd import db_books, db_system


@api_app.route("/api/bcat/")
def api_bcat():
    """**api_bcat** serve route `/api/bcat/`
    _NOTE:_ as exposed through nginx on this server the requestable route is `/bcat` (/api/ part is add by nginx)

    Author: Petre Iordanescu (petre.iordanescu@gmail.com)
    Last update: Sep.2025
    """

    # get list of book records ad list even 1rec
    bcat_records = db_books.getAll()
    if not (type(bcat_records) == type(list())):
        bcat_records = list().append(bcat_records)  # make it list if is not (when just 1 record)

    # render docs/bcat/bcat.html template
    ret_str = render_template(
        "bcat/bcat.html",
        bcat_data = bcat_records
    )
    return ret_str


@api_app.route('/api/docs/<any_path>')
def static_site(any_path: str):
    """**static_site** serve routes of static sote `/docs/...`

    Author: Petre Iordanescu (petre.iordanescu@gmail.com)
    Last update: Sep.2025
    """

    # redirect to static site
    ...

    return str(any_path)  #...4dbg purposes. tb drppped






