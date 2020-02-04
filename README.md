# City Classification

***Project consists of 2 parts:***

* data preparation

* modeling

## 1. data preparation

This part consists of 4 sections.

### 1.1 train data preprocessing

This is the [data_preparation/1_train_preprocessor.py](https://github.com/lev1khachatryan/CityClassification/blob/master/data_preparation/1_train_preprocessor.py) script which includes bad image discarding, save their names to [data/corrupted_images.txt](https://github.com/lev1khachatryan/CityClassification/blob/master/data/corrupted_images.txt) (as you can see there are 2 bad images).

*Note*: If we just change the extension of image, let's say from "jpg" to "Be" or to "$" (which are random characters), we do not corrupt it, so we can read it with PIL or scipy.misc.imread etc. and use them in our training process. That is why I do not delete them from data set.

train preprocessing also includes moving of all training images to "yerevan" and "london" directories.

### 1.2 test data preprocessing

This is the [data_preparation/2_test_preprocessor.py](https://github.com/lev1khachatryan/CityClassification/blob/master/data_preparation/2_test_preprocessor.py) script, which discards bad images from test dataset. As you can see, here we have 1 corrupted image as well as in train dataset [data/corrupted_images.txt](https://github.com/lev1khachatryan/CityClassification/blob/master/data/corrupted_images.txt).

### 1.3 Validation set extraction from train set

In [data_preparation/config.INI](https://github.com/lev1khachatryan/CityClassification/blob/master/data_preparation/config.INI) file you can specify validation set size, and [data_preparation/3_validation_split.py](https://github.com/lev1khachatryan/CityClassification/blob/master/data_preparation/3_validation_split.py) script will randomly choose images from train set and move them to validation folder. In order to avoid "inbalanced data" problem, script chooses images uniformly from both classes.

### 1.4 Data augmentation

This is the [data_preparation/4_data_augmentation.py](https://github.com/lev1khachatryan/CityClassification/blob/master/data_preparation/4_data_augmentation.py) script, which get all necessary parameters from [data_preparation/config.INI](https://github.com/lev1khachatryan/CityClassification/blob/master/data_preparation/config.INI) file, load images from directories (train and validation) and applies one of three transformations (rotation, noise adding and horizontal flipping). In config file you can specify ratio of augmented data.


## 2. modeling

