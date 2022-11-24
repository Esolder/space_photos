import urllib
import os
import pathlib
import requests


def download_photo(folderpath, photo_url, filename):
    pathlib.Path(folderpath).mkdir(parents=True, exist_ok=True)

    response = requests.get(photo_url)
    response.raise_for_status()

    with open(f'{folderpath}/{filename}', 'wb') as file:
        file.write(response.content)


def get_extension(url):
    path = urllib.parse.urlsplit(url).path
    filepath, filename = os.path.split(path)
    name, extension = os.path.splitext(filename)
    return extension

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    folderpath = os.getenv('FOLDERPATH', 'images')
    
    photo_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    filename = 'hubble.jpeg'
    download_photo(folderpath, photo_url, filename)
