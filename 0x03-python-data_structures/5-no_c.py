#!/usr/bin/python3

def no_c(my_string):
    nstring = ""
    for q in my_string:
        if q != 'c' and q != 'C':
            nstring += q
    return nstring		
