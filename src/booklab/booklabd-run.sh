#!/usr/bin/bash
# **boolabd-run** run web / http booklabd server
#
# run gunicorn to serve web api app. Arg #1 state:
#   - if == "d" then run as daemon
#   - if "anything else" or missing run once for tests
#   - ...tbd  if == "k": for kill process.
#     keep in mind that need to run gunicorn with
#     `pid...` option to have process pid or
#     or run `pgrep gunicorn >gunicorn.pid` to create one
#
# config file (or a symlink to) should be present in directory where from this script is run
# config file: .../booklab/conf/conf/gunicorn.conf.py
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)
# Updated at: Sep.2025
#

case $1 in
    -d|--daemon)
        echo Start gunicorn as daemon... Running PIDs are:
        gunicorn -c gunicorn.conf.py -p ./run/gunicorn.PID -D
        ps -A | grep gunicorn
        ;;
    -k|--kill)
        echo Stop gunicorn...
        kill `cat ./run/gunicorn.PID`
        ;;
    -s|--status)
        echo PIDs of gunicorn running proceses:
        ps -A | grep gunicorn
        ;;
    -r|--restart)
        echo Stop gunicorn...
        kill `cat ./run/gunicorn.PID`
        sleep 1
        echo Start gunicorn as daemon... Running PIDs are:
        gunicorn -c gunicorn.conf.py -p ./run/gunicorn.PID -D
        ps -A | grep gunicorn
        ;;
    *)
        echo Run gunicorn as foreground...
        gunicorn -c gunicorn.conf.py
        ;;
esac



