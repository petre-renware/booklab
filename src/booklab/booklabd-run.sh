# **boolabd-run** run web / http booklabd server
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)
# Updated at: 250829



# run gunicorn to serve web api app. Arg #1 state:
# if == "d" then run as daemon
# if anything else or missing run once for tests

if [ $1 = "d" ]; then
    gunicorn -b 0.0.0.0:5003 -u app -D booklab.booklabd:api_app
else
    gunicorn -b 0.0.0.0:5003 -u app booklab.booklabd:api_app
fi



