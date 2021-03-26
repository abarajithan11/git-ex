import cv2

print("Hello world")
print("More code")

print("First change")

im = cv2.imread('det.jpg')

im = cv2.resize(im, (500,500))

cv2.imshow('file', im)
cv2.waitKey(0)
cv2.destroyAllWindows()