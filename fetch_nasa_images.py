import requests
import os
from support_funcs import download_photo, get_extension
from dotenv import load_dotenv
load_dotenv()


def download_nasa_photos(folderpath):
    params = {'api_key': os.getenv('NASA_API_KEY', 'DEMO_KEY'), 'count': 30}

    nasa_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()

    for i, image in enumerate(response.json()):
        download_photo(folderpath, image['hdurl'],
                       f"nasa_{i}{get_extension(image['url'])}")


if __name__ == '__main__':
    folderpath = os.getenv('FOLDERPATH', 'images')
    download_nasa_photos(folderpath)
