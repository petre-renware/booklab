"""**routes** module desined to assure exposion of all `booklabd` interface as HTTP routes

Important variables:
    - `bkd.api_app` - web application object (aka Flask.app)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

import os
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
# booklab imports
from booklab.booklabd import api_app
from booklab.booklabd import db_books
from booklab.booklabd import db_system
from booklab.booklabd import pjroot_location


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
        "bcat/bcat_template.html",
        bcat_data = bcat_records
    )
    # #TODO write rendered_str to file
    # .../docs/bcat/bcat.html
    file_to_write = os.path.abspath(
        os.path.join(pjroot_location, "docs/bcat/bcat.html")
    )
    with open(file_to_write, "w") as file:
        file.write(rendered_str)
    return redirect("/docs/bcat/bcat.html")  # ? use /booklab/ ???


@api_app.route('/<path:any_path>')
def static_site(any_path: str):
    """**static_site** serve routes of static sote `/docs/...`
    This function serve Booklab static site from booklabd server. 
    This is provided to assure a right integration between pure _static site component_ which is the main entry in Booklab application and
    and _dynamic site (api) component_ which deserve those pages the need to write on server (usually database files) - non GET routes which are starting with `/api/...` explicitelly defined in this component (routes.py file).

    Sometimes, when a page is called after `/api/xxz/` route returning, the string "api/" will remain in route so it will _need to be remived_ before sending file type of return.

    Return from this function is done by `send_from_directory` Flask function which will do a "return like from static site" with right renderind on client browser.
    """

    s1 = f"Received path is: {any_path} \n"
    try:
        s2 = "with.param.static" + url_for("static")
    except:
        s2 = "with.param.docs" + url_for("docs")
    s2 = f"URL for static is: {s2}"
    return str(s1 + s2)





