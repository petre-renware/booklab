"""Main python package for Booklab system.

Consists of the following components:

- `booklab_cli` main CLI application to operate the system
- `booklabd` designed to serve `/api/.../` routes used by all functionalities that need write / update and POST operations
- `conf` contain configuration files for different system components including infrastructure ones like gunicorn or nginx
- `doc_src` contain the source of static site directory as Markdown files
- `docs` contain rhe static site compiled and "ready to use as-is" with any standard HTTP server
- `my_books` contain the end user created & generated books and `books_catalog.json` with info about all user books
- `scripts` contain diffrent scrpts usefull in system administrarion (install, maintain, configure, in-house development and customizations)
- `booklab.pyz`as standard Python PEX package

Package is compliant with Python PEP packaging specificatios and published on PyPi under `booklab` name.
Package is open source licenced and available as source package on GitHub under `booklab` name and author repositories.

author: Petre Iordanescu (_mail:_ petre.iordanescu@gmail.com, _GitHub:_ petre-renware)
"""

import pathlib
import os

from .__version__ import __version__
from .conf import booklab_ext_url


# URL paths
EXT_SERVER = booklab_ext_url.EXT_SERVER
EXT_PATH = booklab_ext_url.EXT_PATH
FULL_EXT_URL = booklab_ext_url.FULL_EXT_URL

# file system paths
PACKAGE_ROOT = pathlib.Path(__file__).parent.resolve()
PROJECT_ROOT = PACKAGE_ROOT.parent.resolve().parent.resolve()
DATA_ROOT = PACKAGE_ROOT.joinpath("my_books")
CONF_ROOT = PACKAGE_ROOT.joinpath("conf")
MY_BOOKS_ROOT = PACKAGE_ROOT.joinpath("my_books")
STATIC_SITE_ROOT = PACKAGE_ROOT.joinpath("docs")

#4dbg print(f"{PACKAGE_ROOT=}\n {PROJECT_ROOT=}\n {DATA_ROOT=}\n {CONF_ROOT=}\n {STATIC_SITE_ROOT=}\n")






