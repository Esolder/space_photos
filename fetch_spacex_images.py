import requests
from support_funcs import download_photo, get_extension


def fetch_spacex_launch(folderpath, launch):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch}'
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    for i, image in enumerate(images):
        download_photo(folderpath, image, f'spacex_{i}{get_extension(image)}')

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    import argparse

    folderpath = os.getenv('FOLDERPATH', 'images')

    parser = argparse.ArgumentParser(
        description='Загружает фото запуска nasa по указанному id')
    parser.add_argument('--id', help='id запуска')
    launch = parser.parse_args().id
    if not launch:
        launch = 'latest'
    fetch_spacex_launch(folderpath, launch)