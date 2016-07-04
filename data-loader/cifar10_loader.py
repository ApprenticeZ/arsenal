'''
parse cifar10 data file into images
'''

import os,os.path
import argparse
import numpy as np
import cPickle
import cv2
import random

parser = argparse.ArgumentParser(description='parse cifar 10 data')
parser.add_argument('--data-dir',type=str,default='/qydata/yzhangdx/dataset/cifar-10-batches-py',help='path to load original data files')
parser.add_argument('--img-save-dir',type=str,default='/qydata/yzhangdx/dataset/cifar-10-batches-py',help='path to save images')
parser.add_argument('--lst-save-dir',type=str,default='/qydata/yzhangdx/dataset/cifar-10-batches-py',help='path to save image.lst')
args = parser.parse_args()

random.seed(100)
K_JOIN = '\t'

def parse_batch(datapath,savepath,offset):
	# load data file
	df = open(os.path.join(datapath),'rb')
	d = cPickle.load(df)
	# there are 4 fields in dict
	# 'data', 'batch_label', 'labels','filenames'
	images = d['data']
	numImage = images.shape[0]
	imShape = (3,32,32)
	batch_list = []
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
		lst_info = map(str,[idx+offset,d['labels'][idx],d['filenames'][idx]])
		batch_list.append(lst_info)
	df.close()
	return batch_list

def unpickle(args,setType):
	print(setType+' set')
	# create save dir if it does not exist
	savepath = os.path.join(args.img_save_dir,setType)
	if not os.path.isdir(savepath):
		os.system('mkdir '+savepath)
	batch = []
	if setType == 'train':
		for i in xrange(5):
			print('processing batch '+str(i+1))
			batch.extend(parse_batch(os.path.join(args.data_dir,'data_batch_'+str(i+1)),savepath,10000*i))
	else:
		batch = parse_batch(os.path.join(args.data_dir,'test_batch'),savepath,0)
	random.shuffle(batch)
	lst_file = open(os.path.join(args.lst_save_dir,setType+'.lst'),'w')
	for l in batch:
		lst_file.write(K_JOIN.join(l)+'\n')
	lst_file.close()

unpickle(args,'train')
unpickle(args,'test')