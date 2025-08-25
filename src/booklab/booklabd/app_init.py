"""**app_init** module that initialize `booklabd` application
This module is designed to initialize the main web application object `api_app`.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created: 25-aug-2025
"""

from flask import Flask


def init_app(
    app_name: str
) -> Flask:
    """Create Flask application object and return it

    Args:

        `app_name`: name of web application objwcr

    Return:

        web application object
    """
    app = Flask(app_name)
    return app

# ... this should be moved in main __init.py__ import routes
