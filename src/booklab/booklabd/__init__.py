
""" booklabd - Booklab API server module
Main functionalities:
- operate JSON database file
- provide necessary http routes

Architecture; HTTP REST
Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created; 21-Aug-2025
"""

# general imports
import os
import pysondb
# booklab package imports
from booklab.booklabd.app_init import init_app
from booklab.booklabd.db_init import init_db
from booklab import PROJECT_ROOT
from booklab import PACKAGE_ROOT
from booklab import CONF_ROOT
from booklab import DATA_ROOT
from booklab import STATIC_SITE_ROOT

pjroot_location = os.path.abspath(PROJECT_ROOT)
static_dir = os.path.abspath("docs")
templates_dir = os.path.abspath("docs")
#... #TODO create api_app.config["..."] for all directory constants
# create web application object
api_app = init_app(
    "booklabd",  # name set as this module, ie "booklabd"
    static_site_dir = static_dir,
    templates_dir = templates_dir,
    pjroot_location = pjroot_location
)


# create database object by opening JSON files
db_books, db_system = init_db()


# get routes
import booklab.booklabd.routes




