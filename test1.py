import cv2
from os import listdir
from test_utils.detect_utils import infer_image
from randimage import get_random_image
import matplotlib
# cfg_path = './train_src/custom-obj.cfg'
# weight_path = './train_src/backup/custom-obj_last.weights'

cfg_path = './train_src/custom-obj-tiny.cfg'
weight_path = './train_src/backup-tiny/custom-obj-tiny_last.weights'
yolo_size= (416,416)
netDetect = cv2.dnn.readNetFromDarknet(cfg_path, weight_path)
layer_names = netDetect.getLayerNames()
layer_names = [layer_names[i[0] - 1] for i in netDetect.getUnconnectedOutLayers()]

label_file = './class_list.txt'
f = open(label_file, 'r')
labels = f.read().split('\n')
f.close()

groud_truth_file = './test_data/test.txt'
f = open(groud_truth_file, 'r')
listInputData = f.read().split('\n')
dictName = {}
for data in listInputData:
    data = data.split('\t')
    if len(data) > 1:
        print(data)
        dictName[data[0]] = data[1]
f.close()
numTrue = 0
numImg = 0
folder_test = './test_data/test_images/'
for eacfile in listdir(folder_test):
    numImg += 1
    imgRoot = cv2.imread(folder_test + eacfile)
    h = imgRoot.shape[0]
    img = imgRoot[:, :int(h*1.5)]
    img = cv2.resize(img, (40,30))
    img = cv2.resize(img, yolo_size)
    frame_3, boxes1, confidences, classids, idxs = infer_image(
            netDetect, layer_names, yolo_size[0], yolo_size[1], img, thresh=0.1)
    # print(boxes1, confidences, classids, idxs)
    if len(idxs) > 0:
        boxes2 = []
        bestClass = -1
        maxConf = 0
        heroName = ''
        for i in idxs.flatten():
            if confidences[i] > maxConf:
                maxConf = confidences[i]
                bestClass = classids[i]
        if bestClass >= 0:
            heroName = labels[bestClass]
        if heroName == dictName[eacfile]:
            numTrue += 1
        else:
            print(dictName[eacfile], '=========', heroName)
    else:
        print(dictName[eacfile], '=========', '')
    cv2.imwrite('./real_test/' + str(numImg) + '.jpg', img)
    # cv2.imshow('check', img)
    # cv2.waitKey()
print(numTrue/numImg*100)
