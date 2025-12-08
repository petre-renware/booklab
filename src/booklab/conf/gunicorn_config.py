"""
Configuration file for gunicorn in serving `booklabd` server application

This is a Python file that will be executed by gunicorn at run-time.
As consequence declare all assignements as valid Python code.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from booklab import PACKAGE_ROOT

reload = True  # Specify to reload gunicorn if code under scope change. Need a "file change notifier" to be active - see gunicorn documentation for details.
user = "app"  # User under authority to run gunicorn. Set as "app". In not set root user will be considered.
wsgi_app = "booklab.booklabd:api_app"  # The application module:object to be executed by gunicorn at load.
#TODO add PID file wrting into PACKAGE_ROOT/run directory


all_cfg = locals()  # All configuration variables as dictionary.


