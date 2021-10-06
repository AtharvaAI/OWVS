from bs4 import BeautifulSoup
import re
import requests

url = input('Enter the url of the website (Make sure to append http at the start): ')
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
for meta_tags in soup.find_all("meta"):
    if(meta_tags.get("name") == 'generator'):
        print(meta_tags.get("content"))
