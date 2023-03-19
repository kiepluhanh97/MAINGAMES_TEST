import os
from os import listdir, path
from shutil import copyfile, move, copy
from random import seed
from random import randint
seed(1)

sets_folder = './sets/'

des_folder = './dataset/'

listSet = []
if not os.path.exists(des_folder):
    os.mkdir(des_folder)

for eachFile in listdir(des_folder):
    if len(eachFile) > 0:
        os.remove(des_folder + eachFile)

for eachFile in listdir(sets_folder):
    if len(eachFile) > 0:
        listSet.append(sets_folder + eachFile + '/')

numfile = 0
for eachSet in listSet:
    print(eachSet)
    for eachFile in listdir(eachSet):
        if len(eachFile) > 0 and '.jpg' in eachFile:
            numfile += 1
            print(numfile)
            imgRoot = eachSet + eachFile
            txtRoot = eachSet + eachFile[:len(eachFile) -4] + '.txt'
            nameSave = randint(0,1000000000)
            while path.exists(des_folder + str(nameSave) + '.jpg'):
                print('lollllllllllllllllll')
                nameSave = randint(0,1000000000)
            imgSave = des_folder + str(nameSave) + '.jpg'
            txtSave = des_folder + str(nameSave) + '.txt'
            copy(imgRoot, imgSave)
            copy(txtRoot, txtSave)
    