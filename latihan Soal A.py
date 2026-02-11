import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
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

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand in enumerate(results.multi_handedness):
            label = hand.classification[0].label  # kanan / kiri

            if label == "Right":
                cv2.putText(frame, "TANGAN KANAN", (50, 50),
                            cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            else:
                cv2.putText(frame, "TANGAN KIRI", (50, 50),
                            cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            mp_draw.draw_landmarks(
                frame,
                results.multi_hand_landmarks[idx],
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Deteksi Kanan & Kiri", frame)

    if cv2.waitKey(1) & 0xFF == 28:
        break

cap.release()
cv2.destroyAllWindows()
