import cv2
import Ditherer as dith
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

found_image = 0
while found_image == 0:
    try:
        file_path = filedialog.askopenfilename()
        image = cv2.imread(file_path)
        found_image = 1
    except:
        print('Incorrect file type. Only accepts pictures.')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ditherer = dith.Steinberg(gray_image)
print('Loading...')
ditherer.dither()
print('Done')
ditherer.show()
