import argparse
import os
import requests

from support_funcs import download_photo, get_extension, get_response
from dotenv import load_dotenv


def download_nasa_photos(folderpath, params):
    base_url = 'https://api.nasa.gov'
    path = '/planetary/apod'

    response = get_response(base_url, path, params)

    for img_index, launch_info in enumerate(response.json()):
        if launch_info['media_type'] == 'image':
            try:
                image_url = launch_info['hdurl']
            except KeyError:
                image_url = launch_info['url']
            download_photo(folderpath, image_url,
                           f"nasa_{img_index}{get_extension(image_url)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int,
                        help="количество фото для загрузки",
                        default=10)
    args = parser.parse_args()

    load_dotenv()
    folderpath = os.getenv('FOLDERPATH', 'images')
    params = {'api_key': os.getenv('NASA_API_KEY', 'DEMO_KEY'),
              'count': args.count}

    download_nasa_photos(folderpath, params)
