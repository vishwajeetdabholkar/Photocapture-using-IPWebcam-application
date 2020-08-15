# Author : Vishwajeet Dabholkar
# 
#Code to capture photos using ip camera 
import urllib.request
import cv2
import numpy as np
import time
import sys

sys.path.append("..")

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.1.102:8080/shot.jpg'

img_counter = 0

while True:
    # Use urllib to get the image from the IP camera
    imgResp = urllib.request.urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)	
	
	# put the image on screen
    #cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    #time.sleep(0.1) 
	#following code is for taking image and saving it into spcified directory
    img_name = "test{}.jpg".format(img_counter)
    cv2.imwrite('path/to/save/images/'+img_name, img)
    #print("{} written!".format(img_name))	
    img_counter += 1
	#cv2.imwrite('C:/tensorflow1/models/research/object_detection/'+img_name, img)
    break
