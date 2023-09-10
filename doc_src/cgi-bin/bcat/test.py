#!/usr/bin/python3

#-----------------------------------------------------------
#
# Test script care va executa "whoami" pentru a testa daca masina este live si informatiile vitale ale acesteia
#
#-----------------------------------------------------------

import os


print("Content-Type: text/html\n")

print("<!doctype html><title>Hello</title><h2>BookLab - BCAT component</h2>")

my_name = __name__
my_crt_dir = os.getcwd()

print(f"<p>my code-name: {my_name}</p>")
print(f"<p>current directory: {my_crt_dir}</p>") #NOTE: DE RETINUT aici a afista dir crt ca ".../static_portal/" deci nu cgi-bin






