"""**app_init** module that initialize `booklabd` application
This module is designed to initialize the main web application object `api_app`.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from flask import Flask


def init_app(
    app_name: str,
    static_site_dir: str
) -> Flask:
    """Create Flask application object and return it

    Args:

        `app_name`: name of web application objwcr
        `static_site_dir`: directory used by Flask app to render Jinja templates

    Return:

        web application object
    """
    app = Flask(
        app_name,
        template_folder = static_site_dir,
        static_folder = static_site_dir
    )
    return app



