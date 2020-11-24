#program wajah menggunakan wajah
import pyttsx3
import cv2
import os
import time
import threading
cam = cv2.VideoCapture(0)                                                                   #untuk membuka webcam angka 0 merupakan port dari camera saya (setiap device orang berbeda port cameranya) jadi tidak harus 0
cam.set(3, 1280)                                                                            # angka 3 disini diartikan sebagai get_funtion_width yaitu CV_CAP_PROP_FRAME_WIDTH dengan ini artinya mengatur lebar aplikasi dari cam kita dengan cam sebagai self function yang berisi cv2.VideoCapture
cam.set(4, 1024)                                                                            # angka 4 disini diartikan sebagai get_funtion_height yaitu CV_CAP_PROP_FRAME_HEIGHT dengan ini artinya mengatur tinggi aplikasi dari cam kita
facedetector = cv2.CascadeClassifier('haarcascade_frontalface_default.XML')                 # untuk membaca file .XML yaitu haarcascade.XML/ berisi kumpulan pengaturan yang berisi mengenai rectangle dan pendeteksian otomatis skala pada gambar/video dalam hal ini haarcascade berisi pengaturan yang bersangkutan dengan deteksi jumlah wajah
noisedetector = cv2.CascadeClassifier('Nariz.XML')                                          # untuk membaca file .XML yaitu Nariz.XML/ berisi kumpulan pengaturan yang berisi mengenai rectangle dan pendeteksian otomatis skala pada gambar/video dalam hal ini Nariz.XML berisi pengaturan yang bersangkutan dengan noise detection
mask_on = False        #mask_on = false diartikan sebagai ketika wajah tampil tidak menggunakan masker  dalam camera maka mendeteksi orang tersebut tidak memakai masker
wajahpath=r'E://DATA'

def alarmdeteksi(engine):
    try:
        engine.say("Masker Off")
        engine.runAndWait()
    except:
        None
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',100)

Status=["Mask On", "Mask Off"]
while True:                                                                                 # while disini berfungsi untuk menangkap frame by frame yang artinya fungsi rectangle , fungsi text cvnya yang akan ditangkap dalam video
    retV, frame = cam.read()                                                                #membaca code cam yang dimana code cam berisi video webcam kita
                                                                                            #cvtColor dalam opencv berfungsi untuk mengconvert warna baik itu video atau foto, dalam hal ini variable gray tidak ditampilkan dalam layar (hanya alternatif)
    muka = facedetector.detectMultiScale(image=frame, scaleFactor=1.3, minNeighbors=3)      #detectMultiScale berfungsi sebagai pendeteksian scala video ,yang disini


    for (x,y,w,h) in muka:                                                                   #dalam hal ini butuh perulangan for agar membuat frame rectangle yang berguna untuk mendeteksi wajah akan tampil terus-menerus  dengan variable buatan (x,y,w,h)
            if mask_on:
                frame = cv2.rectangle(frame, (x,y),(x+w,y+h),color=(0,255,0),thickness=2)
                cv2.putText(frame,Status[0],(x,y),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1.5,color=(0,255,0),thickness=2)
            else:
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, Status[1], (x, y), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 0, 255), 2)
                if Status[1]:
                        alarm = threading.Thread(target=alarmdeteksi, args=(engine,))
                        alarm.start()



    hidung = noisedetector.detectMultiScale(frame,1.9,5)                #fungsi code ini untuk membaca Nariz.XML yang berisikan setting detectMultiscale seberapa akurat untuk prosesing detectnya
    for (sx,sy,sw,sh) in hidung:
        cv2.rectangle(frame, (sx, sy), (sx + sw, sy + sh), (255, 255, 0), 4)
        cv2.putText(frame, 'hidung', (sx + sw, sy + sh), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)

    if len(hidung)>0:
        mask_on = False     #Jadi ketika jumlah dari hidung = 0 ,maka mask_on = False yang artinya nantinya mask_on akan bernilai salah dan akan masuk pada perintah else seperti code di atas dengan output =status[1]=mask off
    else:
        mask_on = True



    cv2.putText(frame,'Jumlah Wajah: '+ str(len(muka)),(20,60),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)   #peraturan mengenai text dalam video yaitu jumlah wajah yang berada pojok kiri atas
    cv2.imshow("webcam ku",frame)          # menampilkan tampilan program dengan judul webcamku, dan frame adalah isi                                                              #berfungsi sebagai menampilkan camera dengan judul "webcam ku" yang akan mengeluarkan variable  frame

    if cv2.waitKey(1) & 0xFF==ord('x'):
        break




cam.release()
cv2.destroyAllWindows()                                                                                    # Berfungsi untuk menghentikan selagi webcam sedang dipakai ,jadi ketika ingin menjalankan program ini, maka yang masih menggunakan webcam harus di close/dimatikan dulu camnya