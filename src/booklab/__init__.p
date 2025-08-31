"""**booklab** main python package for Booklab system

Consists of the following basic modules:
- `booklab-cli` which is a CLI application to manage system
- `booklabd` designed to serve `/api/.../` system routes that need database write access
Despite these Python modules, there are other directories in package, the most relevant being:
- `data/` containing the system data in JSON files
- `conf/` containing configuration files for different system components including infrastructure ones like gunicorn or nginx
- `doc/` containing system usage documentation (aka api interface)

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Last update: aug.2025
"""

import pathlib

# Booklab system version. This is the single version refrence
__version__ = "0.4b2"

# get current directory absolute path and construct all work/refered paths
PACKAGE_ROOT = pathlib.Path(__file__).parent.resolve()
DATA_ROOT = "...tb get..."  # database files directory
CONF_ROOT = "...tb get..."  # config files directory

# test & debug print
print(f"*** PACKAGE_ROOT dir is {PACKAGE_ROOT} ")




