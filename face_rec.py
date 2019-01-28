import os
import face_recognition
import time
import shutil
from PIL import Image
from resize import resize_image
from saveFeature import read_dat
import cv2
unknown_image_path = "cache/unknown.jpg"
face_data_path = "DataBase"
resize_data_path = "ResizeFace"

def exist(unknown_image_path):
	if not os.path.exists(unknown_image_path):
		raise  Exception("no unknown image")
		return False
	else:
		return True

#对待识别图片和图片库图片提取特征，进行比对，时间随着图片库的增加而线性增加
def recognition_pic():
	unknown_image = face_recognition.load_image_file(unknown_image_path)
	userName = os.listdir(face_data_path)
	b = False
	for user in userName:
		user_image_path = face_data_path + '/' + user
		user_image = face_recognition.load_image_file(user_image_path)
		user_encoding = face_recognition.face_encodings(user_image)[0]
		unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
		result = face_recognition.compare_faces([user_encoding],unknown_encoding,0.6)
		if result[0] == True:
			b = True
			username = user.split('.')
			return (username[0])
	if not b:
		return ('no that person')

#用预先计算好的特征进行对比识别，加快识别速度
def recognition_fea():
	unknown_image = face_recognition.load_image_file(unknown_image_path)
	#cv2.imshow("src",unknown_image)
	#cv2.waitKey(0)
	face_location = face_recognition.face_locations(unknown_image)
	#unknown_image = unknown_image[face_location[0][0]:face_location[0][2],face_location[0][3]:face_location[0][1]]
	i = 0               #找最大脸
	j = 0
	size = 0
	for face in face_location:
		#print(face[2] - face[0])
		if (face[2] - face[0] > size):
			size = face[2] - face[0]
			i = j
		j += 1
	if j == 0:
		return
	#print(i)
	#unknown_image = unknown_image[face_location[i][0]:face_location[i][2],face_location[i][3]:face_location[i][1],:]
	#cv2.imshow("cut",unknown_image)
	#cv2.waitKey(0)
	userName = os.listdir(resize_data_path)
	b = False
	dic = read_dat()
	start = time.time()
	unknown_encoding = face_recognition.face_encodings(unknown_image)[i]
	end = time.time()
	print(end - start)
	start = time.time()
	for user in userName:
		if user.split('.')[1] == 'jpg':
			id = user.split('.')[0]
			result = face_recognition.compare_faces([dic[id]],unknown_encoding,0.5)
			if result[0] == True:
				b = True
				print(id)
				break
	if not b:
		print('no that person')
	end = time.time()
	print(end - start)

if __name__ == '__main__':
	start = time.time()
	recognition_fea()
	end = time.time()
	print(end - start)
