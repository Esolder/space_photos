import requests
from support_funcs import download_photo, get_extension


def fetch_spacex_launch(folderpath):
    spacex_url = 'https://api.spacexdata.com/v3/launches/76'
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()['links']['flickr_images']
    for i, image in enumerate(images):
        download_photo(folderpath, image, f'spacex_{i}{get_extension(image)}')

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    folderpath = os.getenv('FOLDERPATH', 'images')
    fetch_spacex_launch(folderpath)