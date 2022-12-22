import argparse
import os
import random

import telegram

from support_funcs import get_files_paths


def publish_in_telegram(photo_name, folderpath, telegram_bot, chat_id):
    if photo_name is None:
        photo_names = get_files_paths(folderpath)
        photo_name = random.choice(photo_names)

    with open(photo_name, 'rb') as ph:
        telegram_bot.send_photo(photo=ph, chat_id=chat_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Публикует фото в Telegram канал')
    parser.add_argument('--photo', help='Имя фотографии')
    args = parser.parse_args()

    folderpath = os.environ['FOLDERPATH']
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    publish_in_telegram(args.photo, folderpath, bot, chat_id)
