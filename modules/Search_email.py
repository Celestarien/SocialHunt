import requests
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl

# Packages pip install googlesearch-python

# from googlesearch import search


def main():
    emailSearched = input('What is the beginning of the email of the person you are looking for ? (example : firstName.lastName)\n')
    emailSearched = urllib.parse.quote_plus(emailSearched)

    emailSaved = []

    # SSL

    gcontext = ssl.SSLContext()


    # Protonmail

    print('###################### PROTONMAIL ######################')
    req = urllib.request.Request('https://api.protonmail.ch/pks/lookup?op=index&search=' + emailSearched + '@protonmail.com')
    with urllib.request.urlopen(req, context=gcontext) as response:
        page = response.read()
        soup = BeautifulSoup(page, features = "lxml")
        for line in soup:
            print(line.text)
        print('#####################################################')


    # Yahoo
    print('###################### Yahoo ######################')
    url = 'http://login.yahoo.com/?username=' + emailSearched + '@yahoo.com'
    requests.Session()

    data = {'input#login-username.phone-no': emailSearched}
    
    req = requests.post(url, data=data)
    print(req.text)
    
    # f = open('test.txt', 'w+', encoding='utf-8')
    # f.write(req)
    # f.close()

    # f = open('test.txt', 'r', encoding='utf-8')
    # lines = f.readlines()
    # for line in lines:
    #     print(line)
    
    # req = urllib.request.Request(url, method='POST')
    # # f = open('test.txt', 'w+')
    # # f.write(str(req))

    # with urllib.request.urlopen(req, context=gcontext) as response:
    #     page = response.read()
    #     soup = BeautifulSoup(page, features = "lxml")
    #     f = open('test.txt', 'w+', encoding="utf-8")
    #     for line in soup:
    #         f.write(str(line) + '\n')
    #     f.close()

    # f = open('test.txt', 'r', encoding="utf-8")
    # lines = f.readlines()

    
    
    # for line in lines:
    #     if '<p class="error-msg hide" id="username-error" role="alert"></p>\n' in line:
    #         print( emailSearched + '@yahoo.com')
    #         # print(line + '##' + str(compteur))        
    print('#####################################################')
