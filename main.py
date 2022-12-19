import os
import pandas as pd
import pyautogui
import time
from datetime import datetime
import cv2
import platform
'''
V1.0
'''


def ScreenshotAndCV(tempFile, whatDo, debug=True):
    pyautogui.screenshot('./resource/big.png')
    gray = cv2.imread("./resource/big.png", 0)
    img_template = cv2.imread(tempFile, 0)
    w, h = img_template.shape[::-1]
    res = cv2.matchTemplate(gray, img_template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    pyautogui.moveTo(top+h/2, left+w/2)
    whatDo(x)

    if debug:
        img = cv2.imread("./resource/big.png", 1)
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5,
                         interpolation=cv2.INTER_NEAREST)
        cv2.imshow("processed", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    os.remove("./resource/big.png")


def signIn(meeting_id):
    '''
    Enter meeting NO. and join；
    '''
    # Start voov
    os.startfile("C:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe")
    time.sleep(10)  # wait for start
    ScreenshotAndCV("./resource/joinbtn.png", pyautogui.click, False)
    time.sleep(1)  # get a screenshot to find buttons
    ScreenshotAndCV("./resource/meeting_id.png", pyautogui.click, False)
    pyautogui.write(meeting_id)
    ScreenshotAndCV("./resource/final.png", pyautogui.click, False)
    if password_exsist == True:
        ScreenshotAndCV("./resource/passwordbox.png", pyautogui.click, False)
        time.sleep(5)
        pyautogui.write(password)
        ScreenshotAndCV("./resource/confirmpass.png", pyautogui.click, False)
    time.sleep(2)


'''
Check whether wemeetapp is already started and kill it to avoid conflicts
'''


def Checkanddowemeet():
    if platform.system() == 'Windows':
        os.system("taskkill /f /im wemeetapp.exe")
    elif platform.system() == 'linux':
        os.system("pkill wemeetapp*")


while True:
    # dont forget to add 0 before A.M. time!
    now = datetime.now().strftime("%H:%M")
    password_exsist = False
    debugging = True
    password = '666666'  # meeting room password goes here
    if now == "13:40" or debugging == True:  # here goes your time!
        meeting_id = '6666666666'  # Your meeting number goes here!
        time.sleep(5)
        signIn(meeting_id)
        print('Joined.')
        break
    time.sleep(40)
