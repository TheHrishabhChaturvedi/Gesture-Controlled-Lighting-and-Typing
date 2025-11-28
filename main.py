
import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=1)
video = cv2.VideoCapture(0)
finger_labels = ['5','1', '2', '3', '4']
last_state = [0, 0, 0, 0, 0]
activation_time = [None, None, None, None, None]
typed_digits = ""
frame_count = 0
while True:
 ret, frame = video.read()
 frame = cv2.flip(frame, 1)
 hands, img = detector.findHands(frame)
 frame_count += 1
 display_text = ""
 if hands:
 lmList = hands[0]
 fingerUp = detector.fingersUp(lmList)
 if fingerUp == [0, 1, 0, 0, 1]:
 typed_digits = ""
 display_text = "Reset Triggered"
 elif fingerUp == [0, 0, 0, 0, 0] and last_state != [0, 0, 0, 0, 0]:
 typed_digits += '0'
 display_text = "Typed: 0"
else:
 for i in range(5):
 if fingerUp[i] == 1 and last_state[i] == 0:
 activation_time[i] = frame_count
 elif fingerUp[i] == 0:
 activation_time[i] = None
 active_fingers = [(i, activation_time[i]) for i in range(5) if activation_time[i] is not None]
 active_fingers.sort(key=lambda x: x[1])
 for i, _ in active_fingers:
 typed_digits += finger_labels[i]
 display_text = f"Typed: {finger_labels[i]}"
 activation_time[i] = None
 last_state = fingerUp.copy()
 cnt.led(fingerUp)
 cv2.putText(frame, f'Digits: {typed_digits}', (20, 420),
 cv2.FONT_HERSHEY_COMPLEX, 1.2, (255, 255, 0), 2)
 if display_text:
 cv2.putText(frame, display_text, (20, 460),
 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
 cv2.imshow("frame", frame)
 k = cv2.waitKey(1)
 if k == ord("k") or len(typed_digits) >= 10:
 break
video.release()
cv2.destroyAllWindows()
