"""**booklab** main python package for Booklab system

Consists of the following sub-packages:

- `booklab-cli` which is a CLI application to manage system
- `booklabd` designed to serve `/api/.../` system routes that need database write access
- `booklib` booklab system specific general library functions usable by all sub-modules
- `data` containing the system data in JSON files
- `conf` containing configuration files for different system components including infrastructure ones like gunicorn or nginx
- `doc_src` contains the source of static site directory as Markdown files
- `docs/` contains rhe static site compiled and "ready to use as-is" with any standard HTTP server
- `doc-techical` containing system usage documentation (aka api interface)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
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
DATA_ROOT = PACKAGE_ROOT.joinpath("data")
CONF_ROOT = PACKAGE_ROOT.joinpath("conf")
STATIC_SITE_ROOT = PACKAGE_ROOT.joinpath("docs")

## 4dbg printouts
# print(f"{PACKAGE_ROOT=}\n {PROJECT_ROOT=}\n {DATA_ROOT=}\n {CONF_ROOT=}\n {STATIC_SITE_ROOT=}\n")






