# **boolabd-run** run web / http booklabd server
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)
# Updated at: 250829
#
# run gunicorn to serve web api app. Arg #1 state:
#   if == "d" then run as daemon
#   if anything else or missing run once for tests
# gunicor is run with option to reload app when any of its files changes
# ...tbd to add optuon "k: for kill process. Keep
#   in mind that need run gunicorn with `pid...` option to have process pid or
#   or run `pgrep gunicorn >gunicorn.pid` to create one

case $1 in
d) gunicorn -c gunicorn.conf.py -D;;
*) gunicorn -c gunicorn.conf.py;;
esac



