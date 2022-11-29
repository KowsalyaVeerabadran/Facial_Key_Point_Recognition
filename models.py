## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(1, 32, 5)
        
        self.conv1_bn=nn.BatchNorm2d(32)
        
        # Max-pooling layer
        self.pool = nn.MaxPool2d(2,2) 
        
        # second convolutional layer
        self.conv2 = nn.Conv2d(32, 64, 3)
        
        self.conv3 = nn.Conv2d(64, 128, 3)
                
        # Linear layer
        self.fc1 = nn.Linear(128*26*26, 136)
        
        self.drop1 = nn.Dropout2d(p=0.2, inplace=False)
        
        self.drop2 = nn.Dropout(p=0.2, inplace=False)

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        
        # two conv/relu + pool layers 
        x = self.conv1(x)
        x = self.pool(F.relu(self.conv1_bn(x)))
        x = self.drop1(x)
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
               
        x = x.view(x.size(0), -1)        
       
        x = self.drop2(x)
        
        x = self.fc1(x)     
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
