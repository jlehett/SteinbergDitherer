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

ditherer = dith.Steinberg(image)
options = ['1', '2']
choice = ''
print('Choose dithering method: ')
while choice not in options:
    print('\t1. Two-Tone')
    print('\t2. RGB')
    choice = input('Choice: ')
if choice == '1':
    ditherer.dither2Tone()
elif choice == '2':
    ditherer.dither()
print('Done')
ditherer.show()