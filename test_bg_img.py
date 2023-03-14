from randimage import get_random_image, show_array
import matplotlib
import cv2
img_size = (100,100)
img = get_random_image(img_size)  #returns numpy array
print(img)
matplotlib.image.imsave("check.jpg", img)
img2 = cv2.imread('check.jpg')
print(img2)
# cv2.imwrite('check2.jpg', img)