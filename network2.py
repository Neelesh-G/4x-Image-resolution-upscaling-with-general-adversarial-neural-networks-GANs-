

#!/usr/bin/env python
#title           :Network.py
#description     :Architecture file(Generator and Discriminator)
#author          :Deepak Birla
#date            :2018/10/30
#usage           :from Network import Generator, Discriminator
#python_version  :3.5.4 

# Modules
from keras.layers import Dense
from keras.layers.core import Activation
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import UpSampling2D
from keras.layers.core import Flatten
from keras.layers import Input
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.models import Model
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.layers import add
from keras.models import load_model
from keras.applications.vgg19 import VGG19


#from network2 import Generator, Discriminator
from keras.models import load_model
from keras.models import model_from_json
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from keras.applications.vgg19 import VGG19
from keras.layers.convolutional import UpSampling2D
from keras.models import Model
from keras.optimizers import SGD, Adam, RMSprop
import keras
import keras.backend as K
from keras.layers import Lambda, Input
import tensorflow as tf
import skimage.transform
from skimage import data, io, filters
import numpy as np
from numpy import array
from skimage.transform import rescale, resize
from scipy.misc import imresize
import os


image_shape = (256,256,3)

def vgg_loss(y_true, y_pred):
    
    vgg19 = VGG19(include_top=False, weights='imagenet', input_shape=image_shape)
    vgg19.trainable = False
    for l in vgg19.layers:
        l.trainable = False
    loss_model = Model(inputs=vgg19.input, outputs=vgg19.get_layer('block5_conv4').output)
    loss_model.trainable = False
    return K.mean(K.square(loss_model(y_true) - loss_model(y_pred)))    

    
   




# Network Architecture is same as given in Paper https://arxiv.org/pdf/1609.04802.pdf
class Generator(object):

    def __init__(self, noise_shape):
        
        self.noise_shape = noise_shape

    def generator(self):
       generator_model = load_model('./output/gen_model120.h5', custom_objects={'vgg_loss':vgg_loss})   
	#generator_model = Model(inputs = gen_input, outputs = model)
       return generator_model

# Network Architecture is same as given in Paper https://arxiv.org/pdf/1609.04802.pdf
class Discriminator(object):

    def __init__(self, image_shape):
        
        self.image_shape = image_shape
    
    def discriminator(self):
        
        discriminator_model = load_model('./output/dis_model120.h5', custom_objects={'vgg_loss':vgg_loss}) 
        
        return discriminator_model
