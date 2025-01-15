import cv2
cap = cv2.VideoCapture("thetauvcsrc \
    ! decodebin \
    ! autovideoconvert \
    ! video/x-raw,format=BGRx\
    ! queue ! videoconvert \
    ! queue max-size-buffers=1 leaky=downstream \
    ! appsink drop=true max-buffers=1 sync=false")


if not cap.isOpened():
    raise IOError('Cannot open RICOH THETA')

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    while cv2.getWindowProperty('frame', 0) == 0:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    break
cap.release()
cv2.destroyAllWindows()
