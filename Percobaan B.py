import cv2 #import module opencv
import mediapipe
capture = cv2.VideoCapture(0)
mediapipehand = mediapipe.solutions.hands
tangan = mediapipehand.Hands(max_num_hands=1)
mediapipedraw = mediapipe.solutions.drawing_utils

while True:
    success, image = capture.read() #read video frame by frame
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = tangan.process(imgRGB)
    if results.multi_hand_landmarks:
        for titiktangan in results.multi_hand_landmarks:
            mediapipedraw.draw_landmarks(image, titiktangan,mediapipehand.HAND_CONNECTIONS)
            for id, titik in enumerate(titiktangan.landmark):
                print (id)
                print (titik.x)
                print (titik.y)
    cv2.imshow("webcam", image)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break # Tutup webcam dan jendela tampilan q ditekan
capture.release()
cv2.destroyAllWindows()