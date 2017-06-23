import glob
from scipy.misc import imread, imshow
from scipy import ndimage
import numpy as np
from numpy import array
import math
import json
import matplotlib.pyplot as plt

def main():
	# f = glob.glob('dataset/*.png')
	f = ['dataset/0.png']
	metadata = []
	for image in f:
		img = imread(image)
		color_array = []
		color_r = [0]*64
		color_g = [0]*64
		color_b = [0]*64
		l = []
		for x in img:
			a = []
			for y in x:
				if((y[0] < 30) & (y[1] < 30) & (y[2] < 30)):
					print y[0],y[1],y[2]
					c = [y[0],y[1],y[2]]
				else:
					c = [y[0],y[1],y[2]]
				# r = int(math.floor(y[0]/4))
				# color_r[r] += 1
				# g = int(math.floor(y[1]/4))
				# color_g[g] += 1
				# b = int(math.floor(y[2]/4))
				# color_b[b] += 1
				# c = [r,g,b]
				a.append(c)
			l.append(a)
		plt.imshow(array(l))
		plt.show()
		# color_array.append({'r': color_r, 'g': color_g, 'b': color_b})
		# metadata.append({"fn":image,"metadata": color_array})
		# print "File :",image,"done"
	# with open('tralala.json','w') as file:
	# 	json.dump(metadata,file)

if __name__ == '__main__':
	main()
