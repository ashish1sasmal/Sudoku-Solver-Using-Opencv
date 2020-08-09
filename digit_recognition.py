from PIL import Image
import pytesseract
import cv2
import numpy as np
import os
import sys


def digits(image):
    concateImg = np.concatenate((image, image), axis = 1)
    concateImg = np.concatenate((concateImg, image), axis = 1)
    concateImg = np.concatenate((concateImg, image), axis = 1)
    concateImg = np.concatenate((concateImg, image), axis = 1)
    concateImg = np.concatenate((concateImg, image), axis = 1)
    concateImg = np.concatenate((concateImg, image), axis = 1)


    gray = cv2.cvtColor(concateImg, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(concateImg)
    # cv2.imshow("Out",concateImg)
    # k = cv2.waitKey(0)
    if text=="":
        text=0
    else:
        text = int(text[-1])
        # if k==27:
        #     sys.exit()
    # print(text)
    return(text)
