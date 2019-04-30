import numpy as np 
import matplotlib.pyplot as plt
import os
import cv2 
import random
import pickle

# imageDirectory = "img_data/"
genres = ["blues", "classical", "country", "disco",
          "hiphop", "jazz", "metal", "pop", "reggae", "rock"] 
          

# for i in genres:
#         imagePath = i+"/"
#         imageDirectory = os.path.join("img_data/", imagePath)
#         fileName = os.listdir(imageDirectory)
#         for img in fileName:
#                 img_array = cv2.imread(os.path.join(imageDirectory, img))
#                 # plt.imshow(img_array)
#                 # plt.show()
#                 break
#         break

# print(img_array[200][150][0])


training_data=[]
def create_training_data():
    for g in genres:
        imagePath = g+"/"
        imageDirectory = os.path.join("img_data/", imagePath)
        fileName = os.listdir(imageDirectory)
        # Finding the index for each category to label our images
        classNum = genres.index(g)
        print ("Creating Training DataSet from Images for "+g.upper()+"...")
        for img in fileName:
                try:
                        imgArray = cv2.imread(os.path.join(imageDirectory, img))
                        # print(imgArray.shape[0])
                        training_data.append([imgArray, classNum])
                except Exception as e:
                        print("An error occurred while creating trainning data \n")
                # break
        print("Completed Dataset for genre: "+g.upper()+"\n")
        # break

create_training_data()
print("Length of Training Data is:")
print(len(training_data))
print(" ")
# print(training_data[::1])


# We shuffle the data to ensure correct learning instead of memorization
random.shuffle(training_data)

# for sample in training_data[:10]:
#         print("Shuffled Training labels: ",sample[1])

X = []
y = []
for features, label in training_data:
        X.append(features)
        y.append(label)

X = np.array(X).reshape(-1, 490, 1075, 3)

print("Saving X")
# np.save("X_data", X)
print("Finished Saving X \n")
print(X.shape)

# pickleOut = open("y.pickle", "wb")
print("Pickling Y")
# pickle.dump(y, pickleOut)
# pickleOut.close()
print("Finished pickling Y \n")

# pickleIn = open("X.pickle", "rb")
# print("Reading pickled X")
# X = pickle.load(pickleIn)

# print(X[1])
# print("Checking to see if our saved data works")
# loadedX = np.load('X_data.npy')
# print(loadedX)

