# !/usr/bin/env python
# encoding=utf-8

'''
Function: match esvm model sequence with image id in PASCAL VOC dataset
Input: directory
Output: an txt file, each line contains a record
	    record format = [image_id, box_id, esvm_model_id]

Author: ApprenticeZ
'''

import os
import os.path

dataset_directory = r"I:\AVIP\workspace\Dataset\1000Models\images_1000_Model"
out = open(os.path.join(r"I:\AVIP\workspace\voc-release3.1\sub_category", "esvm_match_voc.txt"), 'w')

for parent, dirnames, filenames in os.walk(dataset_directory):
	out.write(parent+"\n");
	for imname in filenames:
		s_imname = imname.replace('_', '.').split('.')
		out.write(s_imname[0]+'\t'+s_imname[1]+'\t'+s_imname[3]+'\n')

out.close();