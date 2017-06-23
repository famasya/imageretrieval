from __future__ import division
import glob
from PIL import Image
import numpy as np
from numpy import array
import math
import json
from operator import itemgetter

def getMetadata(img):
	metadata = []
	img = Image.open(img)
	arr = array(img)
	color_array = []
	color_r = [0]*64
	color_g = [0]*64
	color_b = [0]*64
	for x in arr:
		for y in x:
			r = int(math.floor(y[0]/4))
			color_r[r] += 1
			g = int(math.floor(y[1]/4))
			color_g[g] += 1
			b = int(math.floor(y[2]/4))
			color_b[b] += 1
	color_array.append({'r': color_r, 'g': color_g, 'b': color_b})
	metadata.append({"fn":"original","metadata": color_array})
	return metadata

def diff(a,b):
	dot = np.dot(a,b)
	size_a = 0
	for x in a:
		size_a += x**2
	size_a = math.sqrt(size_a)
	size_b = 0
	for x in b:
		size_b += x**2
	size_b = math.sqrt(size_b)
	return dot/(size_a*size_b)

def main(file):
	# query = "images/0.jpg"
	query_metadata = getMetadata(file)
	rank = []
	with open("data.json") as json_content:
		items = json.load(json_content)
		for data in items:
			diff_r = diff(query_metadata[0]['metadata'][0]['r'],data['metadata'][0]['r'])
			diff_g = diff(query_metadata[0]['metadata'][0]['g'],data['metadata'][0]['g'])
			diff_b = diff(query_metadata[0]['metadata'][0]['b'],data['metadata'][0]['b'])
			sim = (diff_r+diff_g+diff_b)/3
			rank.append((data['fn'],sim))
	sort = sorted(rank,key=itemgetter(1),reverse=True)
	del sort[0]
	return json.dumps(sort)

if __name__ == '__main__':
	main()
