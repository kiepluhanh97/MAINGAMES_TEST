import cv2
from test_utils.detect_utils import infer_image
import argparse
import json
# import chart

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-path', help='link to ai model', type=str, default="", required=True)
    parser.add_argument('--cfg-path', help='link to cfg file', type=str, default="", required=True)
    parser.add_argument('--images-path', help='link to images folder', type=str, default="", required=True)
    parser.add_argument('--labels-path', help='link to groud truth file', type=str, default="", required=True)

    args = None
    try:
        args = parser.parse_args()
    except:
        print("==== Parse argument exception")
    print(args)

    MODEL_PATH = args.model_path
    CONFIG_PATH  = args.cfg_path
    IMAGES_FOLDER = args.images_path
    GROUND_TRUTH_PATH = args.labels_path

    # cfg_path = './train_src/custom-obj.cfg'
    # weight_path = './train_src/backup/custom-obj_best.weights'
    # cfg_path = './train_src/custom-obj-tiny.cfg'
    # weight_path = './train_src/backup-tiny/custom-obj-tiny_last.weights'

    # loading model
    yolo_size= (416,416)
    netDetect = cv2.dnn.readNetFromDarknet(CONFIG_PATH, MODEL_PATH)
    layer_names = netDetect.getLayerNames()
    layer_names = [layer_names[i[0] - 1] for i in netDetect.getUnconnectedOutLayers()]

    # loading labels of all obj can be detected in model
    label_file = './class_list.txt'
    f = open(label_file, 'r')
    labels = f.read().split('\n')
    f.close()

    # loading ground truth
    groud_truth_file = GROUND_TRUTH_PATH
    f = open(groud_truth_file, 'r')
    listInputData = f.read().split('\n')
    dictName = {}
    for data in listInputData:
        data = data.split('\t')
        if len(data) > 1:
            # print(data)
            dictName[data[0]] = data[1]
    f.close()
    dictStat = {}

    numTrue = 0
    numImg = 0
    folder_test = IMAGES_FOLDER
    outputFile = 'output.txt'
    rs_file = open(outputFile,'w')

    for key,value in dictName.items():
        if value not in dictStat:
            dictStat[value] = {'num_true': 0, 'num_false': 0}
        numImg += 1
        imgRoot = cv2.imread(folder_test + key)
        h = imgRoot.shape[0]
        img = imgRoot[:, :int(h*1.5)]
        img = cv2.resize(img, (40,30)) # got image same size with traning data then scale to yolo size
        img = cv2.resize(img, yolo_size)
        frame_3, boxes1, confidences, classids, idxs = infer_image(
                netDetect, layer_names, yolo_size[0], yolo_size[1], img, thresh=0.01)
        # print(boxes1, confidences, classids, idxs)
        heroName = ''
        if len(idxs) > 0:
            boxes2 = []
            bestClass = -1
            maxConf = 0
            
            for i in idxs.flatten():
                if confidences[i] > maxConf:
                    maxConf = confidences[i]
                    bestClass = classids[i]
            if bestClass >= 0:
                heroName = labels[bestClass]
            if heroName == value:
                numTrue += 1
                dictStat[value]['num_true'] += 1
            else:
                print(value, '=========', heroName)
                dictStat[value]['num_false'] += 1
        else:
            print(value, '=========', heroName)
            dictStat[value]['num_false'] += 1
        rs_file.write(key + '\t' + heroName + '\n')
        # cv2.imwrite('./real_test/' + str(numImg) + '.jpg', img)
        # cv2.imshow('check', img)
        # cv2.waitKey()
    print(f'ACCURACY : {numTrue/numImg*100}')
    rs_file.close()
    s = json.dumps(dictStat)
    open("result.json","w").write(s)