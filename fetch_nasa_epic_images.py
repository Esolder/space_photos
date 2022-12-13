from datetime import datetime
import os
from support_funcs import download_photo, get_extension, get_response
from dotenv import load_dotenv
from urllib.parse import urljoin


def download_nasa_epic_photos(folderpath, count_download_photo, base_url, params):
    last_date = get_last_photo_date(params, base_url)
    photo_info = get_photo_info(params, last_date)
    url_date = get_url_date(last_date)
    for i, image in enumerate(photo_info):
        if i < count_download_photo:
            photo_url = f'/EPIC/archive/natural/{url_date}/png/{image["image"]}.png'
            response = get_response(base_url, photo_url, params=params)
            download_photo(folderpath,
                           response.url,
                           f"nasa_epic{i}{get_extension(response.url)}")


def get_last_photo_date(params, base_url):
    dates_path = '/EPIC/api/natural/all'
    response = get_response(base_url, dates_path, params=params)
    last_date = response.json()[0]['date']
    return last_date


def get_photo_info(params, date):
    photos_path = f'/EPIC/api/natural/date/{date}'
    response = get_response(base_url, photos_path, params=params)
    return response.json()


def get_url_date(last_date):
    full_date = datetime.strptime(last_date, f'%Y-%m-%d')
    return full_date.strftime(f'%Y/%m/%d')


if __name__ == '__main__':
    load_dotenv()

    folderpath = os.getenv('FOLDERPATH', 'images')
    count_download_photo = int(os.getenv('COUNT_NASA_EPIC_PHOTOS', 5))
    params = {'api_key': os.getenv('NASA_API_KEY', 'DEMO_KEY')}

    base_url = 'https://api.nasa.gov'

    download_nasa_epic_photos(folderpath,
                              count_download_photo,
                              base_url,
                              params)
