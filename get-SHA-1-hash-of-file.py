#!/usr/bin/python3
#SHA-1 hash of the file v1.1
#by xyzneverland
import hashlib
import os
import time

def read_file(file_name, encoding="utf-8"):
  with open(file_name, "r", encoding=encoding) as f:
    return f.read()

file_name = input("Please enter the file name: ")

while not os.path.exists(file_name):
  file_name = input("File not found. Please enter the file name again: ")

file_contents = read_file(file_name, encoding="latin1")

sha1 = hashlib.sha1()
file_contents_encoded = file_contents.encode(encoding="latin1")
sha1.update(file_contents_encoded)
file_hash = sha1.hexdigest()

print(f"The SHA-1 hash of the file '{file_name}' is: {file_hash}")
time.sleep(10)
