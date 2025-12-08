"""
Module that serve `booklabd` interface api-functions as HTTP routes

Important variables:

- `booklab.boolabd.api_app`: web application object (aka Flask.app)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

import os
import w3lib.url

from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import request
from flask import request
from flask import abort
from werkzeug.urls import quote as url_quote

from booklab.__version__ import __version__
from booklab import EXT_PATH
from booklab import FULL_EXT_URL
from booklab import STATIC_SITE_ROOT

from booklab.booklabd import PROJECT_ROOT
from booklab.booklabd import api_app
from booklab.booklabd import db_books
from booklab.booklabd import db_system
from booklab.booklabd import pjroot_location

from booklab.my_books.books_manager import MyBooks


# construct redirect url-path prefix (up to static site)
redirect_prefix = url_quote(
    FULL_EXT_URL +
    api_app.static_url_path
)
# construct prefix file-path for docs (static site) directory
docs_prefix = os.path.join(STATIC_SITE_ROOT)


@api_app.route("/api/newb/")
def api_newb():
    """Serve _New book (newb)_ functionality.
    """
    book_code = request.args.get("code")
    ret_str = f"Page for <b>newb</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO here should integrate wip static page
    return ret_str


@api_app.route("/api/bstatus/")
def api_bstatus(book_code: str = ...):
    """Serve _Book status (bstatus)_ functionality.

    **Query parameters:** `code` for database `boook_code`
    """
    ret_str = "nothing to say..."
    if (book_code is ...) or (book_code is None):
        book_code = request.args.get("code", type = str)
        if not book_code:
            abort(404, description = "No Book specified.")
            return
    my_book = MyBooks(
        db = db_books,
        book_code = book_code
    )
    book_data = my_book.getBook()
    if not book_data:
        abort(404, description = "Book not found, does not physically exist.")
        return
    # create Jinja patams with JSON & YAML navigation section
    nav_json = my_book.getBookNav(format = "json")
    nav_yaml = my_book.getBookNav(format = "yaml")
    nav = {
        "fjson": f"{nav_json}",
        "fyaml": f"{nav_yaml}"
    }
    # render bstatus template and write it as html served from static site menu
    rendered_str = render_template(
        "bstatus/bstatus_template.html",
        book_data = book_data,
        nav = nav
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
def api_edtb(book_code: str = ...):
    """Serve _Book edit (edtb)_ functionality.

    **Query parameters:** `code` for database `boook_code`
    """
    if (book_code is ...) or (book_code is None):
        book_code = request.args.get("code", type = str)
        if not book_code:
            abort(404, description = "No Book specified.")
            return
    #TODO before getting book test if status.closed is true and if then return a 400 err "Book not editable"
    ret_str = f"Page for <b>edtb</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO here should integrate wip static page
    return ret_str


@api_app.route("/api/orgm/")
def api_orgm(book_code: str = ...):
    """Serve _Book structure & navigation organization (orgm)_ functionality.

    **Query parameters:** `code` for database `boook_code`
    """
    if (book_code is ...) or (book_code is None):
        book_code = request.args.get("code", type = str)
        if not book_code:
            abort(404, description = "No Book specified.")
            return
    ret_str = f"Page for <b>orgm</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO here should integrate wip static page
    return ret_str


@api_app.route("/api/prvb/")
def api_prvb(book_code: str = ...):
    """Serve _Book preview (prvb)_ functionality.

    **Query parameters:** `code` for database `boook_code`
    """
    if (book_code is ...) or (book_code is None):
        book_code = request.args.get("code", type = str)
        if not book_code:
            abort(404, description = "No Book specified.")
            return
    my_book = MyBooks(
        db = db_books,
        book_code = book_code
    )
    book_data = my_book.getBook()
    if not book_data:
        abort(404, description = "Book not found' Possible was not yet built.")
    book_redirect_url = my_book.getBookURL()
    return redirect(book_redirect_url)


@api_app.route("/api/bbld/")
def api_bbld(book_code: str = ...):
    """Serve _Book build (bbld)_ functionality.

    **Query parameters:** `code` for database `boook_code`
    """
    if (book_code is ...) or (book_code is None):
        book_code = request.args.get("code", type = str)
        if not book_code:
            abort(404, description = "No Book specified.")
            return
    ret_str = f"Page for <b>bbld</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO here should integrate wip static page
    ...
    #TODO update books_catalog ref `last build / update date`
    return ret_str


@api_app.route("/api/dplb/")
def api_dplb(book_code: str = ...):
    """Serve _Book delivery (dplb)_ functionality.

    **Query parameters:** `code` for database `boook_code`
    """
    if (book_code is ...) or (book_code is None):
        book_code = request.args.get("code", type = str)
        if not book_code:
            abort(404, description = "No Book specified.")
            return
    ret_str = f"Page for <b>dplb</b><br>"
    ret_str += f"Request for book with code <b>{book_code}</b><br>"
    #TODO here should integrate wip static page
    return ret_str


@api_app.route("/api/bcat/")
def api_bcat():
    """Serve _Books catalog (bcat)_ functionality.
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


@api_app.route("/api/version/")
def version():
    """ Return Booklab application version as pure plain raw text (no html).
    """
    response = make_response(__version__, 200)
    response.mimetype = "text/plain"
    return response


@api_app.route("/")
def index():
    """Serve accessing Home route.
    This route is an alternate option way (but usually the expected one from an end user) to access static site main / home page.
    """
    redirect_path = w3lib.url.canonicalize_url(
        url_quote(redirect_prefix + "/index.html")
    )
    return redirect(redirect_path)


@api_app.route("/api/about/")
def about():
    """Construct and request for "About Booklab" page.
    """
    rendered_str = render_template(
        "about/about_template.html",
        version = __version__
    )
    file_to_write = os.path.join(
        docs_prefix,
        "about/about.html"
    )
    with open(file_to_write, "w") as file:
        file.write(rendered_str)
    redirect_path = w3lib.url.canonicalize_url(
        url_quote(redirect_prefix + "/about/about.html")
    )
    return redirect(redirect_path)





