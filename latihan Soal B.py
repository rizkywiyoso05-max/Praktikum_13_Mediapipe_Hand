import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            wrist = landmarks.landmark[0]
            index_mcp = landmarks.landmark[5]
            pinky_mcp = landmarks.landmark[17]

            # Deteksi telapak / punggung
            if index_mcp.x < pinky_mcp.x:
                posisi = "TELAPAK (DEPAN)"
                warna = (0, 255, 0)
            else:
                posisi = "PUNGGUNG (BELAKANG)"
                warna = (0, 255, 255)

            cv2.putText(frame, posisi, (50, 50),
                        cv2.FONT_HERSHEY_PLAIN, 3, warna, 3)

            mp_draw.draw_landmarks(
                frame,
                landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Deteksi Depan & Belakang", frame)

    if cv2.waitKey(1) & 0xFF == 28:
        break

cap.release()
cv2.destroyAllWindows()
