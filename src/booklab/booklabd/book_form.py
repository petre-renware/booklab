"""
Module for description of book data as fields (name, type, valudation rules) to be used in HTML forms.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

import os
import w3lib.url
from datetime import datetime
from pathlib import Path

''' #TODO chk what keep
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import request
from flask import abort
from werkzeug.urls import quote as url_quote

from booklab.__version__ import __version__
from booklab import EXT_PATH
from booklab import FULL_EXT_URL
from booklab import STATIC_SITE_ROOT
''' #TODO end of <what keep...>

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


#TODO ...code from here...

