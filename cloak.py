import cv2
import numpy as np

def princess(x):
    print("")

cap=cv2.VideoCapture(0)
bars=cv2.namedWindow("bars")

cv2.createTrackbar("upper_hue","bars",128,100,princess)
cv2.createTrackbar("upper_saturation","bars",255,5,princess)
cv2.createTrackbar("upper_value","bars",255,255,princess)
cv2.createTrackbar("lower_saturation","bars",50,180,princess)
cv2.createTrackbar("lower_hue","bars",90,255,princess)
cv2.createTrackbar("lower_value","bars",70,255,princess)

while(True):
    cv2.waitKey(1000)
    ret,init_frame=cap.read()
    if(ret):
        break

while(True):
    ret,frame=cap.read()
    inspect=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    upper_hue=cv2.getTrackbarPos("upper_hue","bars")
    upper_saturation=cv2.getTrackbarPos("upper_saturation","bars")
    upper_value=cv2.getTrackbarPos("upper_value","bars")
    lower_hue=cv2.getTrackbarPos("lower_hue","bars")
    lower_saturation=cv2.getTrackbarPos("lower_saturation","bars")
    lower_value=cv2.getTrackbarPos("lower_value","bars")

    kernel=np.ones((3,3),np.uint8)

    upper_hsv=np.array([upper_hue,upper_saturation,upper_value])
    lower_hsv=np.array([lower_hue,lower_saturation,lower_value])

    mask=cv2.inRange(inspect,lower_hsv,upper_hsv)
    mask=cv2.medianBlur(mask,3)
    mask_inv=255-mask
    mask=cv2.dilate(mask,kernel,5)

    b=frame[:,:,0]
    g=frame[:,:,1]
    r=frame[:,:,2]
    b=cv2.bitwise_and(mask_inv,b)
    g=cv2.bitwise_and(mask_inv,g)
    r=cv2.bitwise_and(mask_inv,r)
    frame_inv=cv2.merge((b,g,r))

    b=init_frame[:,:,0]
    g=init_frame[:,:,1]
    r=init_frame[:,:,2]
    b=cv2.bitwise_and(b,mask)
    g=cv2.bitwise_and(g,mask)
    r=cv2.bitwise_and(r,mask)
    blanket_area=cv2.merge((b,g,r))

    final=cv2.bitwise_or(frame_inv,blanket_area)

    cv2.imshow('harry',final)
    cv2.imshow('real',frame)

    if(cv2.waitKey(3)==ord('q')):
        break;
    

cv2.destroyAllWindows()
cap.release()





    

    


