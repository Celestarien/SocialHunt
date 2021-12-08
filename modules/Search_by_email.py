import requests
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
# from decouple import config

def main():
    
    emailSearched = input('Who is the person whose email you want to track ?\n')
    emailSearched = urllib.parse.quote_plus(emailSearched)

    # SSL

    gcontext = ssl.SSLContext()

    # Facebook

    print('###################### Facebook ######################')

    url = 'https://www.facebook.com/search/people/?q=' + emailSearched

    req = requests.get("https://graph.facebook.com/search?access_token=" + config('FACEBOOK_TOKEN') +  "&q=" + emailSearched + "&type=page")

    # req = requests.get(url)

    print(req.text)

    # divUserds = '<div class="rq0escxv l9j0dhe7 du4w35lb hybvsw6c io0zqebd m5lcvass fbipl8qg nwvqtn77 k4urcfbm ni8dbmo4 stjgntxs sbcfpzgs" style="border-radius: max(0px, min(8px, ((100vw - 4px) - 100%) * 9999)) / 8px;">'

    # req = urllib.request.Request(url)

    # with urllib.request.urlopen(req, context=gcontext) as response:
    #     page = response.read()
    #     soup = BeautifulSoup(page, features = "lxml")
    #     for line in soup:
    #         f = open('test.txt', 'w+')
    #         f.write(str(line))

    print('#####################################################')