import numpy as np
import cv2

def findClosest(pixel_value):
    diff = abs(255-pixel_value)
    if diff < pixel_value:
        return 255, -diff
    return 0, pixel_value

class Steinberg:
    def __init__(self, image):
        self.image = image
        self.width, self.height = self.image.shape[0], self.image.shape[1]
        self.divisor = 16.0

        # The error diffusion values
        self.MR = 7.0
        self.BL = 3.0; self.BM = 5.0; self.BR = 1.0

    def dither(self):
        error_array = np.zeros((self.width, self.height))
        for y in range(self.height):
            for x in range(self.width):
                pixel_value = self.image[x, y] + error_array[x][y]
                pixel_value, error = findClosest(pixel_value)
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

    def blackAndWhite(self):
        pass

    def show(self):
        cv2.imshow('Dithered', self.image)
        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
        elif k == ord('s'):
            cv2.imwrite('dither.png', self.image)
            cv2.destroyAllWindows()
            print('Saved "dither.png" to home folder.')
            input('Press any key to end process...')