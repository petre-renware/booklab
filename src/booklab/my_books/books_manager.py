import os
import pysondb
import w3lib.url
import json
import pylibyaml
import yaml  # mandatory to import after pylibyank
import rich
from rich import print as rprint
from pathlib import Path
import jinja2 as j2  # see dtl nxt comment
# important objects from jinja package:
#    Environment
#    PackageLoader
#    select_autoescape


from flask import Flask
from werkzeug.urls import quote as url_quote

from booklab import MY_BOOKS_ROOT
from booklab import EXT_PATH
from booklab import FULL_EXT_URL


class MyBooks:
    """
    Class that manage end user books.

    **Mandatory requirements:**

    - any Jinja renderings will be made "from string" (ie, using
    Flask `render_from_string()` which is included) or by creating a local Jinja environment.

    author: Petre Iordanescu (petre.iordanescu@gmail.com)
    """

    MY_BOOKS_URL_prefix: str = (
        "/my-books/"  # URL prefix to add when accesing a book local (generated) site
    )
    MY_BOOK_URL: str = None  # instantiated book URL to local (generated) site
    MY_BOOKS_ROOT: str = (
        MY_BOOKS_ROOT  # confusing name ? just duplicate the global one in class namespace
    )
    book_code: str = None  # instanciated book code
    db_books_catalog: pysondb = None  # books catalog data controller
    db_book_nav: pysondb = None  # books navigation data controller
    jinja_env = None  # Jinja environment usable for my_books rendering needs


    def __init__(self, db: pysondb, book_code: str):
        """Init an instance of class MyBooks"""
        self.MY_BOOKS_ROOT = MY_BOOKS_ROOT  # confusing name ? just duplicate the global one in class namespace
        self.book_code = book_code
        self.db_books_catalog = db
        self.MY_BOOK_URL = w3lib.url.canonicalize_url(
            url_quote(
                str(FULL_EXT_URL)
                + str(MyBooks.MY_BOOKS_URL_prefix)
                + str(self.book_code)
                + "/docs/"
            )
        )
        if this_bk_path := self.getBookPath():
            file_dbnav = os.path.join(this_bk_path, "book_navigation.json")
            self.db_book_nav = pysondb.db.getDb(file_dbnav)
        else:
            self.db_book_nav = None
        self.jinja_env = j2.Environment(
            loader = j2.PackageLoader(
                package_name = "booklab.my_books",
                package_path = "."
            ),
            autoescape = j2.select_autoescape()
        )


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
            # when location exists append `/`to ckear state it as directory otherwise let it unchanged
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
        format: str = None
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
            json_nav_data = json.dumps(bk_nav_data, indent=2)
            json_nav_data = f"{json_nav_data}"
            return json_nav_data
        if format == "yaml":
            yaml_nav_data = yaml.safe_dump(bk_nav_data)
            yaml_nav_data = f"{yaml_nav_data}"
            return yaml_nav_data
        return None  # if get here its a bug due to logic error

    def wrBookNav(self) -> bool:
        """Write out file "book_navigation.yml"

        Return:

        - `True` if file was written
        - `False` if file was not written or cannot be read regardless why (usual problem is source file)
        """
        if not self.db_book_nav:
            return False
        out_file = self.db_book_nav.filename
        out_file = out_file.replace(".json", ".yml")
        out_file = Path(out_file)
        WARNING_CONTENT = (
            "# `nav` section AUTO GENERATED @run-time. DO NOT MODIFY it.\n"
        )
        if not (yaml_content := self.getBookNav(format="yaml")):
            return False
        yaml_content = WARNING_CONTENT + yaml_content
        try:  # write file
            out_file.write_text(yaml_content)
        except:
            return False
        try:  # test if file can be read
            with out_file.open("r") as f:
                _c = f.read()
            return True
        except:
            return False
        return True

    def getBookPath(self) -> str:
        """Get absolute path of current book root directory."""
        my_book_path = os.path.abspath(os.path.join(self.MY_BOOKS_ROOT, self.book_code))
        if os.path.isdir(my_book_path):
            return my_book_path
        else:
            return None

    def getBookURL(self) -> str:
        """Get preview URL (redirectable as is) for current book_code."""
        return self.MY_BOOK_URL

    def renderBookConfig(self) -> tuple:
        """Render current book configuration file.
        Produce file `mkdocs.yml` as being the configuration file to build the book.
        File is writen in book root directory.

        Return:

        - `(exit_code, stdout + stderr)`
        """
        if not self.db_book_nav:
            # if book nav does not exists force exit
            return (False, "EROARE: Cartea nu are navigarea definita (fisier JSON)")
        rslt_s1 = ""
        rslt_s2 = ""
        book_data = None
        ## 1. get book data for rendering
        book_data = self.getBook()
        if not book_data:
            return (False, "EROARE: Cartea nu exista in catalog")
        rslt_s1 = "\nDate generale incarcate din catalog."
        # TODO...

        book_data["nav"] = None
        book_data["nav"] = self.getBookNav(format = "yaml")
        exit_code_s1 = bool(book_data["nav"])
        WARNING_CONTENT = "# `nav` section AUTO GENERATED @run-time. DO NOT MODIFY it.\n"
        book_data["nav"] = \
            WARNING_CONTENT \
            + book_data["nav"]
        rslt_s1 += "\nDate navigare incarcate." if exit_code_s1 else "NE-executat"
        if not exit_code_s1:
            return (False, rslt_s1)
        ## 2. render mkdocs_template.yml
        # TODO ... use
        # self.jinja_env
        exit_code_s2 = True  # ... supose exec until finisf step ...
        rslt_s2 = ...  # + stdout + stderr of prev run)
        rslt_s2 = f"\nRandare Jinja: {rslt_s2}"
        if not exit_code_s2:
            return (False, rslt_s1 + rslt_s2)
        ## if got here, everithing was ok so return True and all result outputs
        return (True, rslt_s1 + rslt_s2)
