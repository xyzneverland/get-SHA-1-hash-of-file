#!/usr/bin/python3
#SHA-1 hash of the file v1.2 (https://github.com/xyzneverland/get-SHA-1-hash-of-file/)
#by xyzneverland (https://github.com/xyzneverland/)
import hashlib
import os
import time

def read_file(file_name):
  with open(file_name, "rb") as f:
    return f.read()

file_name = input("Please enter the file name: ")

while not os.path.exists(file_name):
  file_name = input("File not found. Please enter the file name again: ")

file_contents = read_file(file_name)
sha1 = hashlib.sha1()
sha1.update(file_contents)
file_hash = sha1.hexdigest()

print(f"The SHA-1 hash of the file '{file_name}' is: {file_hash}")
time.sleep(10)
