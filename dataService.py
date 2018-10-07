import requests
from lxml import etree

s = requests.session()

USERNAME = 'xxxxx'
PASSWORD = 'xxxxx'

LOGIN_URL = 'https://securetrans.fitchratings.com/'

FILE_URL = 'https://securetrans.fitchratings.com/action/dload/data/20181001.bnk.hist.lc.zip'


# req = requests.get(LOGIN_URL)
req = s.get(LOGIN_URL)

login_html = etree.HTML(req.content)

hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

form['user'] = USERNAME
form['pwd'] = PASSWORD

print(form)


response = s.post(LOGIN_URL, data=form)

print(response.text)

# fileDownloaded = s.get(FILE_URL, data=form)
# open('file.zip', 'wb').write(fileDownloaded.content)
#
# print(fileDownloaded.text)
#
# with open("downloaded.zip", "wb") as code:
#     code.write(fileDownloaded.content)





