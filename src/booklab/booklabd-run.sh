"""**boolabd-run** run web / http booklabd server
wip...more details here ??? ...

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
Created at: 250826
"""



#...drop.me from booklab.booklabd import api_app

gunicorn -b 0.0.0.0:5003 -u app booklab.booklabd:api_app




