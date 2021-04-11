import cv2
import sys

imagePath = sys.argv[1]
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read and convert the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect the faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
)
print("Found {0} faces!".format(len(faces)))

# show face detections
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Faces found", image)
if len(sys.argv)>=3:
    cv2.imwrite(sys.argv[2], image)
while not cv2.waitKey(0):
    break