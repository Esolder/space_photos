import requests
import pathlib
import os
import urllib

from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


def main():
    photo_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    filename = 'hubble.jpeg'
    folderpath = 'images'

    # download_photo(folderpath, photo_url, filename)

    # fetch_spacex_launch(folderpath)

    # download_nasa_photos(folderpath)

    download_nasa_epic_photo(folderpath)


def download_photo(folderpath, photo_url, filename):
    pathlib.Path(folderpath).mkdir(parents=True, exist_ok=True)

    response = requests.get(photo_url)
    response.raise_for_status()

    with open(f'{folderpath}/{filename}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(folderpath):
    spacex_url = 'https://api.spacexdata.com/v3/launches/76'
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()['links']['flickr_images']
    for i, image in enumerate(images):
        download_photo(folderpath, image, f'spacex_{i}{get_extension(image)}')


def get_extension(url):
    path = urllib.parse.urlsplit(url).path
    filepath, filename = os.path.split(path)
    name, extension = os.path.splitext(filename)
    return extension


def download_nasa_photos(folderpath):
    params = {'api_key': os.getenv('NASA_API_KEY'), 'count': 30}

    nasa_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()

    for i, image in enumerate(response.json()):
        download_photo(folderpath, image['hdurl'],
                       f"nasa_{i}{get_extension(image['url'])}")


def download_nasa_epic_photo(folderpath):
    params = {'api_key': os.getenv('NASA_API_KEY'), 'count': 5}

    dates_url = 'https://api.nasa.gov/EPIC/api/natural/all'
    response = requests.get(dates_url, params=params)
    response.raise_for_status()

    last_date = response.json()[0]['date']
    full_date = datetime.strptime(last_date, f'%Y-%m-%d')
    url_date = full_date.strftime(f'%Y/%m/%d')

    nasa_epic_url = f'https://api.nasa.gov/EPIC/api/natural/date/{last_date}'
    response = requests.get(nasa_epic_url, params=params)
    response.raise_for_status()

    for i, image in enumerate(response.json()):
        photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{url_date}/png/{image["image"]}.png'
        response = requests.get(photo_url, params=params)
        response.raise_for_status()
        download_photo(folderpath, response.url,
                       f"nasa_epic{i}{get_extension(response.url)}")


if __name__ == '__main__':
    main()
