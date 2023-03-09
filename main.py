#!/usr/bin/env python3

# A simple python application to demonstrate the use of Digital signature 
# Milind Dinesh

import getopt , sys , hashlib

argumentList  = sys.argv[1:]
options = "d:e:"

try:
    arguments,_ = getopt.getopt(argumentList,options)
    if len(arguments) >1:
        print("You should only specify one option at a time.")
    elif arguments[0][0] == "-e":
        _,value = arguments[0]
        print(value)
        print("hash " + hashlib.sha256((value.encode("UTF-8"))).hexdigest())
except:
    print("something")