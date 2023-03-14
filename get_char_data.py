# get data from website and save in characters folder with format <character's name>.jpg
from urllib.request import urlopen
import re
import cv2
import numpy as np
import urllib
import requests
import os
def saveWithCV2(url, path):
    try:
        req = urllib.request.urlopen(url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1) # 'Load it as it is'
        cv2.imwrite(path, img)
    except Exception as e:
        print(f'Can not save {url} with opencv, try gif format')
        # path2 = path.replace('.jpg', '.gif')
        # res = requests.get(url)
        # print(res.status_code)
        # with open(path2, 'wb') as out:
        #     out.write(res.content)

url = 'https://leagueoflegends.fandom.com/wiki/League_of_Legends:_Wild_Rift'
pageDetail = urlopen(url)
htmlDetails = pageDetail.read().decode("utf-8")
# write file for test
# f4 = open('check.html', "a")
# f4.write(htmlDetails)
# f4.close()
imageFolder = './characters/'
if not os.path.exists(imageFolder):
    os.mkdir(imageFolder)

listImgText = re.findall(r'(data-width="20"><a href="/wiki((?!<a).)*</a>)', htmlDetails, re.DOTALL)
print(len(listImgText))
for eachImg in listImgText:
    eachImg = eachImg[0]
    nameInfor = eachImg.split('title="')[1].split('"')[0]
    nameInfor = nameInfor.replace('&#39;', '_')
    url = eachImg.split('data-src="')[1].split('"')[0]
    saveWithCV2(url, imageFolder + nameInfor + '.jpg')
    print(nameInfor, url)

