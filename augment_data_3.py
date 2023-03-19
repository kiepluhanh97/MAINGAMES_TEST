import os
from os import listdir
import cv2
import imgaug.augmenters as iaa
from random import seed
from random import randint
from shutil import copy
seed(1)

folder_images = './dataset/'
folder_txts = './dataset/'

des_images = './dataset_aug_3/'
des_txts = './dataset_aug_3/'

listImgs = []
for eachFile in listdir(folder_images):
    if len(eachFile) > 0 and '.jpg' in eachFile:
        objectImg = {'link': folder_images + eachFile, 'name': eachFile[:len(eachFile)-4]}
        listImgs.append(objectImg)
        # print(eachFile)
numberImg = 0
for eachImg in listImgs:
    numberImg += 1
    print(numberImg)
    # if numberImg >=2:
    #      break
    imageInfor = cv2.imread(eachImg['link'])
    # cv2.imwrite('./test/review_aug_folder/root__' + str(numberImg) + '.jpg', imageInfor)
    for i in range(0,1):
        # aug = iaa.WithChannels((0,1,2), iaa.Add((-100, 100)))
        aug = iaa.AverageBlur(k=((5, 11), (1, 3)))
        contrimg = aug.augment_image(imageInfor)
        nameSave = randint(0,100000000)
        imgSaveLink = des_images + eachImg['name'] + '__' + str(i) +  '.jpg'
        cv2.imwrite(imgSaveLink, contrimg)
        copy(folder_txts + eachImg['name'] + '.txt', des_txts + eachImg['name'] + '__' + str(i) + '.txt')
        