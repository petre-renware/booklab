""" booklabd - Booklab API server module
Main functionalities:
- operate JSON database file
- provide necessary http routes

Architecture; HTTP REST
Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created; 21-Aug-2025
"""

from booklab.booklabd.app_init import init_app


# create web application object
api_app = init_app(
    __name__
    # ... set templates and static directories
)
print(f"*** booklabd.__init__.py *** Created api_app var as {api_app}")

# ...#TODO create database object by opening JSON files 
db_system = ...
db_books = ...

# get routes
import booklab.booklabd.routes





