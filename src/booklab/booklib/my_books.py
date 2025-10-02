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
    web_app: Flask
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
        self.web_app = flask_app
        self.db = db


    def getBook(self) -> dict | None:
        """Check for a given book code that is not None, exists in database and is exactly 1 record

        Return:

        - `dict` with found record or `None` if any of conditiona is not met
        """
        if not self.book_code or not isinstance(self.book_code, str):
            return None
        # check if record exists and is only one
        bk_rec = None
        bk_rec = self.db.getBy({"code": self.book_code})
        if bk_rec and isinstance(bk_rec, list):  # list means thare is more than 1 record
            return bk_rec[0]
        return None









