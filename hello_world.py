import cv2

'''
Add function
'''
def add(a,b):
  return a+b

c = add (2,3)
print(f"added: {c}")

"""
Change
"""
width = 500

print("First change")

im = cv2.imread('det.jpg')

im = cv2.resize(im, (width,width))

cv2.imshow('file', im)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Exiting")
