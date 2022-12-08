import telegram
import os
from dotenv import load_dotenv
from random import shuffle
import time


def publish_in_telegram():
    load_dotenv()

    folderpath = os.environ('FOLDERPATH')
    delay_seconds = int(os.getenv('DELAY_SECONDS', 14400))

    bot = telegram.Bot(token=os.environ('TELEGRAM_TOKEN'))
    chat_id = os.environ('TELEGRAM_CHAT_ID')

    while True:
        for root, dirs, files in os.walk(folderpath):
            shuffle(files)
            for file in files:
                with open(os.path.join(folderpath, file), 'rb') as ph:
                    bot.send_photo(photo=ph, chat_id=chat_id)
                time.sleep(delay_seconds)


if __name__ == '__main__':
    publish_in_telegram()
