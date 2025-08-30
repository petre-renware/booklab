#
# Configuration file for gubicon in serving `booklabd` server application
# Warning: this is a Python file that will be onclude in gunicorn run as external module.
#.As consequence seclare all assignements as will be treated as Python code.
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)
# Created: Aug.2025
#

reload = True
user = "app"
wsgi_app = "booklab.booklabd:api_app"






