import numpy as np
import cv2
import random

def findClosest2Tone(pixel_value):
    """
    Given a pixel_value (int from 0-255), return the 0 or 255, whichever is closer
    as well as the distance from that value.
    """
    diff = abs(255-pixel_value)
    if diff < pixel_value:
        return 255, -diff
    return 0, pixel_value

def findClosest(pixel_value, palette):
    """
    Given a palette (an array of rgb values stored as tuples or lists) and a
    pixel value (tuple or list of rgb values), return the closest color in the palette
    and the distance of each rgb value in pixel_value from that color.
    """
    error_array, total_array = [], []
    i = 0
    for color in palette:
        error_array.append([])
        for channel_index in range(len(pixel_value)):
            error_array[i].append(pixel_value[channel_index]-color[channel_index])
        total_error = 0
        for error in error_array[i]:
            total_error += abs(float(error))
        total_array.append(total_error)
        i += 1
    min_index = total_array.index(min(total_array))
    return palette[min_index], error_array[min_index]

class Steinberg:
    def __init__(self, image):
        self.image = image
        self.width, self.height = self.image.shape[0], self.image.shape[1]
        self.divisor = 16.0

        # The error diffusion values
        self.MR = 7.0
        self.BL = 3.0; self.BM = 5.0; self.BR = 1.0

    def convert2Gray(self):
        """
        Convert image to gray. (For use in two-tone dithering)
        """
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def dither2Tone(self):
        """
        Apply a Steinberg dither using only black and white for the palette.
        """
        print('\nLoading...')
        self.convert2Gray()
        error_array = np.zeros((self.width, self.height))
        for y in range(self.height):
            for x in range(self.width):
                pixel_value = self.image[x, y] + error_array[x][y]
                pixel_value, error = findClosest2Tone(pixel_value)
                self.image[x, y] = pixel_value
                error = float(error)
                try:
                    error_array[x+1, y] = self.MR / self.divisor * error
                except:
                    pass
                try:
                    error_array[x-1, y+1] = self.BL / self.divisor * error
                except:
                    pass
                try:
                    error_array[x, y+1] = self.BM / self.divisor * error
                except:
                    pass
                try:
                    error_array[x+1, y+1] = self.BR / self.divisor * error
                except:
                    pass

    def generateRandomPalette(self, colors=8):
        """
        Given the number of colors to generate, generate a random palette of colors.
        """
        self.palette = []
        for i in range(colors):
            self.palette.append((random.randint(0, 255), random.randint(0,255),random.randint(0,255)))

    def generateSelectivePalette(self, colors=8):
        """
        Given the number of colors to generate, generate a palette of colors by taking
        random points on the original image and getting their rgb values.
        """
        self.palette = []
        for i in range(colors):
            pixel = self.image[random.randint(0, self.width-1), random.randint(0, self.height-1)]
            self.palette.append((pixel[0], pixel[1], pixel[2]))

    def choosePalette(self):
        """
        Get the user's choice for generating a palette.
        """
        options = ['1', '2']
        choice = ''
        while choice not in options:
            print('\t1. Random Palette')
            print('\t2. Selective Palette')
            choice = input('Choice: ')
        if choice == '1':
            num_colors = int(input('Number of colors to generate: '))
            self.generateRandomPalette(num_colors)
        elif choice == '2':
            num_colors = int(input('Number of colors to generate: '))
            self.generateSelectivePalette(num_colors)

    def dither(self):
        """
        Apply a Steinberg dither on the class's image. The image is overwritten.
        """
        self.choosePalette()
        print('\nLoading...')
        error_array = np.zeros((self.width, self.height, 3))
        for y in range(self.height):
            for x in range(self.width):
                pixel = self.image[x, y]
                pixel_value = [pixel[0], pixel[1], pixel[2]]
                for i in range(len(pixel_value)):
                    pixel_value[i] += error_array[x][y][i]
                pixel_value, error = findClosest(pixel_value, self.palette)
                self.image[x, y] = pixel_value
                try:
                    for channel_index in range(len(error_array[x+1, y])):
                        error_array[x+1, y][channel_index] = self.MR / self.divisor * error[channel_index]
                except:
                    pass
                try:
                    for channel_index in range(len(error_array[x-1, y+1])):
                        error_array[x-1, y+1][channel_index] = self.BL / self.divisor * error[channel_index]
                except:
                    pass
                try:
                    for channel_index in range(len(error_array[x, y+1])):
                        error_array[x, y+1][channel_index] = self.BM / self.divisor * error[channel_index]
                except:
                    pass
                try:
                    for channel_index in range(len(error_array[x+1, y+1])):
                        error_array[x+1, y+1][channel_index] = self.BR / self.divisor * error[channel_index]
                except:
                    pass


    def show(self):
        """
        Display the class's current image in cv2.
        """
        cv2.imshow('New Image', self.image)
        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
        elif k == ord('s'):
            cv2.imwrite('dither.png', self.image)
            cv2.destroyAllWindows()
            print('Saved "dither.png" to home folder.')
            input('Press any key to end process...')