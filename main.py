import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import random
# функция для получения ссылок на изображения на странице
def get_image_links(url):
    links = []
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        if src is not None and src.startswith('http'):
            links.append(src)
    return links

# функция для открытия случайного изображения
def open_random_image(url):
    links = get_image_links(url)
    if links:
        image_url = links[random.randint(0, len(links)-1)]
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()
    else:
        print('No images found on the page')

# пример использования функций
url = 'https://www.google.com/search?q=cats&tbm=isch'
open_random_image(url)
