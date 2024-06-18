
###for images
# import cv2

# # load pretrained data on faces frontal from opencv
# trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # choose a imaget o detect faces in
# img = cv2.imread('rdjr.jpg') # image read function

# # convert to grayscale
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Detect faces
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img) # multiscale can detect different sizes

# # print(face_coordinates)

# # Draw rectangles around faces
# for(x ,y ,w ,h) in face_coordinates:
#   (x, y, w ,h) = face_coordinates[0]
#   cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) # img, coordinates, color, width

# # show image
# cv2.imshow('Clever programmer Face Detector', img)
# cv2.waitKey() # image will close imediately when program is done so we need to pause execution

# print("Code completed!!")

###for video
import cv2

# load pretrained data on faces frontal from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose a imaget o detect faces in
# webcam = cv2.VideoCapture(0) # should go to default camera with 0
webcam = cv2.VideoCapture('IMG_3529.mp4') # should go to default camera with 0

while True:
  successful_frame_read, frame = webcam.read()

  # convert to grayscale
  grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect faces
  face_coordinates = trained_face_data.detectMultiScale(grayscaled_img) # multiscale can detect different sizes

  # Draw rectangles around faces
  for(x ,y ,w ,h) in face_coordinates:
    (x, y, w ,h) = face_coordinates[0]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # img, coordinates, color, width

  # show image
  cv2.imshow('Clever programmer Face Detector', frame)
  key = cv2.waitKey(1) # image will close imediately when program is done so we need to pause execution

  # stop if key is pressed
  if key == 81 or key == 113:
    break

webcam.release()

print("Code completed!!")

# 1:30:38