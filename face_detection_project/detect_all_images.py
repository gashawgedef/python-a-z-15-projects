import cv2
import glob
import os

# Define the folder containing the images and the Haar Cascade file
folder_path = "C:\\Users\\ggashaw\\Desktop\\python-a-z-15-projects\\face_detection_project"
os.chdir(folder_path)  # Change the current working directory to the folder_path
cascade_path = os.path.join(folder_path, "haarcascade_frontalface_default.xml")
detect = cv2.CascadeClassifier(cascade_path)


# Find all .jpg images in the folder
all_images = glob.glob("*.jpg")
for image in all_images:
    img = cv2.imread(image)
    gray_image  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    faces = detect.detectMultiScale(gray_image,1.1,5)

    for (x,y,w,h) in faces:
        final_img = cv2.rectangle(img,(x,y),(x+y,y+h),(0,255,0),2)
    cv2.imshow("Face Detection",final_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()