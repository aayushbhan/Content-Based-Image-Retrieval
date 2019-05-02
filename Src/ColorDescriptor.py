import numpy as np
import cv2
import imutils

class ColorDescriptor:
    def __init__(self, bins):
        #Storing number of bins for histogram
        self.bins = bins
        
    def describe(self, image):
        #Convert the image into hsv and initialize the features to quantify the image
        image = image.astype('uint8')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []
        
        #Obtaining the dimensions and center of the image
        (h, w) = image.shape[:2]                 
        (cX, cY) = (int(w * 0.5), int(h * 0.5))
        
        #Divide the image into 4 segements(top-left,top-right,bottom-left,bottom-right,center)
        segements = [(0,cX,0,cY),(cX,w,0,cY),(cX,w,cY,h),(0,cX,cY,h)]
        
        #Construct an eliptical mask representing the center of the image which is 75% of height and width of image
        (axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)
        ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)
        	
        #Loop over the segements
        for(startX, endX, startY, endY) in segements:
            #Construct a mask for each corner of the image subtracting the elliptical center from it
            cornerMask = np.zeros(image.shape[:2], dtype="uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255 ,-1)
            cornerMask = cv2.subtract(cornerMask, ellipMask)
            
            #Extract a color histogram from the image and update the feature vector
            hist = self.histogram(image, cornerMask)
            features.extend(hist)
            
        #Extract a color histogram from the elliptical region and update the feature vector
        hist = self.histogram(image, ellipMask)
        features.extend(hist)
        
        #Return the feature vector
        return features
    
    def histogram(self,image,mask):
        
        #Extract a 3-D color histogram from the masked region of the image, using the number of bins supplied
        #print(image)
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])
        
        #Normalize the histogram
        if imutils.is_cv2():
            #For openCV version 2.4
            hist = cv2.normalize(hist).flatten()
        else:
            #For openCV version 3+
            hist = cv2.normalize(hist, hist).flatten()
            
        #Returning histogram
        return hist
