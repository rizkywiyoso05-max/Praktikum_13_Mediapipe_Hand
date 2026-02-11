import  cv2 #import module openCV
import  mediapipe

capture = cv2.VideoCapture(0) #video capture pada device kamera nomer 1
mediapipehand = mediapipe. solutions .hands
tangan = mediapipehand.Hands()  #variable tangan untuk menyimpan konfigurasi deteksi tangan

while True:
    success, img = capture.read() #menyimpan citra tangkapan kamera ke img
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #merubah warna img ke RGB
    result=tangan.process(imgRGB) #melakukan pemrosesan dari citra imgRGB
    if result.multi_hand_landmarks:
        print("tangan") #ketika tangan terdeteksi menampilkan "tangan" pada terminal
    else:
        print("tidak ada") #ketika tangan terdeteksi menampilkan "tidak ada" pada terminal

    cv2.imshow("webcam",img)
    cv2.waitKey(10)
    if cv2.waitKey (10) & 0xFF == ord('q'):
        break

capture.release() # Tutup wabcam dan jendela tampilan saat 1 ditekan
cv2.destroyAllWindows()




