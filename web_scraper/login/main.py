# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:25:59 2022

@author: Linh
"""

import requests
from bs4 import BeautifulSoup
import creds

login_url = ('https://the-internet.herokuapp.com/authenticate')
secure_url = ('https://the-internet.herokuapp.com/secure')

credentials = {
    'username': creds.username,
    'password': creds.password
    }

with requests.session() as s:
    s.post(login_url, data=credentials)
    r = s.get(secure_url)
    soup = BeautifulSoup(r.content, 'html.parser')
#    print(soup.prettify())
    test = soup.find('h4', class_='subheader').text
    print(test)