from os import listdir

nameFile = 'class_list.txt'
image_folder = './characters/'
listimg = []
for eachFile in listdir(image_folder):
    listimg.append(eachFile[:len(eachFile) - 4])

sorted_list = sorted(listimg)
print(sorted_list)
f = open(nameFile, 'a')
for eachFile in sorted_list:
    f.write(eachFile + '\n')
f.close()