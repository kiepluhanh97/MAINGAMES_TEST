from randimage import get_random_image, show_array
from os import listdir
import os
import cv2
import random
import time
import numpy as np
import matplotlib
img_size = (30,40)
# yolo_size = 416
# root_size = (416,416)
NUM_IMG = 20
images_folder = './characters/'
dataset_folder = './dataset/'
if not os.path.exists(dataset_folder):
    os.mkdir(dataset_folder)
for eachFile in listdir(dataset_folder):
    os.remove(dataset_folder + eachFile)
f = open('./class_list.txt')
labels = f.read().split('\n')
numImg = 1
for i in range(NUM_IMG):
    for eachImg in listdir(images_folder):
        charName = eachImg[:len(eachImg) - 4]
        index = labels.index(charName)
        if index >= 0:
            char_img = cv2.imread(images_folder + eachImg)
            # cv2.imshow('check', char_img)
            # cv2.waitKey()
            # char_img = cv2.resize(char_img, (20,20))
            c_h,c_w = char_img.shape[:2]
            print(c_h,c_w)
            time1 = time.time()
            img = get_random_image(img_size)  #returns numpy array
            matplotlib.image.imsave("check.jpg", img)
            big_img = cv2.imread('check.jpg')
            print('Time create img: ', time.time() - time1)
            x_offset = random.randint(5, 15)
            y_offset = random.randint(2,8)
            cx,cy = x_offset + c_w/2, y_offset + c_h/2

            stringWrite = str(index) + ' ' + str(cx/img_size[1]) + ' ' + str(cy/img_size[0]) + ' ' + str(c_w/img_size[1]) + ' ' + str(c_h/img_size[0]) + '\n'

            newWrapimg = big_img[y_offset:y_offset + c_h, x_offset:x_offset + c_w]
            # Create a mask with a circle of the desired size
            mask = np.zeros_like(newWrapimg)
            circle_center = tuple(np.array(newWrapimg.shape[:2]) // 2)
            circle_radius = c_w // 2
            cv2.circle(mask, circle_center, circle_radius, (255, 255, 255), -1)

            # Paste the small image onto the big image using the mask
            output_img = np.zeros_like(newWrapimg)
            output_img[mask == 255] = char_img[mask == 255]
            output_img[mask == 0] = newWrapimg[mask == 0]

            big_img[y_offset:y_offset + 20, x_offset: x_offset+20] = output_img
            big_img = cv2.resize(big_img, (416,416))
            cv2.imwrite(dataset_folder + str(numImg) + '.jpg', big_img)
            f = open(dataset_folder + str(numImg) + '.txt', 'a')
            f.write(stringWrite)
            f.close()
            numImg += 1

