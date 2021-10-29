from bs4 import BeautifulSoup
import requests
import re

def remove_duplicates(plugins_list):
    res = []
    for i in plugins_list:
        if i not in res:
            res.append(i)
    return res

url = input('Enter the url of the website : ')
if (url.startswith('http')):
    pass
else:
    url = 'http://' + url

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

plugins_list = []

#To find the plugins installed in the wordpress site.

for tags in soup.find_all("link"):
    href_string = tags.get('href')
    if 'wp-content/plugins/' in href_string:   
        href_elements_list = href_string.split('/')
        index = href_elements_list.index('plugins')
        plugin_name = href_elements_list[index+1]
        plugins_list.append(plugin_name)

final_plugins_list = remove_duplicates(plugins_list)
print(final_plugins_list)
