import requests
from support_funcs import download_photo, get_extension, get_response


def fetch_spacex_launch(folderpath, launch):
    base_url = 'https://api.spacexdata.com'
    path = f'/v5/launches/{launch}'
    response = get_response(base_url, path)
    images = response.json()['links']['flickr']['original']
    for img_index, image in enumerate(images):
        download_photo(folderpath,
                       image,
                       f'spacex_{img_index}{get_extension(image)}')


if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    import argparse

    parser = argparse.ArgumentParser(
        description='Загружает фото запуска nasa по указанному id')
    parser.add_argument('--id', help='id запуска', default='latest')
    launch = parser.parse_args().id

    load_dotenv()

    folderpath = os.getenv('FOLDERPATH', 'images')

    fetch_spacex_launch(folderpath, launch)
