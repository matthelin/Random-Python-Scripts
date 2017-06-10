#!/usr/bin/python

#A simple function to return a Unix DES-based hash based on a given cleartext value and salt

import crypt

clear_text = raw_input("Enter clear text: ")
salt = raw_input("Enter salt value: ")

hash_val = crypt.crypt(clear_text, salt)
print hash_val
