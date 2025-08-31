
""" booklabd - Booklab API server module
Main functionalities:
- operate JSON database file
- provide necessary http routes

Architecture; HTTP REST
Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created; 21-Aug-2025
"""

import os
from booklab.booklabd.app_init import init_app
from booklab import PACKAGE_ROOT
from booklab import CONF_ROOT
from booklab import DATA_ROOT


template_location = os.path.abspath("../../../docs")
# create web application object
api_app = init_app(
    __name__,
    static_site_dir = template_location
)
print(f"*** booklabd.__init__ *** Created api_app var as {api_app} with template dir to {template_location}")

# ...#TODO create database object by opening JSON files 
db_system = ...
db_books = ...
print(f"*** booklab.__init__ imported {PACKAGE_ROOT=} {DATA_ROOT=} {CONF_ROOT=}")


# get routes
import booklab.booklabd.routes





