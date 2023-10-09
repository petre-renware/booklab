#!/usr/bin/bash

#
# script to assembly mkdocs configuration file from parts
#
# - author: Petre Iordanescu, RENware Software Systems, petre.iordanescu@gmail.com
# - location: #NOTE... current location is where from script is called (in CGI case is the www root directory, so docs/)
#



# change directory in location where this script is located
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR #NOTE ... comment this code if is not required to change current location to those weher script is located


#NOTE ... continue from here

