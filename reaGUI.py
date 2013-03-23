#coding=utf-8
from reaper_python import *
import win32api, win32gui, win32con
from ctypes import windll as windll
import sys
from api import *

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
        self.hi_there = Button(self)
        self.hi_there["text"] = "Show Line Index"
        self.hi_there["command"] = self.displayMessage1
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.reaHWND=RPR_GetMainHwnd()

    def displayMessage1(self):
        RPR_CSurf_OnPlay()
        #窗口的类名
        self = 'SE_SogouExplorerFrame'
        #通过窗口类名获取窗口句柄
        # hwnd = win32gui.FindWindow(self, None)
        #send key
        hwnd = 0x0005080E
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_NUMPAD9, 0)#发送F9键
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_NUMPAD9, 0)
        printf('send')


    def keyPressed(self, event):
        printf('keyPressed' + str(self.reaHWND))
        hwnd=0x0003065E
        win32api.PostMessage(0x0003065E, win32con.WM_KEYDOWN, event.keycode, 0)#发送F9键


if __name__ == '__main__':
    root = Tkinter.Tk()
    app = Application(master=root)
    root.bind_all('<Key>', app.keyPressed)
    app.mainloop()
