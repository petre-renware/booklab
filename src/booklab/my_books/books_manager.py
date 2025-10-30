import os
import pysondb
import w3lib.url
import json
import pylibyaml
import yaml  # mandatory to import after pylibyank
import rich
from rich import print as rprint
from pathlib import Path

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

    author: Petre Iordanescu (petre.iordanescu@gmail.com)
    """
    _MY_BOOKS_URL_prefix = "/my-books/"
    MY_BOOK_URL: str
    MY_BOOKS_PATH: str
    book_path: str
    book_code: str
    web_app: Flask
    db_books_catalog: pysondb
    db_book_nav: pysondb

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
        self.db_books_catalog = db
        self.MY_BOOK_URL = w3lib.url.canonicalize_url(
            url_quote(
                str(FULL_EXT_URL) +
                str(MyBook._MY_BOOKS_URL_prefix) +
                str(self.book_code) +
                "/docs/"
            )
        )
        if (this_bk_path := self.getBookPath()):
            file_dbnav = os.path.join(
                this_bk_path,
                "book_navigation.json"
            )
            self.db_book_nav = pysondb.db.getDb(file_dbnav)
        else:
            self.db_book_nav = None


    def getBook(self) -> dict | None:
        """Check for a given book code that is not None, exists in database and is exactly 1 record.

        Return:

        - `dict` with found record or `None` if any of conditiona is not met
        """
        if not self.book_code or not isinstance(self.book_code, str):
            return None
        # check if record exists and is only one
        bk_rec = None
        bk_rec = self.db_books_catalog.getBy({"code": self.book_code})
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
            if self.db_book_nav:  # ck if nav definition exisys (as json data-file)
                nav_file = self.db_book_nav.filename
                bk_rec["nav_file_location"] = nav_file
            else:
                bk_rec["nav_file_location"] = None
            # return updayed record
            return bk_rec
        else:
            return None


    def getBookNav(
        self,
        format = None
    ) -> None | dict | str:
        """Get book navigation.

        Navigation info is retrieved from `book_navigation.json` data-file
        identified by `self.db_book_nav` pysondb handler.

        Return:

        - `python dict` using `format = "dict"` (default option)
        - `JSON str` using `format = "json"`
        - `YAML str` using `format = "yaml"`
        - `None` if not known format
        """
        if not self.db_book_nav:
            return None
        bk_nav_raw_data = self.db_book_nav.getAll()
        bk_nav_data = dict()
        bk_nav_data["nav"] = bk_nav_raw_data
        # check format param and return accordingly
        if not format or format is ...:
            format = "dict"  # default value if not specified or set as None
        if format == "dict":
            return bk_nav_data
        if format == "json":
            json_nav_data = json.dumps(
                bk_nav_data,
                indent = 2
            )
            json_nav_data = f"{json_nav_data}"
            return json_nav_data
        if format == "yaml":
            yaml_nav_data = yaml.safe_dump(
                bk_nav_data
            )
            yaml_nav_data = f"{yaml_nav_data}"
            return yaml_nav_data
        return None  # if get here its a bug due to logic error


    def wrBookNav(self) -> bool:
        """Write out file "book_navigation.yml"

        Return:

        - `True` if file was written
        - `False` if file was not written doesn't matter why (usual problem is source file)
        """
        if not self.db_book_nav:
            return False
        out_file = self.db_book_nav.filename
        out_file = out_file.replace(".json", ".yml")
        out_file = Path(out_file)
        WARNING_CONTENT = "# `nav` section AUTO GENERATED @run-time. DO NOT MODIFY it.\n"
        if not (yaml_content := self.getBookNav(format = "yaml")):
            return False
        yaml_content = WARNING_CONTENT + yaml_content
        try:
            out_file.write_text(yaml_content)
        except:
            return False
        return True


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
        start_from: int = 1
    ) -> tuple:
        """Render current book configuration file.
        Produce a `mkdocs.yml` file as being the configuration file to build the book.
        File is writen in book root directory.

        Arguments:

        - `start_from` the step where to START from. 
          Valid values are `int` in range `[1, 3]`. 
          A value _out of valid range_ is interpreted as `1` (execute all steps).

        Return:

        - `(exit_code, stdout + stderr)`
        """
        if not self.db_book_nav:
            # if book nav does not exists force exit
            return (False, "EROARE: Cartea nu are navigarea definita (fisier JSON)")
        if (start_from is None)\
           or (type(start_from) is not int)\
           or (start_from < 1)\
           or (start_from > 3)\
        :
            start_from = 1
        s1_exec = False
        s2_exec = False
        s3_exec = False
        rslt_s1 = ""
        rslt_s2 = ""
        rslt_s3 = ""
        ## 1. create YAML for nav section
        if start_from <= 1:
            exit_code_s1 = self.wrBookNav()
            rslt_s1 = "executat" if exit_code_s1 else "NE-executat"
            rslt_s1 = f"\nCreare fisier YAML din JSON: {rslt_s1}"
            if not exit_code_s1:
                return (
                    False,
                    rslt_s1
                )
            s1_exec = True
        ## 2. render mkdocs_template.yml
        if start_from <= 2:
            #TODO ...
            exit_code_s2 = ...
            rslt_s2 = ... # + stdout + stderr of prev run)
            rslt_s2 = f"\nRandare Jinja: {rslt_s2}"
            if not exit_code_s2:
                return (
                    False,
                    rslt_s1 + rslt_s2
                )
            s2_exec = True
        ## 3. run build.sh & keep exit_code
        if start_from <= 3:
            #TODO ... exit_code_s3 = os..:run...
            exit_code_s3 = ...
            rslt_s3 = ... # self._render_config_stack.append(stdout + stderr of prev ruv)
            rslt_s3 = f"\nRulare build carte cu mkdocs: {rslt_s3}"
            if not exit_code_s3:
                return (
                    False,
                    rslt_s1 + rslt_s2 + rslt_s3
                )
            s3_exec = True
        ## 4. everithing was ok here so return True and all result outputs
        if s1_exec or s2_exec or s3_exec:
            return (
                True,
                rslt_s1 + rslt_s2 + rslt_s3
            )




