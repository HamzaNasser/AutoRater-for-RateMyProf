import cv2

import pyautogui as pa

import time 

import keyboard as ky

while ky.is_pressed('q') != True:

	if pa.locateOnScreen("like.png", confidence=0.9) != None:
		print("I can see it sir")
		x,y = pa.locateCenterOnScreen("like.png", confidence=0.6)
		pa.click(x,y)
		pa.click(1907, 1020)
		time.sleep(1)
	if pa.locateOnScreen("like.png") != None:
		x,y = pa.locateCenterOnScreen("like.png", confidence=0.8)
		pa.click(x,y)
		pa.click(1907, 1020)
		time.sleep(1)

	else:
		print("I dont see it ")
		time.sleep(1)