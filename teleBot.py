from config import tokenBOT
from parse import final
import telepot
import pprint
import sys
import time

bot = telepot.Bot(tokenBOT)

def handle(msg):
	global bot
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)
	if content_type == 'text':
		bot.sendMessage(chat_id, msg['text'])
	

def main():
	global bot
	bot.message_loop(handle)

	print ('Listening ...')
	# Keep the program running.
	while 1:
		time.sleep(10)

if __name__ == '__main__':
	main()

# bot = telepot.Bot(tokenBOT)
# bot.message_loop(handle)
# print ('Listening ...')

# Keep the program running.
# while 1:
#     time.sleep(10)
