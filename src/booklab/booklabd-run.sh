# **boolabd-run** run web / http booklabd server
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)
# Updated at: 250829



# run gunicorn to serve web api app. Arg #1 state:
#   if == "d" then run as daemon
#   if anything else or missing run once for tests
# gunicor is run with option to reload app when any of its files changes
if [ $1 = "d" ]
then
    gunicorn --reload -u app -D booklab.booklabd:api_app
else
    gunicorn -c gunicorn.conf.py
fi



