# Super-resolution
4x super resolution srgans

The model takes in a 96by96 image and upscales it to a 384by384 image.

*Upload you image directory as specified in train.py.

*create an output directory to save your models and outputs.

In order to start the training process run the train.py file.

The models directory contains a pretrained generator.Download the pretrained discriminator [HERE](https://drive.google.com/file/d/11PBOs1ginvWt_lBLnpLVF7Uglma2kYrV/view?usp=sharing) and place it in the models file.Run test.py

In order to resume the training from an already trained model,include your model in the intermediate_network.py file.Then import the generator and discriminator from intermediate_network.py into train.py and run train.py.

The below image is the sample output for the 80th epoch.

![gan_generated_image_epoch_80](https://user-images.githubusercontent.com/72451756/95555155-fe878600-0a2e-11eb-8565-9d58ccdcc5af.png)

For a 16x upscaling of resolution(if sufficient amount of ram is available) import the generator and discriminator from network2.py into train.py(Google cloud preffered)







