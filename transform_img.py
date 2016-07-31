from data import *
import numpy as np
from PIL import Image
import sys
import time
resize_h = 20
resize_w = resize_h/2

class transformImage():
    def pre_process_img(self, img):
        # greyscale image
        x = Image.open(img, 'r')
        x = x.convert('L') # make it greyscale
        y = np.asarray(x.getdata(),dtype=np.uint16).reshape((x.size[1],x.size[0]))
        # print y.shape
        return y

    def select_char(self, grey_val):
        if grey_val == 255: grey_level = len(grey_chars) -1
        else: grey_level = int(float(grey_val)/(255./float(len(grey_chars))))
        return grey_chars[grey_level]

    def greyscale_to_ascii(self, y):
        # since the image has way more pixels than the number of characters should be
        # used in ascii representation, scaling the image while preseving the aspect is
        # needed.
        global resize_h, resize_w
        result = []
        # resize_h is the rescaling ratio of height
        # resize_w is the rescaling ratio of width
        for h in range(resize_h-1, y.shape[0], resize_h):
            row = []
            for w in range(resize_w-1, y.shape[1], resize_w):
                new_px = 0
                # get the avg val of a chunk of pixels of size (resize_h * resize_w)
                for sub_h in range(h, h-resize_h, -1):        
                    for sub_w in range(w, w-resize_w, -1):
                        new_px += y[sub_h][sub_w]
                new_px /= resize_h*resize_w

                if new_px < 0: new_px = 0       # double check the new val is within range
                elif new_px > 255: new_px = 255
                
                row.append(self.select_char(new_px))
            result.append(row)

        for row in result:
            for elmt in row:
                sys.stdout.write(elmt)
            time.sleep(.02) 
            sys.stdout.write('\n')

        result = Image.fromarray(y.astype(np.uint8))
        result.save('out.png')

if __name__ == '__main__':
    tf = transformImage()
    y = tf.pre_process_img('totoro.png')
    tf.greyscale_to_ascii(y)




