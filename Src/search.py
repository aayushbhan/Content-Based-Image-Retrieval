#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 00:31:37 2019

@author: aayush
"""

import ColorDescriptor
import Searcher
import argparse
import cv2

# creating the argument parser and parsing the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True, help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True, help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True, help = "Path to the result path")
args = vars(ap.parse_args())

#intializing the color descriptor
cd = ColorDescriptor.ColorDescriptor((8,12,3))

#loading the query image and describe it
query = cv2.imread(args["query"])

queryFeatures = cd.describe(query)

#performing the search
s1 = Searcher.Searcher(args["index"])

results = s1.search(queryFeatures)


#displaying the query
cv2.imshow("Query",query)

#loop over the results

for (score, resultID) in results:
    #load the result image and display it
    result1 = cv2.imread(args["result_path"] + "/" + resultID)
    result = cv2.resize(result1,(300,300))
    cv2.imshow("Result",result)
    cv2.waitKey(0)
