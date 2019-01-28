from PIL import Image
import time
import sys
import os

face_data_path = "DataBase"
resize_data_path = "ResizeFace"
unknown_image_path = "cache/unknown.jpg"
target = 150

#对某一张新加进DataBase的图片进行resize，用于注册
def resize_image(image_name):
	path = face_data_path + '/' + image_name
	image = Image.open(path)
	if image.size[0] > target:
		t = image.size[0] / target
		image = image.resize((target,int(image.size[1] / t)),Image.ANTIALIAS)
	path = resize_data_path + '/' + image_name
	image.save(path)

#对DataBase全部进行resize，调试用
def resize_all():
	userName = os.listdir(face_data_path)
	for user in userName:
		resize_image(user)

#对平板上传的unknown.jpg进行resize，减少像素使得识别加快
def resize_unknown_image():
	unknown_image = Image.open(unknown_image_path)
	if unknown_image.size[0] > target:
		t = unknown_image.size[0] / target
		unknown_image = unknown_image.resize((target,int(unknown_image.size[1] / t)),Image.ANTIALIAS)
	unknown_image.save(unknown_image_path)

if __name__ == '__main__':
	image_name = sys.argv[1]
	start = time.time()
	if image_name == 'resize_all':
		resize_all()
	elif image_name == 'resize_unknown':
		resize_unknown_image()
	else:
		resize_image(image_name)
	end = time.time()
	print(end - start)