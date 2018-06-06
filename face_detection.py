import sys, cv2 as cv
def chooseAndUse(event):
    global mode
    
Mode0Cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
Mode1Cascade = cv.CascadeClassifier('haarcascade_eye.xml')
Mode11Cascade = cv.CascadeClassifier('haarcascade_profileface.xml')
Mode2Cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')
numberPhoto = 0
mode = 0
cap = cv.VideoCapture(0)
eye_color = (255,255,255)
body_color = (255,255,255)
edge_color = (255,255,255)
#Инициализация для захвата с веб-камеры 
while True:
    time = cv.getTickCount() / cv.getTickFrequency()
    ok, img = cap.read() #Загружаем очередной кадр
    if not ok:
        break
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    if (mode == 0):
        students = Mode0Cascade.detectMultiScale(gray, 1.3, 5)
        students1 = Mode11Cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in students1:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
            roi_gray1 = gray[y:y+h, x:x+w]
            roi_color1 = img[y:y+h, x:x+w]
        numberPhoto = len(students)+len(students1)
        #blur = cv.GaussianBlur(img,(7,7),1.5)
    if (mode == 1):
        students = Mode0Cascade.detectMultiScale(gray, 1.3, 5)
        students_eyes = Mode1Cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in students_eyes:
            cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
            roi1_gray = gray[y:y+h, x:x+w]
            roi1_color = img[y:y+h, x:x+w]
    if (mode == 2):
        students = Mode2Cascade.detectMultiScale(gray, 1.3, 5)
    if (mode == 9):
        edge = cv.Canny(gray, 1,50)
        img [edge == 0] = (255,255,255)
        img [edge != 0] = (255,0,0)
        
    time = cv.getTickCount() / cv.getTickFrequency() - time
    cv.putText(img,"DETECTED HUMANS:"+str(numberPhoto),(23,40), cv.FONT_HERSHEY_PLAIN, 1.0, (255,0,255),2)
    cv.putText(img,"DETECTED HUMANS:"+str(numberPhoto),(20,40), cv.FONT_HERSHEY_PLAIN, 1.0, (255,255,255),2)
    cv.putText(img,"1 - EYES DETECTION", (11,471), cv.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), 2)
    cv.putText(img,"1 - EYES DETECTION", (10,470), cv.FONT_HERSHEY_PLAIN, 1.0, eye_color, 2)
    cv.putText(img,"Time: %.4f ms" %(time), (20, 20), cv.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), 2)
    cv.putText(img,"Time: %.4f ms" %(time), (20, 20), cv.FONT_HERSHEY_PLAIN, 1.0, (255,255,255), 1)
    cv.putText(img,"ESC - EXIT", (540, 20), cv.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), 2)
    cv.putText(img,"ESC - EXIT", (540, 20), cv.FONT_HERSHEY_PLAIN, 1.0, (255,255,255), 1)
    
    cv.putText(img,"2 - BODY DETECTION", (191,470), cv.FONT_HERSHEY_PLAIN, 1.0, body_color, 2)
    cv.putText(img,"9 - EDGES", (500,470), cv.FONT_HERSHEY_PLAIN, 1.0, edge_color, 2)
    if (mode !=9):
        for (x,y,w,h) in students:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            #cv.imwrite('%d.jpg'%numberPhoto, img)
    numberPhoto = len(students)
    #Конвертируем цветное изображение в монохромное
    #gray = cv.GaussianBlur(gray, (7, 7), 1.5)
    
    #Добавляем размытие
    #edges = cv.Canny(gray, 1, 50) #Детектируем ребра
    cv.imshow('img',img)
    #print (numberPhoto)
    #cv.imshow("edges", edges) #Отображаем результат
    ch=cv.waitKey(1)
    print (ch)
    if ch == 49:
        mode = 1
        eye_color = (0,255,0)
        body_color = (255,255,255)
        edge_color = (255,255,255)
    if ch == 50:
        mode = 2
        eye_color = (255,255,255)
        body_color = (0,255,0)
        edge_color = (255,255,255)
    if ch == 57:
        mode = 9
        eye_color = (255,255,255)
        body_color = (255,255,255)
        edge_color = (0,255,0)
    if ch == 48:
        mode = 0
        eye_color = (255,255,255)
        body_color = (255,255,255)
        edge_color = (255,255,255)
    if ch == 27:
        break
    #if cv.waitKey(30) > 0:
    #    break 
cv.destroyAllWindows()
numberPhoto = str(numberPhoto)
f = open('log.txt', 'w')
f.write(numberPhoto)
f.close()
