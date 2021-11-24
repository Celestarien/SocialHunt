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
    url = 'https://login.yahoo.com'

#################################
    # VOIR LES REQUETES AVEC BURP !!!
    # Tout le temps la même pas page afficher car la variable email_search n'est pas pris en compte
    # ?username=' + emailSearched + '@yahoo.com'
    # Http to HTTPS
    # On doit ajouter tout les parametres POST necessaire afin que la requete soit correctement envoyé
    # Creuser du coté des paramètres pour display la page du Captcha si le user existe
    # Si le User ne fonctionne pas, pas de captcha, les parametres checker sont donc suffisant.
#################################

    cookies = {'Cookie' : 'GUCS=AemCXECr; B=7drh2ttgpqlmb&b=3&s=ln; A3=d=AQABBM5WnWECEJczGikDGIHzHttUh0_Vo7QFEgABBQGonmGFYuUzb2UB9qMAAAcIy1adYe8i7nY&S=AQAAAi-VhwEsEm3Jv1zwYorwCXg; A1=d=AQABBM5WnWECEJczGikDGIHzHttUh0_Vo7QFEgABBQGonmGFYuUzb2UB9qMAAAcIy1adYe8i7nY&S=AQAAAi-VhwEsEm3Jv1zwYorwCXg; A1S=d=AQABBM5WnWECEJczGikDGIHzHttUh0_Vo7QFEgABBQGonmGFYuUzb2UB9qMAAAcIy1adYe8i7nY&S=AQAAAi-VhwEsEm3Jv1zwYorwCXg&j=GDPR; EuConsent=CPQJWQMPQJWQMAOACBFRBtCoAP_AAH_AACiQIJNf_X__bX9n-_59__t0eY1f9_r_v-Qzjhfdt-8F2L_W_L0H_2E7NB36pq4KuR4ku3bBIQNtHMnUTUmxaolVrzHsak2MryNKJ7LkmnsZe2dYGHtPn91T-ZKZ7_78__f73z___9_-39z3_______9____-___V_993________9nd____BBIAkw1LyALsSxwJNo0qhRAjCsJDoBQAUUAwtE1gAwOCnZWAR6ghYAITUBGBECDEFGDAIABAIAkIiAkALBAIgCIBAACAFSAhAARMAgsALAwCAAUA0LECKAIQJCDI4KjlMCAiRaKCWysASi72NMIQyywAoFH9FRgIlCCBYGQkLBzHAEgJYAYaADAAEEEhEAGAAIIJCoAMAAQQSA; GUC=AQABBQFhnqhihUIh6gUT; cmp=v=21&t=1637701325&j=1; AS=v=1&s=myWuwAD6&d=C619ea977|ObqCM9T.2SrxIi.PVwnsQPoHYRHVqy8OSJcvtI6MtHwIGowvL.7OWSvA8p88TBpou8d1VBK19OsaIIY498gjynUyKZu4evMzwTBLu_OL.spNp53CJI7xEwf97zo5S7ed3W1_jJIJAWMLL2rMXj4Nx_UVHfdKzWWZ1BjGVdvzpQKP5Emfk95uJQZ0lWSDYoyjNIvfTEC6mUXjsW5D0KMqrIisRvHDja3LBiAk_xIfnUnQEQQm4DndcNoE0NkWsuz1dwnBFYz0ujFVdvQ1kXeUPjC9g3cp9jn_0hhiZ13sa5iON3lw0SjuCuDv3EXtQ.lCfqey7Iog0qm0.O14WtX0A5AyLh13XFHqPPjLUN_6IMdhD_FwzNq4cEqfJ19kn9FsujGOa3ZyH9cZN2qRtgHaxDvfTjo9.ycYlibZEFbTivfGaXmQK01kWnmE215tXcq2duGl1GsjqceAG9wHI3Z8MBHmZkqWf711Ap338SlTbVtLz.H19okuHyVP5wcMDsAsM6OaIyL8yzUJ2.a5y9oJuS8jg1oPc_H72e_pjp9JMGqCc5xdRUrsBxrCEFAl4vBmnCtstO3y0hOP1TdY3q1DT8MyVc4mTt33fNzqYjusk5LWrhnY5dx36i8It8BCp.PGj85fTr_u6SQtpwl0K280u6hpeExbpH2vUdsKX4RirUNSGoEl4aORcgaE6k23HA5B4osxqZJecC4BSAYxB5HNhZ0hnIW24ZLdUsqqFHWnBqdC.iDtg4Ulzm9Nk9cBGKMhf1dGZBW0pdJK33ofPNEwdldCN6C1RnXT_xAbCNMa_7hfkGpaq6C8HCeGXlQ5Qmzjk5YI3D_kkBXDKWX4fwqS_MUVcc_ANX57w9qcm1J5iUXfFo0.tiGmBD6iYKSF3OSa_z4rBpSAAB7k8vTscA85DOsWMZefi66uZHHUnf3BpR4QMyxbzhanQboDenj0UFH9BMrJq8DLB1cvuU9fYf.87mcR~A'}
    user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

    requests.Session()


    data = {'browser-fp-data' : '{"language":"fr","colorDepth":24,"deviceMemory":"unknown","pixelRatio":1,"hardwareConcurrency":12,"timezoneOffset":-60,"timezone":"Europe/Paris","sessionStorage":1,"localStorage":1,"indexedDb":1,"cpuClass":"unknown","platform":"Linux x86_64","doNotTrack":"1","plugins":{"count":0,"hash":"24700f9f1986800ab4fcc880530dd0ed"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"NVIDIA Corporation~NVIDIA GeForce GTX 1050 Ti/PCIe/SSE2","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":14,"hash":"a24a80806be03ad4525b3b1475a3d3fe"},"audio":"35.73833402246237","resolution":{"w":"1920","h":"1080"},"availableResolution":{"w":"1051","h":"1920"},"ts":{"serve":1637701566624,"render":1637701564127}}' , 'crumb' : 'PUwz9RaTz7C', 'acrumb' : 'myWuwAD6' , 'sessionIndex' : 'Qw--' , 'displayName' : '', 'deviceCapability' : '{"pa":{"status":false}}' , 'username': emailSearched, 'signin' : 'Suivant' , 'persistent' : 'y' }
    
    # Modification du format Get en Post (Voir Burp)
    req = requests.post(url,  headers = user_agent, data=data, cookies=cookies)
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
