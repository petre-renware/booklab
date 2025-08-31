"""**db_init** module that initialize `booklabd` database (more JSON files)
This module is designed to initialize database objects `db_books` and `db_system`.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created: Sep.2025
"""

import pysondb
import os


def init_db(
    app_name: str
) -> object:
    """Create Flask application object and return it

    Args:

        `app_name`: name of web application objwcr
        `static_site_dir`: directory used by Flask app to render Jinja templates

    Return:

        web application object
    """

bks_catalog_file = os.path.join(DATA_ROOT, 
"books_catalog.json") db_books = 
pysondb.db.getDb(bks_catalog_file) 
print(f"*** booklabd__init__ created object 
{db_books=}") db_system = ...
#  the other db is app_info.json 4dbg... 
# print(f"*** booklabd.__init__ imported 
# {PACKAGE_ROOT=} {DATA_ROOT=} 
# {CONF_ROOT=}")





