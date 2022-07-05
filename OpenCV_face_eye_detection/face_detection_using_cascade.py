import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# For Photo
# image = cv2.imread("photo.jpg")
# For video
cap = cv2.VideoCapture("vid.mp4")
while(cap.isOpened()):
    _ , image = cap.read()

    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(image , 1.04, 6)

    for (x ,y, w, h) in face:
        cv2.rectangle(image , (x,y) , (x+w , y+h) , (0,255,0) , 3 )

    cv2.imshow("Image" , image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()