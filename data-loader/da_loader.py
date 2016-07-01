'''
data loader for domain adaptation dataset
'''

import os,os.path
import argparse
import numpy as np
import cv2

'''
data set structure
* amazon
* dslr
* webcam
'''

parser = argparse.ArgumentParser(description='parse domain adaptation data set')
parser.add_argument('--data-dir',type=str,default='/qydata/yzhangdx/dataset/da-data',help='path to load original data files')
parser.add_argument('--save-dir',type=str,default='/qydata/yzhangdx/dataset/da-data',help='path to save lst files')
args = parser.parse_args()

K_JOIN_SYM = '\t'

def _checkDir(newpath):
    if not os.path.isdir(newpath):
        os.system('mkdir '+newpath)

def _label_mapping(args,category_dict):
    meta_file = open(os.path.join(args.save_dir,'label.info'),'w')
    for k,v in category_dict.items():
        meta_file.write(str(v)+'\t'+k+'\n')
    meta_file.close()

def _write_lst(args,d):
    for domain,lst in d.items():
        lst_file = open(os.path.join(args.save_dir,domain+'.lst'),'w')
        info_file = open(os.path.join(args.save_dir,domain+'.info'),'w')
        for line in lst:
            info_file.write(K_JOIN_SYM.join(map(str,line))+'\n')
            lst_file.write(K_JOIN_SYM.join(map(str,line[:-3]))+'\n')
        lst_file.close()
        info_file.close()

def da_stat(args):
    _checkDir(args.save_dir)
    d = {}
    category_dict = {} # mapping category-label id
    for path, subdirs, files in os.walk(args.data_dir):
        for fname in files:
            fpath = os.path.join(path, fname)
            path_components = fpath.split('/')
            category = path_components[-2]
            if category not in category_dict.keys():
                cid = len(category_dict)
                category_dict[category] = cid
            domain = path_components[-4]
            if domain not in d.keys():
                d[domain] = []
            image_list = d[domain]
            if os.path.isfile(fpath):
                im = cv2.imread(fpath)
                imsize = im.shape
                image_list.append((len(image_list), category_dict[category], fname)+imsize)

    _label_mapping(args,category_dict)
    _write_lst(args,d)

if __name__ == '__main__':
    da_stat(args)