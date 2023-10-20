#!/bin/bash
#
# starts in bck the BookLab HTTP server:
#   - with CGI option and port 80
#   - named to be able to kill it
#

# commend:
sudo python3 -m http.server 80 --directory docs/ --cgi
