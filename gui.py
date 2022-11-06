# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 21:46:17 2022

@author: Master Zhang
"""

import pyautogui

import time
import webbrowser

def get_html():
    url='https://blog.csdn.net/weixin_44791964/article/details/113682561'

    webbrowser.open_new(url) #Open webpage in default browser (firefox)

    time.sleep(3)

    pyautogui.hotkey('ctrl', 's')

    time.sleep(5)

    pyautogui.press('enter')

get_html()