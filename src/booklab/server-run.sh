#!/usr/bin/bash

#
# run web / http booklabd server
#
# run gunicorn to serve web api app. Arg #1 state:
#   - if == "d" then run as daemon
#   - if == "anything else" or missing run once for tests
#   - if == "k": for kill process.
#   0 if == "s" show running gunicorn processes
#
#     keep in mind that need to run gunicorn with
#     `pid...` option to have process pid or
#     or run `pgrep gunicorn >gunicorn.pid` to create one
#
# config file (or a symlink to) should be present in directory where from this script is run
# config file: .../booklab/conf/conf/gunicorn.conf.py
#
# Author: Petre Iordanescu (petre.iordanescu@gmail.com)
#

case $1 in
    -d|--daemon)
        echo Start gunicorn as daemon... Running PIDs are:
        pdm run gunicorn -c python:booklab.conf.gunicorn_config -p ~/.gunicorn.PID -D
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
        pdm run gunicorn -c python:booklab.conf.gunicorn_config -p ~/.gunicorn.PID -D
        ps -A | grep gunicorn
        ;;
    *)
        echo Run gunicorn as foreground...
        pdm run gunicorn -c python:booklab.conf.gunicorn_config
        ;;
esac



