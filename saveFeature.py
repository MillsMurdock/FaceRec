import os
import pickle
import face_recognition
from PIL import Image
import time
import sys

dat_path = "ResizeFace"

#读取face_feature.dat里的特征，返回一个字典，给face_test.py用
def read_dat():
	data_path = dat_path + '/' + 'face_feature.dat'
	if (os.path.exists(data_path) == False) or (os.path.getsize(data_path) == 0):
		return dict()
	file = open(data_path,'rb')
	dic_data = pickle.load(file)
	file.close()
	return dic_data

#对新加进DataBase的图片先进行resize之后调用该函数进行特征提取并保存在face_feature.dat中	
def save_dat(image_name):
	dic = read_dat()
	id = image_name.split('.')[0]
	#print(id)
	if id not in dic.keys():
		image_path = dat_path + '/' + image_name
		if (os.path.exists(image_path) == False):
			raise Exception('can not find the pic')
			#print('can not find the pic')
			return -1
		image = face_recognition.load_image_file(image_path)
		face_encoding = face_recognition.face_encodings(image)[0]
		dic[id] = face_encoding
		data_path = dat_path + '/' + 'face_feature.dat'
		if (os.path.exists(data_path) == False):
			#print('can not find the dat')
			raise Exception('can not find the dat')
			return -1
		file = open(data_path,'wb')
		pickle.dump(dic,file)
		file.close()
	return 1

#清除face_feature.dat中的所有特征
def clean_dat():
	data_path = dat_path + '/' + 'face_feature.dat'
	dic = dict()
	file = open(data_path,'wb')
	pickle.dump(dic,file)
	file.close()
	return 1

#对所有ResizeFace中的人脸进行特征提取，调试用
def save_all():
	userName = os.listdir(dat_path)
	for user in userName:
		if user.split('.')[1] == 'jpg':
			save_dat(user)


if __name__ == '__main__':
	image_name = sys.argv[1]
	start = time.time()
	if image_name == 'clean':
		clean_dat()
	elif image_name == 'saveall':
		save_all()
	else:
		save_dat(image_name)
	end = time.time()
	print(end - start)




