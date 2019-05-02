#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:57:48 2019

@author: aayush
"""

import numpy as np
import csv

class Searcher:
    def __init__(self,indexPath):
        #storing the index 
        self.indexPath = indexPath
        
    def search(self,queryFeatures):
        #make a dictionary for thr results
        results = {}
        
        #open the index file for reading
        with open(self.indexPath) as f:
            # initializing the csv reader
            reader = csv.reader(f)
            
            #loop over the rows in the index
            for row in reader:
                # parse out the imageID and features, then calculate the chi-squared distance between the saved features and the features of our image
                features = [float(x) for x in row[1:]]
                d = self.chi2_distance(features, queryFeatures)
                
                # now we have the distance between the two feature vectors. we now update the results dictionary
                results[row[0]] = d
                
            # closing the reader
            f.close()
            
        # sort the results such that the dictionary starts with smaller values as they will be closest to the given image
        results = sorted([(v,k) for (k,v) in results.items()])
        
        #return our results
        return results[:1]
    
    def chi2_distance(self, histA, histB, eps = 1e-10):
        #calculating the chi squared distance
        d = 0.5 * np.sum([((a-b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
        
        #return the chi squared distance
        return d
