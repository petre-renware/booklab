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
DATA_ROOT = PACKAGE_ROOT.joinpath("data")  # database files directory
CONF_ROOT = PACKAGE_ROOT.joinpath("conf")  # config files directory

# 4dbg... print("*** PACKAGE_ROOT dir: ", PACKAGE_ROOT)
# 4dbg... print("*** DATA_ROOT dir: ", DATA_ROOT)
# 4dbg... print("*** CONF_ROIT dir: ", CONF_ROOT)




