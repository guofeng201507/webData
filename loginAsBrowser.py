from selenium import webdriver

import zipfile
import glob
import os
import time
import json
# try:
#     os.remove(filename)
# except OSError:
#     pass
#
#
usernameStr = 'xxx'
passwordStr = 'xxx'

browser = webdriver.Chrome("C:/Users/guofe/workspace/chrome/chromedriver.exe")
browser.implicitly_wait(10)
# options = webdriver.ChromeOptions()
# options.

browser.get('https://securetrans.fitchratings.com/')

username = browser.find_element_by_id('user').send_keys(usernameStr)

password = browser.find_element_by_id('pwd').send_keys(passwordStr)

button = browser.find_element_by_tag_name('button').click()

dataFolder = browser.find_element_by_link_text('data').click()

for zipFile in browser.find_elements_by_partial_link_text('.bnk'):
    zipFile.click()

time.sleep(10)

os.chdir("C:/Users/guofe/Downloads")

for file in glob.glob("*.zip"):
    print(file)
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall('C:/Users/guofe/Downloads/extracted/')
    zip_ref.close()
    try:
        os.remove(file)
    except OSError:
        pass

os.chdir("C:/Users/guofe/Downloads/extracted")

for jsonFile in os.listdir(os.curdir):
    print(jsonFile)
    with open(jsonFile, 'r') as f:
        dict = json.load(f) #error here: json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
        print(dict)
