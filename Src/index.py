#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:53:54 2019

@author: aayush
"""

import ColorDescriptor

#Used for parsing command line arguments
import argparse
#Used for getting paths of our images
import glob
import cv2

#Create the argument parser to parse the arguments
ap = argparse.ArgumentParser()

#Switch for the path to our photos directory
ap.add_argument("-d","--dataset", required = True , help = "Path to directory that contains images")
ap.add_argument("-i","--index", required = True , help = "Path to where the index will be stored")
args = vars(ap.parse_args())


#Initializing our color descriptor
cd = ColorDescriptor.ColorDescriptor((8,12,13))

#open the output index file for writing
output = open(args["index"],"w")

#Using glob to get path of images and go through all of them
for imagePath in glob.glob(args["dataset"]+"/*.jpg"):
    #Get the UID of the image path and load the image
    imageUID =  imagePath[imagePath.rfind("/")+1:]
    image = cv2.imread(imagePath)
    #Using the describe function 
    features = cd.describe(image)
    
    #write the features to a csv file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageUID, ",".join(features)))
    
# closing the index file
output.close()
