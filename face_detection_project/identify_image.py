import cv2
# detect= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# imp_img = cv2.VideoCapture("gggg.jpg")
# res,img =imp_img.read()
# # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # faces = detect.detectMultiScale(gray,1.3,5)
# cv2.imshow("Gashaw Image",img)
# cv2.waitKey(0)
# imp_img.release()
# cv2.destroyAllWindows()import cv2

# Load the pre-trained model for face detection
file_path = "C:\\Users\\ggashaw\\Desktop\\python-a-z-15-projects\\face_detection_project\\haarcascade_frontalface_default.xml"
print("Attempting to load:", file_path)

# Load the pre-trained model for face detection
detect = cv2.CascadeClassifier(file_path)
if detect.empty():
    print("Error: Unable to load the face detection model.")
    exit()


# Read the image
imp_img = cv2.VideoCapture("C:\\Users\\ggashaw\\Desktop\\python-a-z-15-projects\\face_detection_project\\gggg.jpg")
if not imp_img.isOpened():
    print("Error: Unable to open the image.")
    exit()

ret, img = imp_img.read()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = detect.detectMultiScale(gray,1.3,5)
if not ret:
    print("Error: Unable to read the image.")
    exit()
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
# Display the image
cv2.imshow("Gashaw Image", img)
cv2.waitKey(0)

# Release resources
imp_img.release()
cv2.destroyAllWindows()

