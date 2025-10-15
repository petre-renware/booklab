"""
Configuration file for gunicorn in serving `booklabd` server application

This is a Python file that will be executed by gunicorn at run-time.
As consequence declare all assignements as valid Python code.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from booklab import PACKAGE_ROOT


reload = True
user = "app"
wsgi_app = "booklab.booklabd:api_app"
#TODO add PID file wrting into PACKAGE_ROOT/run directory





