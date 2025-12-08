import os
import pysondb
import w3lib.url
import json
import pylibyaml
import yaml  # NOTE: mandatory to import after pylibyank
import rich
from rich import print as rprint
from rich.console import Console as rConsole
from rich.markdown import Markdown as rMarkdown
from pathlib import Path
import jinja2 as j2
import datetime
from dataclasses import dataclass
from typing import Type
from flask import Flask
from werkzeug.urls import quote as url_quote

from booklab import MY_BOOKS_ROOT
from booklab import EXT_PATH
from booklab import FULL_EXT_URL


@dataclass(frozen = True)
class Results:
    """Define a result model (type) frequently used as return set by MyBook methods.

    Class as data type (model) is defined _frozen_ to protect change its instance
    attribites once created. This is usefull when used as member in other
    objects to protect them to be altered outside the object.
    """
    exit_code: None | bool = None  # Exit code of run method. Usual is the same as method returns.
    exit_text: None | str = None  # Output text of last run method (equivalent of stdout when run a console process).

    @property
    def console_out(self) -> None | str:
        """Return `exit_text` rendered to console format as printed on a simple usual / dumb terminal.
        """
        from rich.console import Console as rConsole
        from rich.markdown import Markdown as rMarkdown
        _console = rConsole()
        _value = rMarkdown(
            "``` console\n" +
            self.exit_text +
            "\n````"
        )
        with _console.capture() as _capture:
            _console.print(_value)
        _value = _capture.get()
        return _value


