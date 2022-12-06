import telegram
import os
from dotenv import load_dotenv
from random import shuffle
import time

def publish_in_telegram():
    load_dotenv()

    folderpath = os.getenv('FOLDERPATH')
    delay_hours = int(os.getenv('DELAY_HOURS', 4))

    bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
    chat_id=os.getenv('TELEGRAM_CHAT_ID')

    while True:
        photos = os.listdir(folderpath)
        shuffle(photos)
        for photo in photos:
            bot.send_photo(photo=open(f'{folderpath}/{photo}', 'rb'),
                           chat_id=chat_id)
            time.sleep(delay_hours * 3600)


if __name__ == '__main__':
    publish_in_telegram()
