from bs4 import BeautifulSoup
import requests


import json

def find(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    cats = []
    grid = soup.find('div', class_='adopt-a-pet-grid')
    try:
        for i, div in enumerate(grid.find_all('div', class_='adopt-a-pet-item')):
            h4_text = div.find('h4').text
            location_text = div.find('div', class_='aap-location').text
            img = div.find('img', {'src': lambda x: 'https://pet-uploads.adoptapet.com' in x})
            url = div.find('a', {
                'href': lambda x: x and x.startswith("https://petsmartcharities.org/adopt-a-pet/find-a-pet/results")})[
                'href']

            if img:
                cat = {
                "number": i,
                "image_src": img["src"],
                "name": h4_text,
                "location": location_text,
                "URL": url,
                }
                cats.append(cat)
            else:
                cat = {
                "number": i,
                "ERROR": "No image found"
                }
            cats.append(cat)
    except:
        cat = {
            "ERROR": "No Breeds Found"
        }
        cats.append(cat)
    return json.dumps(cats)
