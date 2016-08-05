import numpy as np
from PIL import Image
import sys
import time

resize_h = 20
resize_w = resize_h/2
grey_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@'][::-1]

class transformImage():
    def pre_process_img(self, img):
        # greyscale image
        x = Image.open(img, 'r')
        x = x.convert('L') # make it greyscale
        y = np.asarray(x.getdata(),dtype=np.uint16).reshape((x.size[1],x.size[0]))
        # print y.shape
        return y

    def select_char(self, grey_val, if_white):
        global grey_chars
        if grey_val == 255: grey_level = len(grey_chars) -1
        else: grey_level = int(float(grey_val)/(255./float(len(grey_chars))))
        if if_white:
            return grey_chars[grey_level]
        else:
            return grey_chars[len(grey_chars)-1-grey_level]

    def greyscale_to_ascii(self, y):
        # since the image has way more pixels than the number of characters should be
        # used in ascii representation, scaling the image while preseving the aspect is
        # needed.
        global resize_h, resize_w
        result_white = []
        result_black = []
        # resize_h is the rescaling ratio of height
        # resize_w is the rescaling ratio of width
        for h in range(resize_h-1, y.shape[0], resize_h):
            row_white = []
            row_black = []
            for w in range(resize_w-1, y.shape[1], resize_w):
                new_px = 0
                # get the avg val of a chunk of pixels of size (resize_h * resize_w)
                for sub_h in range(h, h-resize_h, -1):        
                    for sub_w in range(w, w-resize_w, -1):
                        new_px += y[sub_h][sub_w]
                new_px /= resize_h*resize_w

                if new_px < 0: new_px = 0       # double check the new val is within range
                elif new_px > 255: new_px = 255
                
                row_white.append(self.select_char(new_px, True))
                row_black.append(self.select_char(new_px, False))
            result_white.append(row_white)
            result_black.append(row_black)
        return [result_white, result_black] # two versions of ascii art