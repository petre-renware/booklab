"""**routes** module desined to assure exposion of all `booklabd` interface as HTTP routes

Important variables:
    - `bkd.api_app` - web application object (aka Flask.app)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
# booklab imports
from booklab.booklabd import api_app
from booklab.booklabd import db_books, db_system


@api_app.route("/api/bcat/")
def api_bcat():
    """**api_bcat** serve route `/api/bcat/`
    _NOTE:_ as exposed through nginx on this server the requestable route is `/bcat` (/api/ part is add by nginx)
    """

    # get list of book records ad list even 1rec
    bcat_records = db_books.getAll()
    if not (type(bcat_records) == type(list())):
        bcat_records = list().append(bcat_records)  # make it list if is not (when just 1 record)

    # render docs/bcat/bcat.html template
    rendered_str = render_template(
        "bcat/bcat.html",
        bcat_data = bcat_records
    )

    ret_str = make_response(rendered_str)
    ret_str.location = "/docs/bcat/"
    ret_str.status = 200

    #TODO ...tbd here need to prepare a response object and return it
    # ... which will asure a return like CGI old varian which was functional integrated with static site
    # ... need to modify response created by render_template to ret like CGI did. See:
    # `https://flask.palletsprojects.com/en/stable/quickstart/#about-responses `

    return ret_str


@api_app.route('/<path:any_path>')
def static_site(any_path: str):
    """**static_site** serve routes of static sote `/docs/...`
    This function serve Booklab static site from booklabd server. 
    This is provided to assure a right integration between pure _static site component_ which is the main entry in Booklab application and
    and _dynamic site (api) component_ which deserve those pages the need to write on server (usually database files) - non GET routes which are starting with `/api/...` explicitelly defined in this component (routes.py file).

    Sometimes, when a page is called after `/api/xxz/` route returning, the string "api/" will remain in route so it will _need to be remived_ before sending file type of return.

    Return from this function is done by `send_from_directory` Flask function which will do a "return like from static site" with right renderind on client browser.
    """

    # ..;tbd filter "any_path" of string "api/"
    ...

    # .;;tbd prep send_from_directory parametrs
    ...

    return str(any_path)  #...4dbg purposes. tb drppped
    # return send_from_directory(f'templates/bridge/{p2

    # ...tbd see TODO from /api/bcat/ route






