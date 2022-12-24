import os
from dotenv import load_dotenv
from random import shuffle
import time
from urllib3.exceptions import HTTPError

import telegram

from support_funcs import get_files_paths


def publish_in_telegram(folderpath, delay_seconds, telegram_bot, chat_id):
    while True:
        filepaths = get_files_paths(folderpath)
        shuffle(filepaths)
        for filepath in filepaths:
            with open(filepath, 'rb') as ph:
                try:
                    telegram_bot.send_photo(photo=ph, chat_id=chat_id)
                    connection_error = False
                except (telegram.error.TimedOut, telegram.error.NetworkError):
                    if not connection_error:
                        connection_error = True
                        continue
                    else:
                        print('Connection error. Retrying in 5 seconds')
                        time.sleep(5)
                        continue
                time.sleep(delay_seconds)


if __name__ == '__main__':
    load_dotenv()

    folderpath = os.getenv('FOLDERPATH', 'images')
    delay_seconds = int(os.getenv('DELAY_SECONDS', '14400'))
    telegram_bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    publish_in_telegram(folderpath, delay_seconds, telegram_bot, chat_id)
