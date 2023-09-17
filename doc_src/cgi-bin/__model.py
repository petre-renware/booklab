#!pyenv/bin/python3

#=============================================================
# Script to #TODO objective here...
#-----------------------------------------
# Author: Petre Iordanescu, (c) RENware Softwre Sytems
#=============================================================



import os
import cgi
import cgitb
import pysondb
import jinja2


my_name = __name__
my_crt_dir = os.getcwd()
cgitb.enable() # this activate displaying errs on HTML page and log them...


# HTTP header section for HTML content
print("Content-Type: text/html\n")
print()



