from randimage import get_random_image, show_array
from os import listdir
import os
import cv2
import random
import time
import numpy as np
import matplotlib
img_size = (50,50)
NUM_IMG = 10
images_folder = './characters/'
dataset_folder = './dataset/'
if not os.path.exists(dataset_folder):
    os.mkdir(dataset_folder)
for eachFile in listdir(dataset_folder):
    os.remove(dataset_folder + eachFile)

numImg = 1
for i in range(NUM_IMG):
    for eachImg in listdir(images_folder):
        char_img = cv2.imread(images_folder + eachImg)
        # cv2.imshow('check', char_img)
        # cv2.waitKey()
        char_img = cv2.resize(char_img, (40,40))
        c_h,c_w = char_img.shape[:2]
        print(c_h,c_w)
        time1 = time.time()
        img = get_random_image(img_size)  #returns numpy array
        matplotlib.image.imsave("check.jpg", img)
        img = cv2.imread('check.jpg')
        big_img = cv2.resize(img, (416,416))
        print('Time create img: ', time.time() - time1)
        x_offset = random.randint(10, 416-10-c_w)
        y_offset = random.randint(10,40)


        dim = (c_w, c_h)
        small_img_resized = cv2.resize(char_img, dim, interpolation=cv2.INTER_AREA)

        # Create circular mask
        mask = np.zeros(small_img_resized.shape[:2], dtype=np.uint8)
        center = (int(mask.shape[1]/2), int(mask.shape[0]/2))
        radius = int(min(mask.shape)/2)
        cv2.circle(mask, center, radius, 255, -1)

        # Resize mask to match big image size
        mask_resized = cv2.resize(mask, (big_img.shape[1], big_img.shape[0]), interpolation=cv2.INTER_AREA)

        # Create complement mask
        complement_mask = cv2.bitwise_not(mask_resized)

        # Combine the two masks
        combined_mask = cv2.bitwise_or(mask_resized, complement_mask)

        # Apply mask to small image
        small_img_masked = cv2.bitwise_and(small_img_resized, small_img_resized, mask=mask)

        # Paste small image onto big image within the circle
        big_img_masked = big_img.copy()
        big_img_masked[y_offset:y_offset+small_img_masked.shape[0], x_offset:x_offset+small_img_masked.shape[1]] = small_img_masked

        # Apply combined mask to big image
        big_img_masked = cv2.bitwise_and(big_img_masked, big_img_masked, mask=combined_mask)
        # img = img.astype(np.uint8)
        cv2.imwrite(dataset_folder + str(numImg) + '.jpg', big_img_masked)
        numImg += 1




