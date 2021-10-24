import requests

# Packages pip install googlesearch-python

from googlesearch import search


def main():
    emailSearched = input('Quelle email veux-tu tracker ?\n')
    request = requests.get('https://twitter.com/' + emailSearched)
    search(emailSearched, num_results=1)
    x = input('')