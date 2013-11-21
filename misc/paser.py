# !/usr/bin/env python
# encoding=utf-8

'''
This piece of code is used to transform the ground truth in xml format to txt format. 
It is designed to parse CAVIAR Dataset, and can be quickly adapted to other dataset. 

Input: filename of the xml file
Output: a series of txt files, each contains ground truth of an image in the dataset
Each row contains 6 data fields, the id of the target, height and width of the bounding box, 
the center of bbox in (xc, yc) format and its appearance (0: appear, 1:visible, 2:disapear, 3:occluded)

Configs:
- infilePath: specify the filename of the xml file
- ofilePath: path to store the parsed txt files

Author: ApprenticeZ
'''

from xml.etree import ElementTree
import sys

# if len(sys.argv) < 3:
	# print 'not enough arguments'
	# sys.exit()

infilePath = r"I:\AVIP\fore-background-detection\TwoLeaveShop1cor\gt\c2ls1gt.xml"
# sys.argv[1]+"\\gt\\"+sys.argv[2] 
ofilePath = r"I:\AVIP\fore-background-detection\TwoLeaveShop1cor\gt\frame"
# sys.argv[1]+r"\gt\frame"
appearanceState = {'appear':0, 'visible':1, 'disappear':2, 'occluded':3}
xmldoc = ElementTree.parse(infilePath)
framelist = xmldoc.getiterator('frame')

for fr in framelist:
	mat = open(ofilePath+fr.get('number')+".txt", 'w')
	# print 'frame ', fr.get('number')
	olist = fr.getiterator('object')
	for obj in olist:
		id = obj.get('id')
		mat.write(id)
		mat.write('\t')
		box = obj.find('box').attrib
		mat.write(box['h'])
		mat.write('\t')
		mat.write(box['w'])
		mat.write('\t')
		mat.write(box['xc'])
		mat.write('\t')
		mat.write(box['yc'])
		mat.write('\t')
		appearance = obj.find('appearance').text
		mat.write(str(appearanceState[appearance]))
		mat.write('\n')
	# glist = fr.getiterator('group')
	mat.close()
