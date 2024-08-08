import argparse
import cv2 as cv
import imutils
import numpy as np

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i","--image",help="This argument is used to ger image",required=True,default="C:/Users/pushp/Downloads/tetris_blocks_for_learning.png")
# #We can also use required = True but then you will have to specify the path of an image and the default value doesn't makes sense. In this case no default value is set.
 
# # Load the image from the path as the command line argument
# args = ap.parse_args()
# image = cv.imread(f"{args.image}")
# cv.imshow("image",image)
# cv.waitKey(0)

# '''Gray Scale Conversion'''
# gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow("gray_scale_image",gray)
# cv.waitKey(0)

# '''Edge Detection'''
# edged = cv.Canny(gray,30,150)
# cv.imshow("Edged ",edged)
# cv.waitKey(0)

# '''Thresolding Operation'''
# thresold_image = cv.threshold(gray,225,255,cv.THRESH_BINARY_INV)[1]
# #Some of the thresolding types are:
#     # 1) THRESH_BINARY: >THRESH To high
#     # 2) THRESH_BINARY_INV: >THRESH to 0
#     # 3) THRESH_TRUNC: >THRESH to THRESH value other remains same
#     # 4) THRESH_TOZERO: <THRESH to 0 other remains same
#     # 5) THRESH_TOZEROINV: >THRESH to 0 other remains same 
# cv.imshow("thresold_image",thresold_image)
# cv.waitKey(0)

# '''Detecting and drawing Contours'''
# cnts= cv.findContours(thresold_image.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
# cnts= imutils.grab_contours(cnts)
# output= image.copy()

# for c in cnts:
#     cv.drawContours(output,[c],-1,(240,0,159),3)
#     cv.imshow("Contour image",output)
#     cv.waitKey(0)

# '''https://learnopencv.com/contour-detection-using-opencv-python-c/'''
# #Refer to the above website for learning contour detection and other similar features of openCV.

# #BGR color splitting
# blue,green,red = cv.split(image)

# #Detecting colour using blue channel only and without thresolding
# contours1, hierarchy=cv.findContours(blue,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
# #Draw contours on the original image
# image_contour_blue = image.copy()
# cv.drawContours(image_contour_blue,contours1,-1,(0,255,0),2,cv.LINE_AA,hierarchy)
# cv.imshow("Contour Detection Using blue only",image_contour_blue)
# cv.waitKey(0)
# cv.destroyAllWindows()

# #Detecting colour using green channel only and without using thresolding
# contours2,hierarchy2 = cv.findContours(green,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
# image_contour_Green = image.copy()
# cv.drawContours(image_contour_Green,contours2,-1,(0,255,0),2,cv.LINE_AA,hierarchy2)
# cv.imshow("Contour Detection using Green Only",image_contour_Green)
# cv.waitKey()
# cv.destroyAllWindows()

# #Detecting contours using Red channel only and without using thresolding
# contours3,hierarchy3 = cv.findContours(red,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
# image_contour_Red = image.copy()
# cv.drawContours(image_contour_Red,contours3, -1,(0,255,0),2,cv.LINE_AA,hierarchy3)
# cv.imshow("Contour Detection using Red only", image_contour_Red)
# cv.waitKey(0)
# cv.destroyAllWindows(0)

# '''For visualising the cv.CHAIN_APPROX_SIMPLE and cv.CHAIN_APPROX_NONE'''
# #Remember Simple and none give very similar type of image contours thanks to the draw contours() because it automatically draws the adjacent contour points by itself
# gray_2 = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# ret,thres= cv.threshold(gray_2,150,255,cv.THRESH_BINARY)
# contours_,hierarchy_ = cv.findContours(thres,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# image_2 =image.copy()
# cv.drawContours(image_2,contours_,-1,(0,255,0),2,cv.LINE_AA,hierarchy_)
# cv.imshow("Simple Approximation Contours",image_2)
# cv.waitKey(0)

# image_3 = image.copy()
# for i, contour in enumerate(contours_):  #loop over one contour area
#     for j, contour_point in enumerate(contour):  #loop over the points
#         # Draw a circle on the current contour coordinate
#         cv.circle(image_3,((contour_point[0][0],contour_point[0][1])),2,(0,255,0),2)

# #see the resu;ts 
# cv.imshow("CHAIN_APPROX_SIMPLE print only",image_3)
# cv.waitKey(0)
# cv.destroyAllWindows()

'''Blob Detection'''
image_blob = cv.imread("C:/Users/pushp/Downloads/tetris_blocks_for_learning.png")
image_blob_gray = cv.cvtColor(image_blob,cv.COLOR_BGR2GRAY)
# Set up the detector with default parameters.
detector = cv.SimpleBlobDetector()
#Detect blobs 
keypoints = detector.detect(image_blob_gray)

# Draw detected blobs as red circles 
# cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
image_blob_with_keypoints = cv.drawKeypoints(image_blob_gray,keypoints,np.array([]),(0,0,255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv.imshow("Keypoints",image_blob_with_keypoints)
cv.waitKey(0)



 
 
 
 
        





