# MAINGAMES_TEST
I've try some machine learning algorithm like SVM or function in opencv to detect hero image appear in background but it not work well. So I try it with deep learning model: YOLO
I'll create train data without any image in test set. Step by step above
1. craw character image from website - Done
run
python3 get_char_data.py
to get all hero avartar in characters folder

I must to check list name in txt input file and list character get from the website because it isn't enought. So I create new txt file make sure enough for all hero.
run
python3 check_char_name.py
to check name in txt input file with jpg name file. if have any mistake, I must update jpg file name to fit with name in txt input file

run
python3 create_txt_file.py
to create new txt file for labels

2. create data set with ramdom background - Done
run
python3 create_root_set.py
to create root dataset in dataset folder

3. augmentation data set
run
python3 aument-data.py
to augment data set with ramdom scale images

run
python3 augment-data_3.py
to augment data set with more blur images

augment-data_3.py to augment data with change some color backgroud. But after training, I get worse result, so we'll not use it

you can use merge_dataset_v3.py and mix-dataset.py to create new set from one or many set ramdom order.

4. prepare for training
when have dataset folder, run python3 gen.py to create train.txt file and test.txt file. that have 90% for traning and 10% for validating in traning process

5. test on test set
run 
python3 test.py --model-path './train_src/backup-tiny/custom-obj-tiny_last.weights' --cfg-path './train_src/custom-obj-tiny.cfg' --images-path './test_data/test_images/' --labels-path './test_data/test.txt'
