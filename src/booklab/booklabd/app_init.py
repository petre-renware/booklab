"""**app_init** module that initialize `booklabd` application

This module is designed to initialize the main web application object `api_app`.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


def init_app(
    app_name: str,
    static_site_dir: str,
    templates_dir: str,
    pjroot_location: str
) -> Flask:
    """Create Flask application object and return it

    Args:

        `app_name`: name of web application objwcr
        `static_site_dir`: directory used by Flask app to render Jinja templates
        `templates_dir`: directory name where templates are to becfound (relative to pjroot_location)
        `pjroot_location`: project root directory (relative to pjroot_location)

    Return:

        web application object
    """
    app = Flask(
        app_name,
        template_folder = templates_dir,
        static_folder = static_site_dir,
        root_path = pjroot_location
    )

    ''' DOESN'T WK. PROBABLY ARE MORE THAN 1 PROXIES. 1 on local maxhine and 1 on proxy host
    # this code enable Flask Proxy middlware
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,
        x_proto=1,
        x_host=1,
        x_prefix=1
    )
    '''

    return app



