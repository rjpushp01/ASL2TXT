import cv2 as cv
import sys
import imutils      #imutils is a library that can be used to make cv and many more things easier


# img = cv.imread(cv.samples.findFile("starry_night.jpg"))
# img = cv.imread(r"C:\Users\pushp\OneDrive\Pictures\Screenshots\Screenshot 2024-06-30 232055.png")
# if img is None:
#     sys.exit("image can't be generated")

# cv.imshow("Display Window",img)     # Display window is only a name given for the window that will be shown
# [h,w,d] = img.shape                # Height is the no. of rows and width is the col. while depth is the no. of layers like here RGB
# print(f"height = {h}, w= {w} and d= {d}")
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("soc image.jpg",img)
#     print("image is saved")
# cv.destroyAllWindows()

# #To access the pixel at a particular loc. like (100,50) i.e y = 100 and x= 50 as explained above which is rows then columns as height and width
# for i in range(941):     
#     (B,G,R)= img[i,50]
#     if B != 255: 
#         print (f"R= {R}, G= {G} and B={B}\n") # Remember RGB is used as BGR as initially it was considered as this format when RGB was initialized in openCV
#         print(i)
 
 

'''Array or image slicing image[startY:endY,startX:EndX] '''      
img2 = cv.imread(r"C:\Users\pushp\Downloads\cv learning image.jpg")
cv.imshow("Jurassic park",img2)
cv.waitKey(0)
[H,W,D]=img2.shape
# ROI = img2[60:220,320:400]   
# cv.imshow("Zoomed image",ROI)
# cv.waitKey(0)

'''Resizing Image ignoring aspect ratio'''
# img2_resize = cv.resize(img2,(200,200))
# cv.imshow("resized image",img2_resize)
# cv.waitKey(0)

'''Resizing considering aspect ratio'''
# r_H = 300       #resized height
# r_W = int(300*W/H)
# img2_aspect = cv.resize(img2,(r_W,r_H))
# cv.imshow("Resize with aspect ratio",img2_aspect)
# cv.waitKey(0)

# '''Resizing using imutils'''
# img2_aspect = imutils.resize(img2,height=300)
# cv.imshow("Resize with imutils",img2_aspect)
# cv.waitKey(0)

'''Image rotation using CV2'''
# centre = (W//2,H//2)
# M = cv.getRotationMatrix2D(centre,-45,1)
# rotated = cv.warpAffine(img2,M,(W,H))
# cv.imshow("Rotated image using cv",rotated)
# cv.waitKey(0)

'''image rotation using imutils'''
# rotated2 = imutils.rotate(img2,-45)
# cv.imshow("Rotated using imutils",rotated2)
# cv.waitKey(0)

'''Rotated image entirely in the picture'''
#CV doesn't care about the image going out of the frame, so a diff. imutils func. rotate_bound is used
# rotated3 = imutils.rotate_bound(img2,45)
# cv.imshow("Rotated in frame",rotated3)
# cv.waitKey(0)

'''Creating blurred image (as it makes algorithm easier to understand instead of getting misleaded by noises)'''
# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
# blurred = cv.GaussianBlur(img2,(11,11),0)  
# cv.imshow("blurred image",blurred)
# cv.waitKey(0)

'''Drawing on image'''
#Notice that drawing on an image is inplace so we must copy before doing these tasks
# img2_copy = img2.copy()
# rect = cv.rectangle(img2_copy,(320,40),(420,180),(0,0,255),2)  # BGR and starting point is at top left and ending is at bottom right and the 2 parameter is for line width
# cv.imshow("Rectangle image",rect)
# cv.waitKey(0)

# Circle takes a centre point, radius, BGR and width 
# img2_copy2 = img2.copy()
# circle = cv.circle(img2_copy2,(360,110),70,(255,0,0),-1)        # -1 will make the circle or any other drawing solid i.e. a disc
# cv.imshow("Circular image",circle)
# cv.waitKey(0)

#Line takes 2 points as parameters
# img2_copy3 = img2.copy()
# line = cv.line(img2_copy3,(100,23),(340,90),(0,0,150),2)
# cv.imshow("Lined Image",line)
# cv.waitKey(0)

'''Putting text in image'''
img2_copy4 = img2.copy()
#The putText takes image, text, starting pt. , font style, scaling of font , color and line width
text = cv.putText(img2_copy4,"Text_CV + Jurassic Park",(30,24),cv.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0),2) 
cv.imshow("text on image",text)
cv.waitKey(0)

img3 = cv.imread(r"C:\Users\pushp\Downloads\tetris_blocks for learning.png")
cv.imshow("tetris image",img3)
cv.waitKey(0)

''''''



