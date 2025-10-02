import pysondb
from flask import Flask


class MyBook:
    """
    Class that manage my created books:

    - get a book data (JSON data)
    - get the HTML rendered my book to expose it over http
    - build a book (compile HTML static site)
    - build book definition (`mkdocs.yml`) replacing Jinja codes with soecific book values
    - get book navigation items

    Instance variables:

    `book_code`: str
    `flask_app`: Flask
    `db`: pysondb

    Author: Petre Iordanescu (petre.iordanescu@gmail.com)
    """


    def __init__(
        self,
        flask_app: Flask,
        db: pysondb,
        book_code: str
    ):
        """Init an instance of class MyBook
        """
        self.book_code = book_code
        self.flask_app = flask.app
        self.db = db
        ...  #TODO to be continued :..










'''
#TODO this code to become method of MyBook class
# code was already indented to "fit" a class property
#
    def getBook() -> dict | None:
        """Check for a given book code:

        * test if book code is not None
        * test if book code exists in database and is exactly 1 record
        * if both conditions return that record as List[Dict]
        * if not any condition return None

        Return:

        * `dict` with found record
        * `None` if any condition is not met
        """

        if not book_code or not isinstance(book_code, str):
            return None # exit because not satisfying basic requirements
        # check to see if record exists and if then just select first got
        bk_rec = None
        bk_rec = db.getBy({"code":book_code})
        if bk_rec and isinstance(bk_rec, list):
            return bk_rec[0]
        return None
'''


