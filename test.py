import os
print(os.getcwd())

#path = os.path.join(os.path.dirname(__file__),"Documents/majorProject/Face-Mask-Dectection/dataset/with_mask");

dirc = os.getcwd()

path = os.path.join(dirc,"dataset/with_mask");
print(path);

print(path)

for img in os.listdir(path):
	img_path = os.path.join(path, img)
	print(img_path)

