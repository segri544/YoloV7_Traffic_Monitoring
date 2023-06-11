import cv2
import torch
import numpy as np
from tracker import *


path='C:/Users/Administrator/AppData/Local/Programs/Python/Python38/Lib/site-packages/yolov5/yolov5s-int8.tflite'

model = torch.hub.load('C:/Users/Administrator/AppData/Local/Programs/Python/Python38/Lib/site-packages/yolov5', 'custom', path,source='local')

model.classes = [2,3,5,7]

area1=[(0,0),(1019,0),(0,599),(1019,599)]#
area_1=set()
cap=cv2.VideoCapture('vid2.mp4')

count=0
tracker = Tracker()
total=0



def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', POINTS)

while True:
    ret,frame=cap.read()
    if not ret:
        break
    count += 1
    if count % 10 != 0:
        continue
    frame=cv2.resize(frame,(1020,600))
    #cv2.polylines(frame,[np.array(area1,np.int32)],True,(255,0,255),2)
    results=model(frame)
    list=[]
    for index,rows in results.pandas().xyxy[0].iterrows():
        x=int(rows[0])
        y=int(rows[1])
        x1=int(rows[2])
        y1=int(rows[3])
        b=str(rows['name'])
        # cv2.rectangle(frame,(x,y),(x1,y1),(0,0,255),2)
        list.append([x,y,x1,y1])
    idx_bbox=tracker.update(list)
    for bbox in idx_bbox:
        x2,y2,x3,y3,id = bbox
        cv2.rectangle(frame,(x2,y2),(x3,y3),(0,0,255),2)
        cv2.putText(frame,str(id),(x2,y2),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
        cv2.circle(frame,(x3,y3),3,(0,255,0),-1)
        result = cv2.pointPolygonTest(np.array(area1,np.int32),(x3,y3),False)
        if result > 0:
            area_1.add(id)
        
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(255,0,255),2)
    a1=len(area_1)
    print(a1)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(0)&0xFF==27: 
        break
cap.release()
cv2.destroyAllWindows()
