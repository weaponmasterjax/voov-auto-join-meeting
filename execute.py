import os
import pandas as pd
import pyautogui
import time
from datetime import datetime
import cv2
def ScreenshotAndCV(tempFile, whatDo, debug=True):
    pyautogui.screenshot('big.png')
    gray = cv2.imread("big.png",0)
    img_template = cv2.imread(tempFile,0)
    w, h = img_template.shape[::-1]
    res = cv2.matchTemplate(gray,img_template,cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    pyautogui.moveTo(top+h/2, left+w/2)
    whatDo(x)

    if debug:
        img = cv2.imread("big.png",1)
        cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
        cv2.imshow("processed",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    os.remove("big.png")
    
def signIn(meeting_id):
    '''
    Enter meeting NO. and join；
    '''
    # Start voov
    os.startfile("C:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe")
    time.sleep(10)# wait for start
    ScreenshotAndCV("joinbtn.png", pyautogui.click, False)
    time.sleep(1)# get a screenshot to find buttons
    ScreenshotAndCV("meeting_id.png", pyautogui.click, False)
    pyautogui.write(meeting_id)
    ScreenshotAndCV("final.png", pyautogui.click, False)
    if password_exsist==True:
        ScreenshotAndCV("passwordbox.png", pyautogui.click, False)
        time.sleep(5)
        pyautogui.write(password)
        ScreenshotAndCV("confirmpass.png", pyautogui.click, False)
    time.sleep(2)


while True:
    now = datetime.now().strftime("%H:%M")#dont forget to add 0 before A.M. time!
    password_exsist=True
    debugging=False
    password='334455'
    if now=="13:40" or debugging==True:#here goes your time!
        meeting_id = '703961705'#Your meeting number goes here!
        time.sleep(5)
        signIn(meeting_id)
        print('Joined.')
        break
    time.sleep(40)
