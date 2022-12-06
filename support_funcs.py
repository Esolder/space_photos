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
