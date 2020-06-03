#!/usr/bin/env python
from selenium import webdriver
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings('ignore')

record = []

url = 'https://www.worldometers.info/'
table = 'counterdiv'
targets = {
            'world_population': 'current_population',
            'year_births': 'births_this_year',
            'today_births': 'births_today',
            'year_deaths': 'dth1s_this_year',
            'today_deaths': 'dth1s_today'
        }

driver = webdriver.PhantomJS()
driver.get(url)
secction = driver.find_element_by_class_name(table)
index = secction.get_attribute('innerHTML')

parse = BeautifulSoup(index, 'lxml')

for tag in targets.values():
    value = parse.find('span', attrs={'rel': tag}).text
    format_value = value.replace(',', '')
    record.append(int(format_value))
