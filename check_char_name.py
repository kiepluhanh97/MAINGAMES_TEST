from os import listdir

image_folder = './characters/'
file_path = './test_data/hero_names.txt'

listImg = []
for eachFile in listdir(image_folder):
    listImg.append(eachFile)
print(listImg)
f = open(file_path, 'r')
lines = f.read()
lines = lines.split('\n')
f.close()

for char_name in lines:
    if char_name + '.jpg' not in listImg:
        print(char_name)
