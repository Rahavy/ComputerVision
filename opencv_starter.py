#pip install numpy
#pip install matplotlib
#pip install scipy
#pip install scikit-image
#pip install opencv-contrib-python

import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

#read in an image into memory
img = cv.imread('C:/Users/joshu/OneDrive/Documents/GitHub/ComputerVision/Orings/Oring1.jpg',0)
copy = img.copy()
#check out some of its pixel values...img[x,y]..try different x and y values
x = 100
y = 100
pix = img[x,y]
print("The pixel value at image location [" + str(x) + "," + str(y) + "] is:" + str(pix))

#histogram
plt.figure(figsize=(10,5))
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram of Image 1')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

#auto thresholding with otsus method from lecture 2
hist = np.histogram(img.ravel(), 256, (0,256))[0]
total = img.size
sum_total = 0
for t in range(256):
    sum_total += t * hist[t]
sumB = 0
wB = 0
varMax = 0
threshold = 0
for t in range(256):
    wB += hist[t] #weight background
    if wB == 0:
        continue
    wF = total - wB#weight foreground
    if wF == 0:
        break
    sumB += t * hist[t]
    mB = sumB / wB #mean background
    mF = (sum_total - sumB) / wF #mean foreground
    varBetween = wB * wF * (mB - mF) * (mB - mF) #between class variance
    if varBetween > varMax:
        varMax = varBetween
        threshold = t
print("auto thresholding", threshold)


#implement thresholding ourselves using loops (soooo slow in python)
before = time.time()
for x in range(0, img.shape[0]):
    for y in range(0, img.shape[1]):
        if img[x,y] > threshold:
            img[x,y] = 255
        else:
            img[x,y] = 0
after = time.time()
print("Time taken to process hand coded thresholding: " + str(after-before))

#text
text1 = "threshold: " + str(threshold)
text2 = "time: " + str(after-before)
font = cv.FONT_HERSHEY_SIMPLEX
height = img.shape[0]
cv.putText(img,text1,(10,40),font, 0.4,(0,0,255),1)
cv.putText(img,text2,(10,height-10), font, 0.4,(0,0,255),1)



cv.imshow('thresholded image 1',img)
cv.waitKey(0)

###########################################

#read in an image into memory
img = cv.imread('C:/Users/joshu/OneDrive/Documents/GitHub/ComputerVision/Orings/Oring2.jpg',0)
copy = img.copy()
#check out some of its pixel values...img[x,y]..try different x and y values
x = 100
y = 100
pix = img[x,y]
print("The pixel value at image location [" + str(x) + "," + str(y) + "] is:" + str(pix))

#histogram
plt.figure(figsize=(10,5))
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram of Image 2')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

#auto thresholding with otsus method from lecture 2
hist = np.histogram(img.ravel(), 256, (0,256))[0]
total = img.size
sum_total = 0
for t in range(256):
    sum_total += t * hist[t]
sumB = 0
wB = 0
varMax = 0
threshold = 0
for t in range(256):
    wB += hist[t] #weight background
    if wB == 0:
        continue
    wF = total - wB#weight foreground
    if wF == 0:
        break
    sumB += t * hist[t]
    mB = sumB / wB #mean background
    mF = (sum_total - sumB) / wF #mean foreground
    varBetween = wB * wF * (mB - mF) * (mB - mF) #between class variance
    if varBetween > varMax:
        varMax = varBetween
        threshold = t
print("auto thresholding", threshold)

#implement thresholding ourselves using loops (soooo slow in python)
before = time.time()
for x in range(0, img.shape[0]):
    for y in range(0, img.shape[1]):
        if img[x,y] > threshold:
            img[x,y] = 255
        else:
            img[x,y] = 0
after = time.time()
print("Time taken to process hand coded thresholding: " + str(after-before))
cv.imshow('thresholded image 2',img)
cv.waitKey(0)



