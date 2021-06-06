import time
import requests
import re
import json
import os
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def WaitForChild(driver, XPath):
    Child = None
    while True:
        try:
            Child = driver.find_element_by_xpath(XPath)
            break
        except Exception as e:
            print(e)
            time.sleep(0.1)
    return Child

def ButtonClick(Button):
    while True:
        try:
            Button.click()
            break
        except Exception as e:
            time.sleep(.2)
    return True
        
def Bypass(Url, Shit):
    driver = webdriver.Chrome()

    driver.get(Url)
    os.system("cls")

    ACCESS_BTN = WaitForChild(driver, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/lv-redirect-first-page/lv-countdown-block/div/div/div/div[2]/div/div[2]/div/lv-button')
    DISCOVER_BTN = WaitForChild(driver, ' /html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/lv-redirect-second-page/lv-todo-block/div/div/div[3]/div/div[1]/div')
    CLOSE_BTN = WaitForChild(driver, '//*[@id="webModal"]/div/div/div[1]/div[2]/div/a')
    CONTINUE_BTN = WaitForChild(driver, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/lv-redirect-second-page/lv-todo-block/div/div/div[3]/div/div[3]/lv-button')

    print("Access Button | ...")
    ButtonClick(ACCESS_BTN)
    print("Access Button | OK")
    time.sleep(1)
    print("Discover Button | ...")
    ButtonClick(DISCOVER_BTN)
    print("Discover Button | OK")
    time.sleep(12)
    print("Access Button | ...")
    ButtonClick(CLOSE_BTN)
    print("Access Button | OK")
    time.sleep(1)
    print("Continue Button | ...")
    ButtonClick(CONTINUE_BTN)
    print("Continue Button | OK")
    print("Everything done :D")

    ################################################################################################
    ##  FREE ACCESS | /html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/lv-redirect-first-page/lv-countdown-block/div/div/div/div[2]/div/div[2]/div/lv-button
    ##  DISCOVER    | /html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/lv-redirect-second-page/lv-todo-block/div/div/div[3]/div/div[1]/div
    ##  CLOSE       | //*[@id="webModal"]/div/div/div[1]/div[2]/div/a
    ##  CONTINUE    | /html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/lv-redirect-second-page/lv-todo-block/div/div/div[3]/div/div[3]/lv-button
    ################################################################################################

# Very Important
# playsound.playsound('C:/Users/https/OneDrive/Skrivbord/PythonSelenium/sus.mp3', True)

Bypass("URL HERE", "Kiko was here!")