class MyBooks:
    """
    Class that manage end user books.

    - _Mandatory requirements:_
        - _rendering:_ any Jinja renderings will be made 
          "from string" (ie, using Flask `render_from_string()` which is included)
          or by creating a local Jinja environment.
    """
    MY_BOOKS_URL_prefix: str = "/my-books/"  # URL prefix to add when accesing a book local (generated) site.
    MY_BOOK_URL: str = None  # Instantiated book URL to local (generated) site.
    MY_BOOKS_ROOT: str = MY_BOOKS_ROOT  # Confusing name ? just duplicate the global one in class namespace.
    book_code: str = None  # Instanciated book code.
    db_books_catalog: pysondb = None  # Books catalog data controller.
    db_book_nav: pysondb = None  # Books navigation data controller.
    jinja_env = None  # Jinja environment usable for my_books rendering needs.
    results: Type[Results] = Results(
        exit_code = None,
        exit_text = None,
    )  # Keep result of last run method (for methods that should return composite result).

    def __init__(
            self, db: pysondb,
            book_code: str
    ) -> None:
        """Init an instance of class MyBooks.
        """
        self.MY_BOOKS_ROOT = MY_BOOKS_ROOT  # Confusing name ? just duplicate the global one in class namespace
        self.book_code = book_code
        self.db_books_catalog = db
        #
        self.MY_BOOK_URL = w3lib.url.canonicalize_url(
            url_quote(
                str(FULL_EXT_URL)
                + str(MyBooks.MY_BOOKS_URL_prefix)
                + str(self.book_code)
                + "/docs/"
            )
        )
        #
        self.db_book_nav = None
        if (_this_bk_path := self.getBookPath()):
            file_dbnav = os.path.join(_this_bk_path, "book_navigation.json")
            if os.path.isfile(file_dbnav):
                self.db_book_nav = pysondb.db.getDb(file_dbnav)
        #
        self.jinja_env = j2.Environment(
            loader = j2.PackageLoader(
                package_name = "booklab.my_books",
                package_path = "."
            ),
            autoescape = j2.select_autoescape()
        )
        #
        self.results = Results(
            exit_code = None,
            exit_text = None
        )

    def getBook(self) -> dict | None:
        """Check for a given book code that is not None, exists in database and is exactly 1 record.

        Return:
            dict: with found record or 
            None: if any of conditiona is not met
        """
        if not self.book_code or not isinstance(self.book_code, str):
            return None
        # Check if record exists and is only one.
        bk_rec = None
        bk_rec = self.db_books_catalog.getBy({"code": self.book_code})
        if bk_rec:
            if isinstance(bk_rec, list):
                # There is more than 1 record and keep only the first one.
                bk_rec = bk_rec[0]
            elif isinstance(bk_rec, dict):
                # Do nothing, record is in right format.
                pass
            else:
                # Unknown record type so exit with None.
                return None
            # Upd key "store_location".
            bk_rec["store_location"] = self.getBookPath()
            # When location exists append `/`to ckear state it as directory otherwise let it unchanged.
            if bk_rec["store_location"]:
                bk_rec["store_location"] += "/"
            # Upd key "preview_url".
            bk_rec["preview_url"] = self.getBookURL()
            if self.db_book_nav:  # Chk if nav definition exisys (as json data-file).
                nav_file = self.db_book_nav.filename
                bk_rec["nav_file_location"] = nav_file
            else:
                bk_rec["nav_file_location"] = None
            # Return updated record.
            return bk_rec
        else:
            return None

    def getBookNav(
            self,
            format: str = None
    ) -> None | dict | str:
        """Get book navigation.

        Navigation info is retrieved from `book_navigation.json` data-file
        and is identified by `self.db_book_nav` pysondb handler.

        Return:
            dict: using `format = "dict"` (default option)
            str: JSON string using `format = "json"`
            str: YAML string using `format = "yaml"`
            None: if not known format
        """
        if not self.db_book_nav:
            return None
        bk_nav_raw_data = self.db_book_nav.getAll()
        bk_nav_data = dict()
        bk_nav_data["nav"] = bk_nav_raw_data
        # Check format param and return accordingly.
        if not format or format is ...:
            format = "dict"  # Default value if not specified or set as None.
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
        return None  # If get here its a bug due to logic error.

    def wrBookNav(self) -> bool:
        """Write out file "book_navigation.yml".

        Return:
            True: if file was written
            False: if file was not written or cannot be read regardless why (usual problem is source file)

        _Lateral effects:_

        - _on disk:_ create / update current book navigation definition file in YAML format (`book_navigation.yml`).
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
        try:  # Write file.
            out_file.write_text(yaml_content)
        except:
            return False
        try:  # Test if file can be read.
            with out_file.open("r") as f:
                _c = f.read()
            return True
        except:
            return False
        return True

    def getBookPath(self) -> str:
        """Get absolute path of current book root directory.
        """
        my_book_path = os.path.abspath(os.path.join(self.MY_BOOKS_ROOT, self.book_code))
        if os.path.isdir(my_book_path):
            return my_book_path
        else:
            return None

    def getBookURL(self) -> str:
        """Get preview URL (redirectable as is) for current book_code.
        """
        return self.MY_BOOK_URL

    def renderBookConfig(self) -> Results:
        """Render current book configuration file.
        Produce file `mkdocs.yml` as being the configuration file to build the book.
        File is writen in book root directory.

        Return:

        - `Results object` reference to `self.results`

        _Lateral effects:_

        - _on disk:_ update current book configuration file (`mkdocs.yml`).
        """
        exit_text = "*** Start book configuration file (mkdocs.yml) rendering"
        book_data = None
        # Get book data for rendering.
        book_data = self.getBook()
        if not book_data:  # If book is not present in catalog force exit.
            exit_text += "\nEROARE: Cartea nu exista in catalog"
            self.results = Results(
                exit_code = False,
                exit_text = exit_text
            )
            return self.results
        # Get book navigation d2finition / configuration
        if not self.db_book_nav:  # If book nav does not exists force exit.
            exit_text += "\nEROARE: Cartea nu are navigarea definita (book_navigation.json)."
            self.results = Results(
                exit_code = False,
                exit_text = exit_text
            )
            return self.results
        # Prepare nav(igation) confuguration.
        exit_text += "\nDate generale incarcate din catalog."
        book_data["nav"] = None
        exit_code = self.getBookNav(format = "yaml")
        if not exit_code:  # If nav config cannot be obtained as YAML then force exit.
            exit_text += "\nEROARE: Cartea nu are navigare definita (book_navigation.json)."
            self.results = Results(
                exit_code = False,
                exit_text = exit_text
            )
            return self.results
        else:  # Rationale: ret of getBookNav() can be None or got value.
            book_data["nav"] = exit_code
            _crtdt = datetime.datetime.now()
        WARNING_CONTENT = f"# nav section AUTO GENERATED @{_crtdt:%Y-%m-%d %H:%M:%S}. DO NOT MODIFY it.\n"
        book_data["nav"] = \
            WARNING_CONTENT \
            + book_data["nav"]
        exit_text += "\nDate navigare incarcate."
        # Render mkdocs_template.yml.
        exit_text += "\nRandare temmplate configurate carte"
        template_cfg_file = "mkdocs_template.yml"
        to_render_file = self.book_code + "/" + template_cfg_file
        #---TST if template file exists.
        _tst1 = os.path.isfile(
            os.path.join(
                self.getBookPath(),
                template_cfg_file
            )
        )
        if not _tst1:
            exit_text += "\nEROARE: Template configurare carte inexistent (mkdocs_template.yml)."
            self.results = Results(
                exit_code = False,
                exit_text = exit_text
            )
            return self.results
        #---EOF ck config template existance. Can continue safe.
        out_file = os.path.join(
            self.getBookPath(),
            "mkdocs.yml",
        )
        out_file = Path(out_file)
        book_cfg = self.jinja_env.get_template(to_render_file)
        try:
            book_cfg = book_cfg.render(book_data = book_data)
        except:
            exit_text += "\nEROARE: randarea mkdocs_template.yml esuata."
            self.results = Results(
                exit_code = False,
                exit_text = exit_text
            )
            return self.results
        else:  # Try block executed correctly.
            exit_text += f"\nRandare template configurare carte executata"
        #
        exit_text += "\nScrierea fisierului mkdocs.yml."
        try:
            out_file.write_text(book_cfg)
        except:
            exit_text += "EROARE: scrierea fisierului mkdocs.yml esuata."
            self.results = Results(
                exit_code = False,
                exit_text = exit_text
            )
            return self.results
        else:  # Try block executed correctly.
            exit_text += f"\nScrierea fisierului mkdocs.yml executata."
        ## If got here, everithing was ok so return True and all result outputs.
        self.results = Results(
            exit_code = True,
            exit_text = exit_text
        )
        return self.results

    def buildBook(self) -> None | str:
        """Build (mkdocs build) current boook.

        Build current book (ie, `mkdocs build`) in its own directory.
        Method suppose that mkdocs.yml file is good and book content directory (doc_src/) content is ok and "as-expected",
        that meaning the method just run nkdocs build process, collect output and return it.

        Return:

        - `str` stdout + stderr of run process
        - `None` if process exit with fatal err (standard baah return 1)

        _Lateral effects:_

        - _on disk:_ create / update current book static site directory (usual `docs/`).
        """
        #TODO ...
        pass

    def createPhysicalBook(self) -> bool:
        """Create physical book directory as copy of "book_template".

        _Lateral effects:_

        - _on disk:_ creates new directory & filrs on disk represing current book physical location.
        """
        #TODO ...
        pass





