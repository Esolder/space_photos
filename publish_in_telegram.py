import telegram
import os
from dotenv import load_dotenv
from random import shuffle
import time


def publish_in_telegram(folderpath, delay_seconds, telegram_bot, chat_id):
    while True:
        for root, dirs, files in os.walk(folderpath):
            shuffle(files)
            for file in files:
                with open(os.path.join(folderpath, file), 'rb') as ph:
                    try:
                        telegram_bot.send_photo(photo=ph, chat_id=chat_id)
                        connection_error = False
                    except ConnectionError:
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

    folderpath = os.environ['FOLDERPATH']
    delay_seconds = int(os.getenv('DELAY_SECONDS', 14400))
    telegram_bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    publish_in_telegram(folderpath, delay_seconds, telegram_bot, chat_id)
