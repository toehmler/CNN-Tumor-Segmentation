# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import SimpleITK as sitk
import numpy as np 
import skimage.io as skio
import os
from medpy.io import load
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

inputfolder = "/Users/jacobellen/desktop/BRATS2015_Training/HGG/"
lowgradefilelist = os.listdir("/Users/jacobellen/desktop/BRATS2015_Training/LGG/")
highgradefilelist = os.listdir("/Users/jacobellen/desktop/BRATS2015_Training/HGG/")


files = []
def loadscan(path):
    for dirName, subdirList, fileList in os.walk(path):
        for filename in fileList:
            if ".mha" in filename.lower():
                files.append(os.path.join(dirName, filename))
    return files

HGG = loadscan("/Users/jacobellen/desktop/BRATS2015_Training/HGG/")
LGG = loadscan("/Users/jacobellen/desktop/BRATS2015_Training/LGG/")


images = []
for i in HGG:
    image = sitk.ReadImage(i)
    images.append(image)

#SHOWS EACH THREE-DIMENSIONAL IMAGE
sitk.Show(images[200])

#Subset of Images if Needed for Testing
imagessub = images[1:3]


#Turning Images into a Stack of 155 2-D Images of Dimensions 240x240
max_index = images[1].GetDepth()
list_of_2D_images = [images[1][:,:,i] for i in range(max_index)]
sitk.Show(list_of_2D_images[80])

#Turning Images into a 


#listofimages = []
#for threedimages in images2:
m = [sitk.GetArrayFromImage(images[1][:,:,i]) for i in range(max_index)]
 #listofimages.append(m)
a=image[1]
zslice = a[100]
z = 0
slice = sitk.GetArrayFromImage(image)[100,:,:]
slice

#slice = sitk.GetArrayViewFromImage(images[1])[x,y,z]
#plt.imshow(slice)


#maysurvey = pd.read_csv('/Users/jacobellen/desktop/maysurvey.csv')
#maysurvey = pd.DataFrame(maysurvey)
#june = maysurvey.loc[1,:]
#a = maysurvey['totalTime'] 
#b=maysurvey.totalTime
#c= maysurvey[['totalTime', 'referrer']]