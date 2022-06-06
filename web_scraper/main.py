# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 09:31:33 2022

@author: Linh
"""

import requests
from bs4 import BeautifulSoup
import time

def find_jobs():
    # Getting page HTML through request
    page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(page, 'lxml') # Parsing content using beautifulsoup
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if '2' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            link = job.header.h2.a['href']
        
            with open(f'job_postings/{index}.txt', 'w') as f:
                
                f.write(f'Company Name: {company_name.strip()} \n')
                f.write(f'Required Skills: {skills.strip()} \n')
                f.write(f'Job Link: {link}')
            
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 24 # Runs program every 24 hours
        print(f'Waiting {time_wait} hours...')
        time.sleep(time_wait * 3600)