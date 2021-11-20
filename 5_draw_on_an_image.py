import numpy as np
import cv2



def draw_circle(event,x,y,flags,param):
    if (event==cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img,center=(x,y),radius=50,color=(0,255,0),thickness=-1)
    elif (event==cv2.EVENT_RBUTTONDOWN):
        cv2.circle(img,center=(x,y),radius=50,color=(255,0,0),thickness=-1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

img=np.zeros((512,512,3),dtype=np.uint8)
while True:
    cv2.imshow('my_drawing',img)


    #if we have waited at least 1ms and we have pressed ESC.
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()