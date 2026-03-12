#!/usr/bin/env python

from time import sleep
"""
    print function with flush parameter
    Created by : Markuss Jānis Pommers

    https://wwwincludehelp.com/python/flush-parameters-in-python-with-print-function.aspx
"""

# output is not flushed here
print("Es macos programmet! ", end='')
print("Lietoju funkciju print. ", end='')
print("Ar parametru flush. ", end='')

sleep(5)
print("Bye!!!")
input("Press <ENTER> to exit.")
