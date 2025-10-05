import pysondb
import w3lib.url
from flask import Flask
from werkzeug.urls import quote as url_quote
from booklab import MY_BOOKS_ROOT
from booklab import EXT_PATH
from booklab import FULL_EXT_URL


class MyBook:
    """
    Class that manage my created books:

    - get a book data (JSON data)
    - get the HTML rendered my book to expose it over http
    - build a book (compile HTML static site)
    - build book definition (`mkdocs.yml`) replacing Jinja codes with soecific book values
    - get book navigation items

    **Important properties:**

    - `MY_BOOK_URL`: url to redirect to access book static site (preview book)
    - `MY_BOOK_PATH`: file-parh to book root location

    Author: Petre Iordanescu (petre.iordanescu@gmail.com)
    """
    _MY_BOOKS_URL_prefix = "/my-books/"
    MY_BOOK_URL: str
    MY_BOOKS_PATH: str
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
        MyBook.MY_BOOKS_PATH = MY_BOOKS_ROOT
        self.book_code = book_code
        self.web_app = flask_app
        self.db = db
        self.MY_BOOK_URL = w3lib.url.canonicalize_url(
            url_quote(
                FULL_EXT_URL +
                MyBook._MY_BOOKS_URL_prefix +
                self.book_code +
                "/docs/"
            )
        )


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


    def getBookPath(self) -> str:
        """Get absolute path of current book root directory.
        """
        pass


    def getBookPreviewURL(self) -> str:
        """Get preview URL (redirectable as is) for current book_code.
        """
        pass


    def renderBookConfig(
        self,
        out_file: str = "mkdocs.yml"
    ) -> bool:
        """Render current book configuration file used in static site generation.
        """
        pass





