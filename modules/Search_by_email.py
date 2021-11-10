import requests
import urllib.request
from bs4 import BeautifulSoup
import ssl

# Packages pip install googlesearch-python

# from googlesearch import search


def main():
    emailSearched = input('Quelle est la personne dont tu veux tracker l\'email ?\n')

    # Protonmail

    print('###################### PROTONMAIL ######################')
    req = urllib.request.Request('https://api.protonmail.ch/pks/lookup?op=index&search=' + emailSearched + '@protonmail.com')
    gcontext = ssl.SSLContext()
    with urllib.request.urlopen(req, context=gcontext) as response:
        page = response.read()
        soup = BeautifulSoup(page, features = "lxml")
        for line in soup:
            print(line.text)
        print('#####################################################')



    # Yahoo
    print('###################### Yahoo ######################')
    url = 'http://login.yahoo.com/?.src=ym&pspid=2023392333&activity=ybar-mail&.lang=fr-FR&.intl=fr&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.intl%3Dfr%26.lang%3Dfr-FR%26pspid%3D2023392333%26activity%3Dybar-mail&username=' + emailSearched + '@yahoo.com'
    requests.Session()
    req = requests.post(url=url)
    f = open('test.txt', 'w+')
    f.write(str(req.text))
    find = False
    for line in req.text:
        if 'error-msg hide' in str(line):
            find = True
    if find == True:
        print( emailSearched + '@yahoo.com')
    else:
        print('Pas d\'email trouvé à ce nom')
    print('#####################################################')
