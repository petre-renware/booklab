"""**routes** module desined to assure exposion of all `booklabd` interface as HTTP routes

Important variables:
    - `booklab.boolabd.api_app` - web application object (aka Flask.app)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

import os
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import request
from flask import send_from_directory
# booklab imports
from booklab.booklabd import PROJECT_ROOT
from booklab.booklabd import api_app
from booklab.booklabd import db_books
from booklab.booklabd import db_system
from booklab.booklabd import pjroot_location


'''
@api_app.route("/")
def static_site():
    """**app_index** serve the application main / root index from static site (ie, `docs/index.html`)
    """
    src_dir = os.path.join(
        PROJECT_ROOT,
        "/docs/"
    )
    send_from_directory(src_dir, "index.html")
    return
'''


@api_app.route("/api/bcat/")
def api_bcat():
    """**api_bcat** serve route `/api/bcat/`

    _NOTE:_ as exposed through nginx on this server the requestable route is `/bcat` (/api/ part is add by nginx)
    """
    # get list of book records ad list even 1rec
    bcat_records = None
    bcat_records = db_books.getAll()
    if not (type(bcat_records) == type(list())):
        bcat_records = list().append(bcat_records)  # make it list if is not (when just 1 record)

    # render docs/bcat/bcat.html template
    rendered_str = render_template(
        "bcat/bcat_template.html",
        bcat_data = bcat_records
    )

    file_to_write = os.path.join(
        PROJECT_ROOT,
        "docs/bcat/bcat.html"
    )
    with open(file_to_write, "w") as file:
        file.write(rendered_str)
    #... #TODO set Flasx proxy middleware to eliminate need fir /booklab/ in route
    return redirect("/booklab/docs/bcat/bcat.html")


@api_app.route('/<path:any_path>')
def test(any_path: str = "") -> str:
    """**static_site** serve routes of static sote `/docs/...`

    This function serve Booklab static site from booklabd server. 
    This is provided to assure a right integration between pure _static site component_ which is the main entry in Booklab application and
    and _dynamic site (api) component_ which deserve those pages the need to write on server (usually database files) - non GET routes which are starting with `/api/...` explicitelly defined in this component (routes.py file).

    Return from this function vary depending on `any_path` value:
    - if "" or None then the static site will be addressed
    - for any other value that will be shown in a small HTML foe debugging purposrs
    """
    if any_path or any_path == "":
        s1 = f"Received path is: <b>{any_path}<b/> \n"
        s2 = ""  # kept fo show query params
        return str(s1 + s2)
    else:
        #... here will come code from route / then drop it
        #4dbg... return("in proceessing REQUEST FOR ROOT. Not implemented yet")
        src_dir = os.path.join(
            PROJECT_ROOT,
            "/docs/"
        )
        send_from_directory(src_dir, "index.html")
        return
    return









