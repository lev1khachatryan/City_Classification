# City Classification

***Project consists of 2 parts:***

* [data preparation](https://github.com/lev1khachatryan/CityClassification/tree/master/data_preparation)

* [modeling](https://github.com/lev1khachatryan/CityClassification/tree/master/src)

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

This part also consists of 4 sections.

### 2.1 Base NN

This is the main section of modeling. [src/models/BaseNN.py](https://github.com/lev1khachatryan/CityClassification/blob/master/src/models/BaseNN.py) is an abstract class responsible for ***network creation***, ***initialization***, ***training***, ***testing*** and ***saving*** to specified directory. It also contains ***network*** abstract method implemented in derived (child) class, which gives us high level of abstraction and ability to create different types of networks with a little code change.

### 2.2 Specific Architectures

These are derived classes from BaseNN. I use 2 architectures: [src/models/CNN.py](https://github.com/lev1khachatryan/CityClassification/blob/master/src/models/CNN.py) and [src/models/DNN.py](https://github.com/lev1khachatryan/CityClassification/blob/master/src/models/DNN.py). These classes are responsible for implementing abstract methods of BaseNN class, so they ***construct the network***, ***defines the metric***, ***attach summaries*** and ***load tensors***.

### 2.3 Data loader

This [src/data_loader.py](https://github.com/lev1khachatryan/CityClassification/blob/master/src/data_loader.py) class gives all required methods for train/test/validation data loading and additional information for network constructing.

### 2.4 Starting points

[src/mainCNN.py](https://github.com/lev1khachatryan/CityClassification/blob/master/src/mainCNN.py) and [src/mainDNN.py](https://github.com/lev1khachatryan/CityClassification/blob/master/src/mainDNN.py) are starting points for DNN and CNN respectively. They define ***flags*** for network and do train/test depending on flag.


## Usage

Make sure you have installed [python 3](https://www.python.org/download/releases/3.0/) and all [required](https://github.com/lev1khachatryan/CityClassification/blob/master/requirements.txt) libraries.To install needed libraries just run `pip install -r requirements.txt`. If you will be using docker then run `docker build -t city_classification_image .` (image size is 2.46 GB).

### Preprocessing

To preprocess the data, put data folder to root directory (replace it with [existing](https://github.com/lev1khachatryan/CityClassification/tree/master/data) folder), go to [data_preparation](https://github.com/lev1khachatryan/CityClassification/tree/master/data_preparation) and specify correct parameters to [data_preparation/config/INI](https://github.com/lev1khachatryan/CityClassification/blob/master/data_preparation/config.INI) file.

Now you can run data preparation scripts. To train data preprocessing just run `python 1_train_preprocessor.py`. Test data preprocessing: `python 2_test_preprocessor.py`. Validation set extraction from train set: `python 3_validation_split.py` and for data augmentation `python 4_data_augmentation.py`. 




