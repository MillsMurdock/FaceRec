from resize import resize_image
from saveFeature import save_dat
import sys
import socket

def create_new_user(image_name):
	resize_image(image_name)
	save_dat(image_name)

if __name__ == '__main__':
	#image_name = sys.argv[1]
	image_name="4.jpg"
	create_new_user(image_name)


