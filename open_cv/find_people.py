import cv2

# Load the image
image = cv2.imread('people.jpg')

# Create a HOG Descriptor object
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Detect people in the image
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

# Draw the bounding boxes around the detected people
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with the bounding boxes
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
