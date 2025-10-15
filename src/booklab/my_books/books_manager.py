import os
import pysondb
import w3lib.url

from flask import Flask
from werkzeug.urls import quote as url_quote

from booklab import MY_BOOKS_ROOT
from booklab import EXT_PATH
from booklab import FULL_EXT_URL


class MyBook:
    """
    Class that manage end user books.

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
                str(FULL_EXT_URL) +
                str(MyBook._MY_BOOKS_URL_prefix) +
                str(self.book_code) +
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
        if bk_rec:
            if isinstance(bk_rec, list):
                # there is more than 1 record and keep only the first one
                bk_rec = bk_rec[0]
            elif isinstance(bk_rec, dict):
                # do nothing, record is in right format
                pass
            else:
                # unknown record type so exit with None
                return None
            # upd key "store_location"
            bk_rec["store_location"] = self.getBookPath()
            # when location exists appent `/`to ckear state it as directory otherwise let it unchanged
            if bk_rec["store_location"]:
               bk_rec["store_location"] += "/"
            # upd key "preview_url"
            bk_rec["preview_url"] = self.getBookURL()
            # return updayed record
            return bk_rec
        else:
            return None


    def getBookPath(self) -> str:
        """Get absolute path of current book root directory.
        """
        my_book_path = os.path.abspath(
            os.path.join(
                self.MY_BOOKS_PATH,
                self.book_code
            )
        )
        if os.path.isdir(my_book_path):
            return my_book_path
        else:
            return None


    def getBookURL(self) -> str:
        """Get preview URL (redirectable as is) for current book_code.
        """
        return self.MY_BOOK_URL


    def renderBookConfig(
        self,
        out_file: str = "mkdocs.yml"
    ) -> bool:
        """Render current book configuration file used in static site generation.
        """
        #TODO ...
        pass





