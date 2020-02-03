# City Classification

***repo consists of 6 parts:***

* data preparation

* main.py

* utils.py

* data loader.py

* BaseNN.py

* DNN.py

## 1. data preparation

This part consists of 3 parts

### 1.1 train data preprocessing

At first I discard all "bad" images. An Interesting finding here: If we just change the extension of image let's say from "jpg" to "Be" or to "$" (which are random characters), we do not corrupt it, so we can read it with PIL or scipy.misc.imread etc. and use them in our training process. That is why I do not delete them from train images.

After "bad" image discarding step, we move all training images to "yerevan" and "london" directories.

### 1.2 test data preprocessing

Here we have a corrupted image "242_yerevan.jpg", and I delete it from the folder and save the full path to data/corrupted_images.txt file.

### 1.3 data augmentation

Load images from directory and applies one of three transformations (rotation, noise adding and horizontal flipping).
All necessary parameters was taken from config.INI file.



