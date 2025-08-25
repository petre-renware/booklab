"""*app_init* module that initialize `booklabd` application
This module is designed to initialize the main web application object `api_app`.


Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created: 25-aug-2025
"""

from flask import Flask


def init_app() -> Flask:
    """Create Flask application object and return it

    """
    app = Flask(__name__)
    return app

# ... this should be moved in main __init.py__ import routes
