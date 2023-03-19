import random
import imgaug as ia
import numpy as np
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from imgaug.augmentables.kps import KeypointsOnImage, Keypoint
from imgaug import augmenters as iaa
ia.imgaug.seed(15)
random.seed(5)
from os import listdir
import cv2
def preprocess_scale(im, boxes):
    imgboxes = BoundingBoxesOnImage.from_xyxy_array(boxes, im.shape)
    seq = iaa.Affine(scale={"x": (0.6, 1), "y": (0.6, 1)})
    #apply
    image_aug, boxes_aug = seq(image=im, bounding_boxes=imgboxes)
    image_aug = ia.imresize_single_image(image_aug, im.shape[0:2])
    boxes_aug = boxes_aug.on(image_aug)
    boxes = boxes_aug.to_xyxy_array(dtype=np.int)
    return image_aug, boxes

folder_images = './dataset/'
folder_txts = './dataset/'

des_images = './dataset/'
des_txts = './dataset/'

number = 0
for eachImage in listdir(folder_images):
    # print('lol')
    if '.jpg' in eachImage:
        fileName = eachImage[:len(eachImage)-4]
        number+=1
        print(number)
        img = cv2.imread(folder_images + eachImage)
        (H,W) = img.shape[:2]
        txtFile = folder_txts + eachImage[:len(eachImage)-3] + 'txt'
        listBox = []
        listId = []
        with open(txtFile,'r') as f:
            rows = f.readlines()
            for i,v in enumerate(rows):
                v = v[:len(v)-1]
                v = v.split(' ')
                cx,cy,w,h = float(v[1])*W, float(v[2])*H, float(v[3])*W, float(v[4])*H
                x1,y1,x2,y2 = int(cx-w/2), int(cy-h/2), int(cx+w/2), int(cy+h/2)
                listBox.append((x1,y1,x2,y2))
                listId.append(v[0])
        boxes = np.array(listBox)

        for ii in range(0,2):
            new_img, new_box = preprocess_scale(img, boxes)
            stringOutput = ''
            for idp,each_box in enumerate(new_box):
                stringOutput += listId[idp] + ' '
                cx = each_box[0] + (each_box[2]- each_box[0]) / 2
                cy = each_box[1] + (each_box[3] - each_box[1]) / 2
                w = each_box[2]- each_box[0]
                h = each_box[3] - each_box[1]
                stringOutput += str(cx/W) + ' ' + str(cy/H) + ' ' + str(w/W) + ' ' + str(h/H) + '\n'
            
            cv2.imwrite(des_images + str(fileName) + '__' + str(ii) + '.jpg', new_img)
            f2 = open(des_txts + str(fileName) + '__' + str(ii) + '.txt',"w+")
            f2.write(stringOutput)
            f2.close()