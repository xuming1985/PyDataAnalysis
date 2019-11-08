import requests
import json
import csv
from urllib.parse import urlencode
import time

def saveHtml(file_name, file_content):
    with open(file_name.replace('/','_')+'.html','wb') as f:
        f.write(file_content)

def getData(url, writer):
    response = requests.get(url)
    data = response.content
    