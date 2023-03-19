from os import path,listdir
import os
from shutil import copy
from random import randint
root_folder = './dataset/'
des_folder = './dataset_mix/'

if not path.exists(des_folder):
    os.mkdir(des_folder)

for eachFile in listdir(root_folder):
    if '.jpg' in eachFile:
        txtRoot = eachFile[:len(eachFile) -4] + '.txt'
        nameSave = randint(0,1000000000)
        while path.exists(des_folder + str(nameSave) + '.jpg'):
                print('lollllllllllllllllll')
                nameSave = randint(0,1000000000)

        imgSave = des_folder + str(nameSave) + '.jpg'
        txtSave = des_folder + str(nameSave) + '.txt'
        copy(root_folder + eachFile, imgSave)
        copy(root_folder + txtRoot, txtSave)
