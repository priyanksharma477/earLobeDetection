import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def nothing(x):
    pass

cap = cv2.VideoCapture('trainData2.avi')
file = open('ear_coordinate.txt', 'w')
#file.write('x1			y1			x2			y2\n')
file.write('x1			y1\n')			

n3 = 'HSV_TrackBar'
x = 'trackbar'
cv2.namedWindow(n3)
# Creating track bar
cv2.createTrackbar('h', n3, 70, 179, nothing)
cv2.createTrackbar('s', n3, 76, 255, nothing)
cv2.createTrackbar('v', n3, 110, 255, nothing)
cv2.createTrackbar('h1', n3, 90, 179, nothing)
cv2.createTrackbar('s1', n3, 255, 255, nothing)
cv2.createTrackbar('v1', n3, 255, 255, nothing)

while (1):

    h = cv2.getTrackbarPos('h', n3)
    s = cv2.getTrackbarPos('s', n3)
    v = cv2.getTrackbarPos('v', n3)
    h1 = cv2.getTrackbarPos('h1', n3)
    s1 = cv2.getTrackbarPos('s1', n3)
    v1 = cv2.getTrackbarPos('v1', n3)

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, np.array([h, s, v]), np.array([h1, s1, v1]))

    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    cv2.imshow('thresh', thresh)

    _, cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if len(cnts) > 0:
        max_area1 = 1
	#max_area2 = 1
        c1 = 0
	#c2 = 0
        for i in range(len(cnts)):
            cnt = cnts[i]
            area = cv2.contourArea(cnt)
            if (area > max_area1):
		#max_area2 = max_area1
                max_area1 = area
                c1 = i

        ((x1, y1), radius1) = cv2.minEnclosingCircle(cnts[c1])
	#((x2, y2), radius2) = cv2.minEnclosingCircle(cnts[c2])
        M1 = cv2.moments(cnts[c1])
        center1=(0,0)
 	#center2=(0,0)
        if int(M1["m00"]) != 0:# and int(M2["m00"]) != 0:
            center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))
	    #center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))

        #print (x1, y1, x2, y2)
	#print (x1, y1)
	#file.write(str(x1)+'			'+str(y1)+'			'+str(x2)+'			'+str(y2)+'\n')
	file.write(str(x1)+'			'+str(y1)+'\n')

        cv2.line(frame, center1, center1, (255, 255, 255), 7)
        #cv2.line(frame, center2, center2, (255, 255, 255), 7)
        
    cv2.imshow('live',frame)
   
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
