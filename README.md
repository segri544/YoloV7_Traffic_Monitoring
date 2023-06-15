### Traffic monitoring with yolov7
This repository contains the implementation of YOLOv7-based vehicle detection and counting system using Python. The system is designed to detect and count vehicles in real-time from video or image inputs, providing valuable traffic data for road analysis. It also supports the use of a CSI camera on Jetson Nano.

## Features
* Real-time vehicle detection and counting
* Support for video and image inputs
* Efficient and accurate vehicle detection using YOLOv7
* Easy-to-use Python API for integrating into your projects
* CSI camera support for Jetson Nano

# Test samples
![Ekran Görüntüsü (602)](https://github.com/segri544/YoloV7_Traffic_Monitoring/assets/111482228/1ff7b559-1df0-4e5c-8d91-c98e9c10fa09)
for more samples check https://www.youtube.com/channel/UCqv1qrgRdgH8aCm-YG47qPA

# Commands
1. python detect.py --weights 982-11mb.pt  --view-img --source video.mp4  --show-fps  

2. python detectpy --weights 982-47mb.pt  --view-img --nosave --source 0  --show-fps --conf 0.5  --seed 2 --track

3. python detect.py --weights 982-11mb.pt  --view-img --nosave --source image.jpg --show-fps --conf 0.5 



## İmportant Note
To run it on jetson nano with CSI camera (considering all configurations have done) utils/dataset.py should be changed to frame is taken by a CSI camera. it is recommended to check face_detect.py from https://github.com/JetsonHacksNano/CSI-Camera/blob/master/face_detect.py

## Referances 
* https://github.com/WongKinYiu/yolov7
* https://github.com/RizwanMunawar/yolov7-object-tracking/
* https://github.com/krisnarengga/yolov7-vehicle-counting

