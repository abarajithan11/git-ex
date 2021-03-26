import cv2

print("Hello world")
print("More code")

width = 500

print("First change")

im = cv2.imread('det.jpg')

im = cv2.resize(im, (width,width))

cv2.imshow('file', im)
cv2.waitKey(0)
cv2.destroyAllWindows()