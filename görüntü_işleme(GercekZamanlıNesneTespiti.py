import cv2;
import numpy as np;

camera=cv2.VideoCapture(0)

while(True):
    ret,video=camera.read()
    hsv=cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,129,14])
    upper_red=np.array([2,204,250])
    sb=cv2.inRange(hsv,lower_red,upper_red)
    renk=cv2.bitwise_and(video,video,mask=sb)
    cv2=imshow("Renkli",renk)
    cv2=imshow("Siyah-Beyaz",sb)
    if cv2.waitkey(50)& 0xFF==ord('x'):
        break

camera.release()
cv2.destroyAllWindows()