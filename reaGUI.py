#coding=utf-8
from reaper_python import *
import win32api, win32gui, win32con
from ctypes import windll as windll
import sys

sys.argv = ["Main"]

user32 = windll.user32
kernel32 = windll.kernel32

def console_msg(*msg):
    RPR_ShowConsoleMsg(str(msg) + '\n' + '\n')


import Tkinter
from Tkinter import *


class Application(Tkinter.Frame):
    def AddEnv(self):
        pass

    def createWidgets(self):
        self.lb = Listbox(self)
        self.lb.insert(END, '1', '2', '3')
        self.lb.bind("<Double-Button-1>", self.ok)
        self.lb.pack()

        self.hi_there = Button(self)
        self.hi_there["text"] = "Show Line Index"
        self.hi_there["command"] = self.displayMessage1
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def displayMessage1(self):
        RPR_CSurf_OnPlay()


    def ok(self, event):
        RPR_CSurf_OnPlay()


if __name__ == '__main__':
    #窗口的类名
    self = 'SE_SogouExplorerFrame'
    #通过窗口类名获取窗口句柄
    # hwnd = win32gui.FindWindow(self, None)
    #send key
    hwnd = 0x0001032E
    user32.SendMessageA
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_NUMPAD0, 0)#发送F9键
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_NUMPAD0, 0)
# root = Tkinter.Tk()
# app = Application(master=root)
# app.mainloop()
