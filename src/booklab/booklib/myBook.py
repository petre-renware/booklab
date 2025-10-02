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

    Author: Petre Iordanescu (petre.iordanescu@gmail.com)
    """

    book_code: str
    flask_app: Flask
    db: pysondb


    def __init__(
        self,
        flask_app: Flask,
        db: pysondb,
        book_code: str
    ):
        """Init an instance of class MyBook
        """
        self.book_code = book_code
        self.flask_app = flask_app
        self.db = db


    def getBook(self) -> dict | None:
        """Check for a given book code:

        - test if book code is not None
        - test if book code exists in database and is exactly 1 record
        - if both conditions return that record as Dict
        - if not any condition return None

        Return:

        - `dict` with found record
        - `None` if any condition is not met
        """

        if not self.book_code or not isinstance(self.book_code, str):
            return None # exit because not satisfying basic requirements
        # check to see if record exists and if then just select first got
        bk_rec = None
        bk_rec = self.db.getBy({"code": self.book_code})
        if bk_rec and isinstance(bk_rec, list):  # list means thare is more than 1 record
            return bk_rec[0]
        return None









