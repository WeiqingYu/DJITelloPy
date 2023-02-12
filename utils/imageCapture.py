from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()

print(me.get_battery())

cnt = 0
while True:
    img = me.get_frame_read().frame
    print(img)
    cnt += 1
    print(cnt)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

