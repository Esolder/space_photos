from fetch_spacex_images import fetch_spacex_launch
from fetch_nasa_images import download_nasa_photos
from fetch_nasa_epic_images import download_nasa_epic_photo


def main():
    photo_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    filename = 'hubble.jpeg'
    folderpath = 'images'

    # download_photo(folderpath, photo_url, filename)

    fetch_spacex_launch(folderpath)

    download_nasa_photos(folderpath)

    download_nasa_epic_photo(folderpath)

if __name__ == '__main__':
    main()
