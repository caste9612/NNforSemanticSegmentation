import os

def make_list(path, list_name):
	with open(list_name, 'w') as f:
		
		for (dirpath, dirnames, filenames) in os.walk(path):
			for filename in filenames:
				if filename.endswith(file_ending_lbl):

					lbl = os.path.join(dirpath, filename)
					img = lbl.replace(file_ending_lbl, "leftImg8bit.png" )
					img = img.replace("gtFine", "leftImg8bit")

					f.write( img + " " + lbl + "\n")

file_ending_lbl = 'gtFine_labelTrainIds.png'

#CREATE cityscapes_train_list.txt
path = "/home/antonioc/Scrivania/ML/dataset/cityscape/leftImg8bit_trainvaltest/gtFine/train/"
list_name= "cityscapes_train_list.txt"
make_list(path,list_name)
print("Created ", path+list_name)

#CREATE cityscapes_val_list.txt
path = "/home/antonioc/Scrivania/ML/dataset/cityscape/leftImg8bit_trainvaltest/gtFine/val/"
list_name= "cityscapes_val_list.txt"
make_list(path,list_name)
print("Created ", path+list_name)
