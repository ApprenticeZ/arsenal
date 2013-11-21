# !/usr/bin/env python
# encoding=utf-8

'''
Function: Go through a directory and save the file in the dir into a txt file
Input: directory
Output: an txt file stores all the filenames in the specified dir
The first line specifies the directory
The following lines record the file names

Author: ApprenticeZ
'''

import os
import os.path

dataset_directory = r"I:\AVIP\workspace\Dataset\an\jpg2"
out = open(os.path.join(r"I:\AVIP\workspace\dataset\an", "training-poslist.txt"), 'w')
for parent, dirnames, filenames in os.walk(dataset_directory):
	out.write(parent+"\n");
	for imname in filenames:
		out.write(imname+"\n")
		
out.close()