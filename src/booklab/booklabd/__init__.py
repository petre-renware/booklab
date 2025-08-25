""" booklabd - Booklab API server module
Main functionalities:
- operate JSON database file
- provide necessary http routes

Architecture; HTTP REST
Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created; 21-Aug-2025
"""


from app_init import init_app

# global api_app




api_app = init_app(
    __name__
)
print(f"booklabd.__init__.py: Created api_app var as {api_app}")

import routes





