## Table of Contents

0. [About](#about)
0. [Installation](#installation)
0. [Quick start](#quick-start)
0. [References](#references)

## About

In this work, we implement the U-Net segmentation architecture on the Mnih et. al. Massachusetts Roads Dataset for the task of road network extraction. The trained network achieves a mask accuracy of 95% on the test set. The network was trained on AWS P2.x instance.
Inference time on a single K80 Tesla GPU(AWS P2.x instance) is 0.28 seconds and on CPU is 6 seconds.

<p align="center">
  <img width="460" height="300" src="assets/u-net.png">
</p>

## Installation

The following installation has been tested on MacOSX 10.13.6 and Ubuntu 16.04. (This project requires Python 3.6 and Conda which is an open source package management system and environment management system that runs on Windows, macOS and Linux. Before starting, make sure both are installed or follow the instructions below.)


Install Conda(A normal verification step would ask whether you would want to install Anaconda. Type yes so that the installation continues.)

```bash
chmod 777 conda.sh
./conda.sh
```

1. Clone the repo

```bash
git clone https://github.com/akshaybhatia10/RoadNetworkExtraction-MoveHack.git
cd RoadNetworkExtraction-MoveHack/
```

2. The project requires the fastai library. To install it, simply run the setup.sh script. (OPTIONAL: The default installation is for CPU. To install for GPU, in setup.sh file, change line 5 i.e conda env update -f environment-cpu.yml
to conda env update.)
conda install -c intel openmp 
git clone https://github.com/fastai/fastai.git
cd fastai
conda env update -f environment.yml
```
cd old
# to run the main.py it is essential to downgrade fastai to version 0.7
pip install .
cd ..
cd ..
conda install pytorch torchvision -c pytorch

Finally if using CPU version, run: 

```bash
source activate fastai-cpu
```

For GPU version, run:

```bash
source activate fastai
```

To train the network, proceed with step 3 and then [Quick start](#train). To test using the pretrained model, simply skip to [Quick start](#test).

3. Download the dataset from [here](http://academictorrents.com/details/3b17f08ed5027ea24db04f460b7894d913f86c21) or [here](https://www.cs.toronto.edu/~vmnih/data/). It is recommended to download the dataset using the torrent link since it downloads the files in the appropriate directories.


## Quick start

You have 2 options-

### Train

1. To train the U-NET architecture on the dataset, make sure to download the dataset and follow the repo structure as:


The repo structure should be as follows:
```angular2html
RoadNetworkExtraction-MoveHack
|_ mass_roads/
|  |_ train/
|  |  |_sat/
|  |  |  |img1.tiff
|  |  |  |img2.tiff
|  |  |  |......
|  |  |_map/
|  |  |  |img2.tif
|  |  |  |img2.tif
|  |  |  |......
|  |_ valid/
|  |  |_sat/
|  |  |  |img1.tiff
|  |  |  |img2.tiff
|  |  |  |......
|  |  |_map/
|  |  |  |img2.tif
|  |  |  |img2.tif
|  |  |  |......
|  |_ test/
|  |  |_sat/
|  |  |  |img1.tiff
|  |  |  |img2.tiff
|  |  |  |......
|  |  |_map/
|  |  |  |img2.tif
|  |  |  |img2.tif
|  |  |  |......
|_ fastai
|_ dataset.py
|_ model.py
|_ models/
|_ ....
|_ (other files)
```

Now, start training with the following command- (NOTE: This will first set up the necessary folders and convert .tiff files to png and save them. Then it will start trained the u-net architecture for num_epochs(default is 1) and with cycle_len(default is 4). The trained model will be saved to the models/ directory. and achieves a mask accuracy of 95% on test set.)

```bash
python main.py --mode train

usage: main.py  [--data_dir] [--learning_rate] [--mode]
                [--model_dir] [--num_epoch] [--build_dataset] [--cycle_len]
                [--test_img]

Arguments:
  --data_dir		 Path to the dataset(REQUIRED if mode is train, DEFAULT mass_roads/)
  --build_dataset	 If True, builds dataset from .tiff files i.e converts and resizes images to 1024 and stores in 'mass_roads_new/'(DEFAULT True)
  --mode 	    	 One of train or test(DEFAULT test)
  --learning_rate        learning rate(OPTIONAL, DEFAULT 0.1)
  --model_dir            Path to save model files(OPTIONAL, DEFAULT models)
  --test_img             Path to test image for inference(OPTIONAL, DEFAULT test_images/10378780_15.png)
  --num_epoch            number of epochs(OPTIONAL, DEFAULT 1)
  --cycle_len            cycle length(OPTIONAL, DEFAULT 4)
```

The trained model will be saved in the models directory with the name '1024-Mnih-own'.

### Test

2. To run inference using the trained model available in the models directory(with mask accuracy score of 95%), run the following- 

```bash
python main.py --mode test --test_img test_images/"Image_name".png
```

Change --test_img to path/to/image to run inference on other image.

To adjust the amount of epoch runned for the training edit the number for "--number of epoch" on line 42 in main.py


This will output 3 different images in the current working directory- a 1024x1024 version of original image, 1024x1024 generated mask image(output of the system), 1024x1024 mask overlayed on original image.


## References 

- Olaf Ronneberger, Philipp Fischer, Thomas Brox. U-Net: Convolutional Networks for Biomedical Image Segmentation. Medical Image Computing and Computer-Assisted Intervention (MICCAI), Springer. 2015.
- Volodymyr Mnih. Machine Learning for Aerial Image Labeling. University of Toronto. 2013.
- Jeremy Howard and others. fastai. GitHub. 2018.
