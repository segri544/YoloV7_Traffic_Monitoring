import os 


os.system('cmd /c "python detect_or_track.py --weights yolov7.pt --no-trace --view-img --nosave --source vid2.mp4 --show-fps --seed 2 --track --classes 2 3 5 7 --show-track  --unique-track-color --nobbox "')

