import cv2
import numpy as np

cv2.namedWindow("Face_Detect")
cap = cv2.VideoCapture(0)
success, frame = cap.read()
path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/cv2/data/'
classifier = cv2.CascadeClassifier(path + "haarcascade_frontalface_default.xml")

while success:
    success, frame = cap.read()
    size = frame.shape[:2]
    image = np.zeros(size, dtype=np.float16)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.equalizeHist(image, image)
    divisor = 8
    h, w = size
    #像素一定是整数，或者用w//divisor
    minSize = (w//divisor, h//divisor)
    faceRects = classifier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)

    if len(faceRects) > 0:
        for faceRect in faceRects:
            x, y, w, h = faceRect
            #圆形轮廓
            cv2.circle(frame, (x+w//2, y+h//2), min(w//2, h//2), (255, 0, 0), 2)
            #左眼轮廓
            cv2.circle(frame, (x+w//4, y+2*h//5), min(w//8, h//8), (0, 255, 0), 2)
            #右眼轮廓
            cv2.circle(frame, (x+3*w//4, y+2*h//5), min(w//8, h//8), (0, 255, 0), 2)
            #鼻子轮廓
            cv2.circle(frame, (x+w//2, y+2*h//3), min(w//8, h//8), (0, 255, 0), 2)
            #矩形轮廓
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("Face_Detect", frame)
key = cv2.waitKey(10)
c = chr(key & 255)
if c in ['q', 'Q', chr(27)]:
    print('exit')

 #循环结束则清零
cap.release()
cv2.destroyAllWindows()
