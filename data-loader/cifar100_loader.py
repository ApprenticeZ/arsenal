'''
parse cifar100 data file into images
'''

import os,os.path
import argparse
import numpy as np
import cPickle
import cv2

parser = argparse.ArgumentParser(description='parse cifar 100 data')
parser.add_argument('--data-dir',type=str,default='/qydata/yzhangdx/dataset/cifar-100-python',help='path to load original data files')
parser.add_argument('--img-save-dir',type=str,default='/qydata/yzhangdx/dataset/cifar-100-python',help='path to save images')
parser.add_argument('--lst-save-dir',type=str,default='/qydata/yzhangdx/dataset/cifar-100-python',help='path to save image.lst')
args = parser.parse_args()

K_JOIN = '\t'

def unpickle(args,setType):
	# create save dir if it does not exist
	savepath = os.path.join(args.img_save_dir,setType+'-img')
	if not os.path.isdir(savepath):
		os.system('mkdir '+savepath)
	lst_file = open(os.path.join(args.lst_save_dir,setType+'.lst'),'w')
	# load data file
	df = open(os.path.join(args.data_dir,setType),'rb')
	d = cPickle.load(df)
	# there are 5 fields in dict
	# 'data', 'batch_label', 'fine_labels', 'coarse_labels','filenames'
	images = d['data']
	numImage = images.shape[0]
	imShape = (3,32,32)
	for idx in xrange(numImage):
		# reshape image
		im = np.reshape(images[idx],imShape)
		r = im[0,:,:]
		g = im[1,:,:]
		b = im[2,:,:]
		im = cv2.merge((r,g,b))
		# write to disk
		cv2.imwrite(os.path.join(savepath,d['filenames'][idx]),im)
		# write label+filename to lst file
		lst_info = map(str,[idx,d['fine_labels'][idx],d['coarse_labels'][idx],d['filenames'][idx]])
		lst_file.write(K_JOIN.join(lst_info)+'\n')
	df.close()
	lst_file.close()

unpickle(args,'train')
unpickle(args,'test')
