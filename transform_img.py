from data import *
import numpy as np
from PIL import Image

class transformImage():
	def pre_process_img(self, img):
		# greyscale image
		x = Image.open(img, 'r')
		x = x.convert('L') # make it greyscale
		y = np.asarray(x.getdata(),dtype=np.uint16).reshape((x.size[1],x.size[0]))
		print y.shape
		return y

	def select_char(self, grey_val):
		pass

	def greyscale_to_ascii(self, nparray):
	    result = []
		for h in range(0, nparray.shape[0]):
			list = []
			for w in range(0, nparray.shape[1]):
				#TODO: need to reshape img first


		# result = Image.fromarray(y.astype(np.uint8))
		# result.save('out.png')
		
if __name__ == '__main__':
	tf = transformImage()
	tf.pre_process_img('dog.png')