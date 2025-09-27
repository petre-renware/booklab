"""
Module that serve `booklabd` interface api-functions as HTTP routes

Important variables:

- `booklab.boolabd.api_app`: web application object (aka Flask.app)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

import os
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import request
from flask import request
from flask import abort
from werkzeug.urls import quote as url_quote
from booklab import EXT_PATH
from booklab import FULL_EXT_URL
from booklab import STATIC_SITE_ROOT
from booklab.booklabd import PROJECT_ROOT
from booklab.booklabd import api_app
from booklab.booklabd import db_books
from booklab.booklabd import db_system
from booklab.booklabd import pjroot_location
from booklab.booklib.getBook import getBook


# construct redirect url-path prefix (up to static site)
redirect_prefix = url_quote(
    FULL_EXT_URL +
    api_app.static_url_path
)
# construct prefix file-path for docs (static site) directory
docs_prefix = os.path.join(STATIC_SITE_ROOT)

# construct redirect url-path prefix (up to my_books to point then to /<book code>/docs/)
mybooks_redirect_prefix = url_quote(
    FULL_EXT_URL +
    "/preview/"
)


@api_app.route("/api/newb/")
def api_newb():
    """serve **New book (newb)** functionality.

    Query paraneters: none
    """
    book_code = request.args.get("code")
    ret_str = f"Page for <b>newb</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO  here should integrate wip static page
    return ret_str


@api_app.route("/api/bstatus/")
def api_bstatus(book_code = ...):
    """serve **Book status (bstatus)** functionality.

    Query paraneters: book code
    """
    ret_str = "nothing to say..."
    if book_code is ...:
        book_code = request.args.get("code")
    book_data = getBook(
        db_books,
        book_code
    )
    if not book_data:
        abort(404, description = "Book not found")
    else:
        ret_str = f"Book {book_code} data is <br>{book_data}"
    # render bstatus template and write it as html served from static site menu
    rendered_str = render_template(
        "bstatus/bstatus_template.html",
        book_data = book_data
    )
    file_to_write = os.path.join(
        docs_prefix,
        "bstatus/bstatus.html"
    )
    with open(file_to_write, "w") as file:
        file.write(rendered_str)
    redirect_path = url_quote(redirect_prefix + "/bstatus/bstatus.html")
    return redirect(redirect_path)


@api_app.route("/api/edtb/")
def api_edtb(book_code = ...):
    """serve **Book edit (edtb)** functionality.

    Query paraneters: book code
    """
    if book_code is ...:
        book_code = request.args.get("code")
    #TODO before getting book test if status.closed is true and if then return a 400 err "Book not editable"
    ret_str = f"Page for <b>edtb</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO  here should integrate wip static page
    return ret_str


@api_app.route("/api/orgm/")
def api_orgm(book_code = ...):
    """serve  **Book structure organization (orgm:** functionality.

    Query paraneters: book code
    """
    if book_code is ...:
        book_code = request.args.get("code")
    ret_str = f"Page for <b>orgm</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO  here should integrate wip static page
    return ret_str


@api_app.route("/api/prvb/")
def api_prvb(book_code = ...):
    """serve **Book preview (prvb)** functionality.

    Query paraneters: book code
    """
    if book_code is ...:
        book_code = request.args.get("code")
    book_data = getBook(
        db_books,
        book_code
    )
    if not book_data:
        abort(404, description = "Book not found")
    book_redirect_url = url_quote(
        mybooks_redirect_prefix +
        str(book_code) +
        "/docs/"
    )
    return redirect(book_redirect_url)


@api_app.route("/api/bbld/")
def api_bbld(book_code = ...):
    """serve **Book build (bbld)** functionality.

    Query paraneters: book code
    """
    if book_code is ...:
        book_code = request.args.get("code")
    ret_str = f"Page for <b>bbld</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO  here should integrate wip static page
    return ret_str


@api_app.route("/api/dplb/")
def api_dplb(book_code = ...):
    """serve **Book delivery (dplb)** functionality.

    Query paraneters: book code
    """
    if book_code is ...:
        book_code = request.args.get("code")
    ret_str = f"Page for <b>dplb</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO  here should integrate wip static page
    return ret_str


@api_app.route("/api/bcat/")
def api_bcat():
    """serve accessing **books catalog (bcat)** functionality.
    """
    bcat_records = None
    bcat_records = db_books.getAll()
    if not (type(bcat_records) == type(list())):
        bcat_records = list().append(bcat_records)  # make it list if is not (when just 1 record)
    # render bcat template and write it as html served from static site menus
    rendered_str = render_template(
        "bcat/bcat_template.html",
        bcat_data = bcat_records
    )
    file_to_write = os.path.join(
        docs_prefix,
        "bcat/bcat.html"
    )
    with open(file_to_write, "w") as file:
        file.write(rendered_str)
    redirect_path = url_quote(redirect_prefix + "/bcat/bcat.html")
    return redirect(redirect_path)


@api_app.route("/")
def index():
    """serve a cessing Home route.
    This is an alternate (but those expected from an end user) way to access static site main / home page.
    """
    redirect_path = url_quote(redirect_prefix + "/index.html")
    return redirect(redirect_path)



