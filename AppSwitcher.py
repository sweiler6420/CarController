import keyboard  # using module keyboard
import win32gui, win32con
import os
import math
import time

os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad")
time.sleep(2)
notepad = win32gui.GetForegroundWindow()
os.startfile(r"C:\Users\sweil\OneDrive\Documents\Vehicles\Projects\Porsche\HeadUnit\Apps\RunAndroidAuto.vbs")
time.sleep(2)
androidAuto = win32gui.GetForegroundWindow()

keyboard.add_hotkey("a", lambda: maxAndroidAuto())
keyboard.add_hotkey("b", lambda: maxNotepad())

def maxAndroidAuto():
    win32gui.ShowWindow(notepad, win32con.SW_MINIMIZE)
    win32gui.ShowWindow(androidAuto, win32con.SW_MAXIMIZE)

def maxNotepad():
    win32gui.ShowWindow(androidAuto, win32con.SW_MINIMIZE)
    win32gui.ShowWindow(notepad, win32con.SW_MAXIMIZE)

while True:
    pass


    
    





