import requests
from datetime import datetime
import os
from support_funcs import download_photo, get_extension
from dotenv import load_dotenv


def download_nasa_epic_photo(folderpath):
    params = {'api_key': os.getenv('NASA_API_KEY', 'DEMO_KEY')}
    count = os.getenv('COUNT_NASA_EPIC_PHOTOS', 5) 

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
        if i <= count - 1:
            photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{url_date}/png/{image["image"]}.png'
            response = requests.get(photo_url, params=params)
            response.raise_for_status()
            download_photo(folderpath, response.url,
                        f"nasa_epic{i}{get_extension(response.url)}")

if __name__ == '__main__':
    load_dotenv()
    folderpath = os.getenv('FOLDERPATH', 'images')
    download_nasa_epic_photo(folderpath)
