import argparse
import os
import random

import telegram


def publish_in_telegram(photo_name):
    folderpath = os.environ.get('FOLDERPATH')
    bot = telegram.Bot(token=os.environ.get('TELEGRAM_TOKEN'))
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')

    if photo_name is None:
        photo_names = []
        for root, dirs, files in os.walk(folderpath):
            for name in files:
                photo_names.append(os.path.join(root, name))
        photo_name = random.choice(photo_names)

    with open(photo_name, 'rb') as ph:
        bot.send_photo(photo=ph, chat_id=chat_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Публикует фото в Telegram канал')
    parser.add_argument('--photo', help='Имя фотографии')

    args = parser.parse_args()

    publish_in_telegram(photo_name=args.photo)
