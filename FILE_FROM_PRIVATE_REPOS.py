import requests
import sys

user = 'patilvinmay'
pao = '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'

github_session = requests.Session()
github_session.auth = (user, pao)

# providing raw url to download csv from github
file_url = 'https://raw.githubusercontent.com/patilvinmay/Testing/main/Hello.py'

download = github_session.get(file_url).text

pwd="C:\\Users\\admin\\Desktop\\temp.py"

f = open(pwd, "w")
f.write(download)
f.close()

from temp import *

print_abcdefg_hi("Vinmay")
