import urllib
import os
from pathlib import Path
import requests
from urllib.parse import urljoin


def download_photo(folderpath, photo_url, filename):
    Path(folderpath).mkdir(parents=True, exist_ok=True)

    response = requests.get(photo_url)
    response.raise_for_status()

    with open(Path(('folderpath'), ('filename')), 'wb') as file:
        file.write(response.content)


def get_extension(url):
    path = urllib.parse.urlsplit(url).path
    filepath, filename = os.path.split(path)
    name, extension = os.path.splitext(filename)
    return extension

def get_response(base_url, path, params=None):
    url = urljoin(base_url, path)
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response
