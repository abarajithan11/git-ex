import cv2

print("Hello world")
print("More code")

print("First change")

im = cv2.imread('det.jpg')

cv2.imshow('file', im)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Exiting")
