
""" booklabd - Booklab API server module

Main functionalities:
* operate & manage JSON database file
* provide necessary http API routes fir book functionalities that need write & dynamic (run-time) behavior

Architecture; HTTP WSGI

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

# general imports
import os
import pysondb
# booklab package imports
from booklab.booklabd.app_init import init_app
from booklab.booklib.db_init import init_db
from booklab import PROJECT_ROOT
from booklab import PACKAGE_ROOT
from booklab import CONF_ROOT
from booklab import DATA_ROOT
from booklab import STATIC_SITE_ROOT


pjroot_location = os.path.abspath(PACKAGE_ROOT)
static_dir = os.path.abspath("docs")
templates_dir = os.path.abspath("docs")
# create web application object
api_app = init_app(
    "booklabd",  # name set as this module, ie "booklabd"
    static_site_dir = static_dir,
    templates_dir = templates_dir,
    pjroot_location = pjroot_location
)
# save all project dir constants to api_app.config
api_app.config["STATIC_SITE_ROOT"] = STATIC_SITE_ROOT
api_app.config["DATA_ROOT"] = DATA_ROOT
api_app.config["CONF_ROOT"] = CONF_ROOT
api_app.config["PACKAGE_ROOT"] = PACKAGE_ROOT
api_app.config["PROJECT_ROOT"] = PROJECT_ROOT

# create database object by opening JSON files
db_books, db_system = init_db()

# get routes
import booklab.booklabd.routes




