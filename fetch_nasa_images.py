import argparse
import os
import requests

from support_funcs import download_photo, get_extension
from dotenv import load_dotenv


def download_nasa_photos(folderpath, count):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': os.getenv('NASA_API_KEY', 'DEMO_KEY'),
              'count': count if count else 10}

    response = requests.get(nasa_url, params=params)
    response.raise_for_status()

    for i, launch_info in enumerate(response.json()):
        if launch_info['media_type'] == 'image':
            try:
                image_url = launch_info['hdurl']
            except KeyError:
                image_url = launch_info['url']
            download_photo(folderpath, image_url,
                        f"nasa_{i}{get_extension(image_url)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int,
                        help="количество фото для загрузки")
    args = parser.parse_args()

    load_dotenv()
    folderpath = os.getenv('FOLDERPATH', 'images')
    download_nasa_photos(folderpath, args.count)
