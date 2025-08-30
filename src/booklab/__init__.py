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
# import os
# import pathlib.Path

__version__ = "0.4b2"

# ...tbd #TODO get current directory as absolute path and store it in
# PACKAGE_PATH = 

