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
hist = np.histogram(img.ravel(), 256, (0,256))[0]#gets graph of pixel values
total = img.size#number of pixels in the img
sum_total = 0#gets sum of pixels from img
for t in range(256):
    sum_total += t * hist[t]
sumB = 0#gets sum of pixels for background and foreground
wB = 0
varMax = 0
threshold = 0
for t in range(256):#test all threshld values
    wB += hist[t] #weight background/adddes pixels to background
    if wB == 0:
        continue
    wF = total - wB#weight foreground/whatever pixels are left are for foreground
    if wF == 0:
        break
    sumB += t * hist[t]#adds pixels to background sum
    mB = sumB / wB #mean background/gets average pixel value for background
    mF = (sum_total - sumB) / wF #mean foreground/gets average pixel value for foreground
    varBetween = wB * wF * (mB - mF) * (mB - mF) #between class variance/gets the variance between the two classes
    if varBetween > varMax:#if the variance is bigger than the max then it becomes new max and threshold is the current t value
        varMax = varBetween
        threshold = t
print("auto thresholding", threshold)


#pixiel img
before = time.time()
for x in range(0, img.shape[0]):
    for y in range(0, img.shape[1]):
        if img[x,y] > threshold:
            img[x,y] = 255
        else:
            img[x,y] = 0
after = time.time()
print("Time taken to process hand coded thresholding: " + str(after-before))

#binary morphology
SE = np.arry([[0,1,0],#circle structure cuz rings are circuls 
              [1,1,1],
              [0,1,0]])

dilated = img.copy()

for x in range(1, img.shape[0]-1):#goes to img but edges are blocked
    for y in range(1, img.shape[0]-1):
        neighbourhood = img[x-1:x+2, y-1:y+2]#looks at the area around the pixel
        if np.any(neighbourhood == 255):#looks to find a white pixel in the neighbourhood then it sets the current pixel to white
            dilated[x,y] = 255
            
#erosion
closed = dilated.copy()#copies the dilated img to get erosion 
for x in range(1, dilated.shape[0]-1):#also goes to img
    for y in range(1, dilated.shape[1]-1):
        neighbourhod = dilated[x-1:x+2, y-1:y+2]#also looks at the area around the pixel
        if np.any(neighbourhood == 0):#same but instead of looking for white its black and current pixel is turned black
            closed[x,y] = 0


#text
text1 = "threshold: " + str(threshold)
text2 = "time: " + str(after-before)
font = cv.FONT_HERSHEY_SIMPLEX
height = img.shape[0]#for the placement of text
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



