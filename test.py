import os
print(os.getcwd())

#path = os.path.join(os.path.dirname(__file__),"Documents/majorProject/Face-Mask-Dectection/dataset/with_mask");

dirc = os.getcwd()

path = os.path.join(dirc,"dataset/without_mask");
print(path);

print(path)
count = 0
for img in os.listdir(path):
	img_path = os.path.join(path, img)
	count += 1
print(count)	

