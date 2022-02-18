import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

ksize = 5
sigma = 5
theta = 1*np.pi/4 #1*np.pi/2
lamda = 1*np.pi/4  #1*np.pi/4 I'm fig for here
gama = 0.5
phi = 0

kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gama, phi, ktype=cv2.CV_32F)

img = cv2.imread('synthetic.jpg') #pic.png
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fimg = cv2.filter2D(img, cv2.CV_8UC3, kernel)
kernel_resized = cv2.resize(kernel, (400, 400))

cv2.imshow('Origin image', img)
cv2.imshow('filter image', fimg)
cv2.imshow('kernel', kernel_resized)
cv2.waitKey()
cv2.destroyAllWindows()