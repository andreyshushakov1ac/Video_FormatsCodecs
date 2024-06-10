import cv2
cap = cv2.VideoCapture(0) #Открываем видеопоток с веб-камеры
fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
out = cv2.VideoWriter('MJPG.wmv',fourcc, 20.0, (640,480)) 
#Список идентификаторов fourcc:
# DIVX = DIVX
# XVID = XVID
# MJPG = Motion JPEG
# X264 = H.264
# AVC1 = AVC1
# MP4V = MPEG-4 Video
# WMV1 = WMV1
# WMV2 = WMV2
# WMV3 = WMV3
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret==True:
    frame = frame
    out.write(frame) #Записываем кадр
    cv2.imshow('frame',frame) #Отображаем кадр в окне
    if cv2.waitKey(25) & 0xFF == ord('q'): #Закончить запись по нажатии клавиши "q"
      break
  else:
    break
cap.release()
out.release
cv2.destroyAllWindows()
