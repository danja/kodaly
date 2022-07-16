# program to capture single image from webcam in python

# importing OpenCV library
import cv2

# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
camera_port = 0
camera = cv2.VideoCapture(camera_port)

# reading the input using the camera
result, image = camera.read()

if result:
    cv2.imshow("dan1", image)
# saving image in local storage
    cv2.imwrite("dan1.png", image)

    cv2.waitKey(0)
    cv2.destroyWindow("dan1")
else:
    print("Fail!")
