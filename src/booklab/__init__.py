"""**booklab** main python package for Booklab system

Consists of the following basic modules:

- `booklab-cli` which is a CLI application to manage system
- `booklabd` designed to serve `/api/.../` system routes that need database write access

Despite these Python modules, there are other directories in package, the most relevant being:

- `data/` containing the system data in JSON files
- `conf/` containing configuration files for different system components including infrastructure ones like gunicorn or nginx
- `doc-techical/` containing system usage documentation (aka api interface)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

import pathlib
import os

from .__version__ import __version__

PACKAGE_ROOT = pathlib.Path(__file__).parent.resolve()
DATA_ROOT = PACKAGE_ROOT.joinpath("data")  # database files directory
CONF_ROOT = PACKAGE_ROOT.joinpath("conf")  # config files directory
PROJECT_ROOT = PACKAGE_ROOT.parent.resolve().parent.resolve()
STATIC_SITE_ROOT = PROJECT_ROOT.joinpath("docs")









