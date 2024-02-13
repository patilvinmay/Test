#!/usr/bin/env python3
import requests
import os

url = 'https://raw.githubusercontent.com/patilvinmay/Test/main/Hello.py'
req = requests.get(url)
pycode = req.text
pwd = os.getcwd()
pwd = pwd + '\\'
print_abcdefg(pwd)

f = open(pwd + "temp.py", "w")
f.write(pycode)
f.close()

from temp import print_abcdefg_hi

print_abcdefg_hi('Vinmay')
