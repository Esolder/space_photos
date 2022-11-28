import telegram
import os
from dotenv import load_dotenv
load_dotenv()

bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
print(bot.get_me())
# bot.send_message(chat_id='@dvmn_lesson_space_photos', text="I'm sorry Dave I'm afraid I can't do that.")
bot.send_photo(photo=open('images/hubble.jpeg', 'rb'), chat_id='@dvmn_lesson_space_photos')
