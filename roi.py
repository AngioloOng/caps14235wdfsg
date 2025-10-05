import cv2

im = cv2.imread('imgtest1.jpg')

roi = cv2.selectROI(im)

print(roi) 

im_cropped = im[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

cv2.imwrite('output.jpg', im_cropped)
cv2.destroyAllWindows()