import requests
from lxml import etree

s = requests.Session()

USERNAME = 'xxxxx'
PASSWORD = 'xxx'

INIT_URL = 'https://securetrans.fitchratings.com/'

LOGIN_URL = 'https://securetrans.fitchratings.com/action/login'
REDIRECT_URL = 'https://securetrans.fitchratings.com/action/storage'
FILE_URL = 'https://securetrans.fitchratings.com/action/dload/data/20181001.bnk.hist.lc.zip'

#Step 1: Open Page

req = s.get(INIT_URL)
login_html = etree.HTML(req.content)

hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

form['user'] = USERNAME
form['pwd'] = PASSWORD

print(form)

#Step 2: login
response = s.post(LOGIN_URL, data=form)

# print(response.text)
print(response.cookies)
print(response.headers)

#Step 3: Redirect
s.headers.update(response.headers)
s.cookies.update(response.cookies)
try:
    nextResp = s.get(REDIRECT_URL)
except Exception as e:
    print(e)

#Step 4: download
fileDownloaded = s.get(FILE_URL, data=form)
fileDownloaded = s.get(FILE_URL)
open('file.zip', 'wb').write(fileDownloaded.content)

print(fileDownloaded.text)

with open("downloaded.zip", "wb") as code:
    code.write(fileDownloaded.content)





