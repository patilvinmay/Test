#!/usr/bin/env python3
import requests
import os

url = 'https://raw.githubusercontent.com/patilvinmay/Test/main/Hello.py'
req = requests.get(url)
pycode = req.text

os.getcwd()

f = open("temp.py", "w")
f.write(pycode)
f.close()

from temp import print_hi
print_hi('Vinmay')
