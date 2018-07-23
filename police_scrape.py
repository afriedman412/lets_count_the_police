# its all your code ... in one place!
import pandas as pd
import billboard
from bs4 import BeautifulSoup
import re
import requests
import unidecode
import string
import datetime
import time
from IPython.display import clear_output
import urllib3
import certifi
import matplotlib.pyplot as plt
import seaborn as sns

# https://www.policeone.com/law-enforcement-directory/search/?type=police%20departments&state=new-mexico
# https://www.policeone.com/law-enforcement-directory/search/page-{n}/?state={state}&type=police%20departments


url = f'https://www.policeone.com/law-enforcement-directory/search/page-{n}/?state={state}&type=police%20departments'

# takes 'artist' and 'title'
# returns 'title', 'artist', 'year' and 'album_link' for album search for artist and title
def searchy(artist, title, year):
    # process artist and title
    a = texty(artist)
    t = texty(title)

    search = f'{a} {t}'.replace(' ', '+')
    url = f'https://www.allmusic.com/search/albums/{search}'

    r = http.request('GET', url)

    if r.status == 200:
        soup = BeautifulSoup(r.data, 'lxml')
        zults = []
        for d in soup.find_all('div', {'class':'info'}):
            entry = {}
            for tag in ['title','artist','year']:
                try:
                    entry[tag] = d.find('div', {'class':tag}).text.strip()
                except AttributeError:
                    entry[tag] = d.find('div', {'class':tag})
                if tag == 'title':
                    entry['album_link'] = d.find('div', {'class':tag}).find('a')['href']
            zults.append(entry)
        return zults
