""" booklabd - Booklab API server module
Main functionalities:
- operate JSON database file
- provide necessary http routes

Architecture; HTTP REST
Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created; 21-Aug-2025
"""

from booklab.booklabd.app_init import init_app
import os


template_location = os.path.abspath("../../../docs")
# create web application object
api_app = init_app(
    __name__,
    template_dir = template_location
    # ... set static directories
)
print(f"*** booklabd.__init__.py *** Created api_app var as {api_app} with template dir to {template_location}")

# ...#TODO create database object by opening JSON files 
db_system = ...
db_books = ...

# get routes
import booklab.booklabd.routes





