"""**db_init** module that initialize `booklabd` database (more JSON files)
This module is designed to initialize database objects `db_books` and `db_system`.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created: Sep.2025
"""

import pysondb
import os
from booklab import DATA_ROOT


def init_db() -> tuple[pysondb]:
    """Create db_books, db_system objects and return them as tuple
    
    Return:

        (db_books, db_system) tuple `pysondb` object
    """

    # ...tbd review and update code ...
    bks_catalog_file = os.path.join(DATA_ROOT, "books_catalog.json")
    db_books = pysondb.db.getDb(bks_catalog_file)
    print(f"*** booklabd.init_db created object {db_books=}")
    db_system = None  # ...#TODO tbd@250831
    #  the other db is app_info.json 4dbg... 
    # print(f"*** booklabd.__init__ imported 
    # {PACKAGE_ROOT=} {DATA_ROOT=} 
    # {CONF_ROOT=}")

    return (db_books, db_system)


