"""
Module that initialize `booklabd` database (more JSON files)

This module is designed to initialize database objects `db_books` and `db_system`.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

import pysondb
import os
from booklab import DATA_ROOT


def init_db() -> tuple[pysondb]:
    """Create db_books, db_system objects and return them as tuple

    Return:

        `(db_books, db_system)` tuple of pysondb object
    """
    file = os.path.join(DATA_ROOT, "books_catalog.json")
    db_books = pysondb.db.getDb(file)

    file = os.path.join(DATA_ROOT, "app_info.json")
    db_system = pysondb.db.getDb(file)

    return (db_books, db_system)


