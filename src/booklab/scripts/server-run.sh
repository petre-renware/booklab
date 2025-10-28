#!/usr/bin/bash

#
# run web / http booklabd server
#
# run gunicorn to serve web api app. Arg #1 state:
#   - if == "d" then run as daemon
#   - if == "anything else" or missing run once for tests
#   - if == "k": for kill process.
#   - if == "s" show running gunicorn processes
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)
#

$(pdm venv activate)
case $1 in
    -d|--daemon)
        echo Start gunicorn as daemon... Running PIDs are:
        gunicorn -c python:booklab.conf.gunicorn_config -p ~/.gunicorn.PID -D
        ps -A | grep gunicorn
        ;;
    -k|--kill)
        echo Stop gunicorn...
        kill `cat ~/.gunicorn.PID`
        ;;
    -s|--status)
        echo PIDs of gunicorn running proceses:
        ps -A | grep gunicorn
        ;;
    -r|--restart)
        echo Stop gunicorn...
        kill `cat ~/.gunicorn.PID`
        sleep 1
        echo Start gunicorn as daemon... Running PIDs are:
        gunicorn -c python:booklab.conf.gunicorn_config -p ~/.gunicorn.PID -D
        ps -A | grep gunicorn
        ;;
    *)
        echo Run gunicorn as foreground...
        gunicorn -c python:booklab.conf.gunicorn_config
        ;;
esac



