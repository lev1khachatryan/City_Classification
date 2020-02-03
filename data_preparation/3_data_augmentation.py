import os, os.path
import random
from scipy import ndarray
import numpy as np

# image processing library
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io

import csv
import os
import imageio
import numpy as np
import pandas as pd
import configparser
from utils import *
from PIL import Image

def random_rotation(image_array: ndarray):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image_array, random_degree)

def random_noise(image_array: ndarray):
    # add random noise to the image
    return sk.util.random_noise(image_array)

def horizontal_flip(image_array: ndarray):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[:, ::-1]


def main(DATA_DIR, PERCENT_TO_AUGMENT):
	# dictionary of the transformations we defined earlier
	available_transformations = {
	    'rotate': random_rotation,
	    'noise': random_noise,
	    'horizontal_flip': horizontal_flip
	}

	print('------------------Train set augmentation started')
	subFolderList = []
	for x in os.listdir(DATA_DIR):
	    if os.path.isdir(DATA_DIR + '/' + x):
	        subFolderList.append(x)

	dict = {}
	for x in subFolderList:
	    all_files = [y for y in os.listdir(DATA_DIR + x)]
	    dict[DATA_DIR + x] = len(all_files)

	for k, v in dict.items():
	    folder_path = k
	    num_files_desired = int(np.round( v * PERCENT_TO_AUGMENT))
	    
	    # find all files paths from the folder
	    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
	    
	    num_generated_files = 0
	    while num_generated_files <= num_files_desired:
	        # random image from the folder
	        image_pat = random.choice(images)
	        # read image as an two dimensional array of pixels
	        image_to_transform = sk.io.imread(image_pat)
	        # random num of transformation to apply
	        num_transformations_to_apply = random.randint(1, len(available_transformations))

	        num_transformations = 0
	        transformed_image = None
	        while num_transformations <= num_transformations_to_apply:
	            # random transformation to apply for a single image
	            key = random.choice(list(available_transformations))
	            transformed_image = available_transformations[key](image_to_transform)
	            num_transformations += 1

	        new_file_path = '%s/augmented_image_%s.png' % (folder_path, num_generated_files)

	        # write image to the disk
	        io.imsave(new_file_path, transformed_image)
	        num_generated_files += 1

	print('------------------Train set augmentation finished')

if __name__ == "__main__":
	config = configparser.ConfigParser()
	config.read('config.INI')

	DATA_DIR = config['paths']['DATA_DIR']
	PERCENT_TO_AUGMENT = float(config['other']['PERCENT_TO_AUGMENT'])

    main(DATA_DIR, PERCENT_TO_AUGMENT)