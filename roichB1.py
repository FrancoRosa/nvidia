import cv2
from ultralytics import YOLO
# pipeline below worked on Jetson and x86
cap = cv2.VideoCapture("thetauvcsrc \
    ! decodebin \
    ! autovideoconvert \
    ! video/x-raw,format=BGRx \
    ! queue ! videoconvert \
    ! queue max-size-buffers=1 leaky=downstream \
    ! appsink drop=true max-buffers=1 sync=false")
model = YOLO("yolov8n.pt")

# pipeline suggestion thanks to nickel110
# attempt to force hardware acceleration
# tested with NVIDIA 510.73 with old GTX 950 on Ubuntu 22.04
# cap = cv2.VideoCapture("thetauvcsrc \
#     ! queue \
#     ! h264parse \
#     ! nvdec \
#     ! gldownload \
#     ! queue \
#     ! videoconvert n-threads=0 \
#     ! video/x-raw,format=BGR \
#     ! queue \
#     ! appsink")

# NVIDIA Jetson
# cap = cv2.VideoCapture("thetauvcsrc \
#     ! nvv4l2decoder \
#     ! nvvidconv \
#     ! video/x-raw,format=BGRx \
#     ! queue ! videoconvert \
#     ! video/x-raw,format=BGR ! queue ! appsink")

if not cap.isOpened():
    raise IOError('Cannot open RICOH THETA')

while True:
    ret, frame = cap.read()
    results = model(frame)
    # frame = cv2.resize(frame, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    cv2.imshow('frame', results[0].plot())

    while cv2.getWindowProperty('frame', 0) == 0:
        ret, frame = cap.read()
        results = model(frame)
        cv2.imshow('frame', results[0].plot())

        if cv2.waitKey(1) & 0xFF == ord("q"):
            stop_event.set()
            break

    break
cap.release()
cv2.destroyAllWindows()
