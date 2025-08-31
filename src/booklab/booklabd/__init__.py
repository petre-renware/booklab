
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
from booklab import PACKAGE_ROOT
from booklab import CONF_ROOT
from booklab import DATA_ROOT


template_location = os.path.abspath("../../../docs")
# create web application object
api_app = init_app(
    __name__,
    static_site_dir = template_location
)
# 4dbg... print(f"*** booklabd.__init__ Created {api_app=} with {template_location=}")

# create database object by opening JSON files
db_books, db_system = init_db()
# 4dbg... print(f"*** booklabd__init__ created objects {db_books=} and {db_system=}")


# get routes
import booklab.booklabd.routes




