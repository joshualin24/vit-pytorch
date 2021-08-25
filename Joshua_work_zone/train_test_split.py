
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import search_around_sky, SkyCoord
from astropy import units as u
from sklearn.model_selection import train_test_split
from shutil import copyfile
import os, sys



root_folder = "/media/joshua/Milano/galaxy_zoo/images_training_rev1/"
train_folder = "/media/joshua/Milano/galaxy_zoo/train/"
test_folder = "/media/joshua/Milano/galaxy_zoo/test/"


# if not os.path.exists(root_folder + train_folder):
#     os.mkdir(root_folder + train_folder)
#
# if not os.path.exists(root_folder + test_folder):
#     os.mkdir(root_folder + test_folder)


train = pd.read_csv("/media/joshua/Milano/Milano_git_work_zone/Galaxy-Zoo-Classification/class_labels_train_46183_C5.csv")
test = pd.read_csv("/media/joshua/Milano/Milano_git_work_zone/Galaxy-Zoo-Classification/class_labels_test_15395_C5.csv")



for i in range(train.shape[0]):
    ID = train['GalaxyID'].iloc[i]
    img_path = root_folder + str(ID) + '.jpg'
    try:
        copyfile(img_path, train_folder  + str(ID) + '.jpg')
    except:
        print("miss:", ID)


for i in range(test.shape[0]):
    # ID = X_test.iloc[i]
    # M = y_test.iloc[i]
    ID = test['GalaxyID'].iloc[i]
    img_path = root_folder + str(ID) + '.jpg'
    try:
        copyfile(img_path, test_folder + str(ID) + '.jpg')
    except:
        print("miss:", ID)

print("job done.")
