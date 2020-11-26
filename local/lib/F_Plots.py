
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
from PIL import Image
import numpy as np
import pandas as pd

def display_random_image (images, label,show_box = False,image_path = 'local/data/imgs'):
    """
        Display a random image
    """
    
    images = images[images['label'] == label]
    index = np.random.randint(images.shape[0])
    img = Image.open(os.path.join(image_path,images.iloc[index][0]))

    if show_box == True:
        img_n = np.array(img)
        len_y , len_x , _ = img_n.shape

        xmin = images.iloc[index][1] * len_x
        xmax = images.iloc[index][2] * len_x
        ymin = images.iloc[index][3] * len_y
        ymax = images.iloc[index][4] * len_y

        plt.figure(figsize=(15,8))
        plt.imshow(img)
        plt.title('Image #{} : Formato : {} '.format(index,images.iloc[index][6]))
        plt.plot((xmin,xmax),(ymin,ymin),"r")
        plt.plot((xmin,xmax),(ymax,ymax),"r")
        plt.plot((xmin,xmin),(ymax,ymin),"r")
        plt.plot((xmax,xmax),(ymax,ymin),"r")
        plt.show()

        
    else:
        plt.figure(figsize=(15,8))
        plt.imshow(img)
        plt.grid(False)
        plt.title('Image #{} : Formato : {} '.format(index,images.iloc[index][6]))
        plt.show()


#function to show a batch of three images

def imshow_batch_of_three(batch, show_box=True):
    
    """
    Returns plot of 3 images with bbox.

    Args:
        batch (iter): iter with loaded images.

        show_box (bol)= True if you want to print the Bbox
                        False if you dont want to print the Bbox

    Returns:

        plot 3 images of the dataset
    """

    boxes_batch = batch[1].numpy()
    image_batch = batch[0].numpy()
    _ , axarr = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    _,len_y,len_x,_=image_batch.shape

    for i in range(3):
        img = image_batch[i, ...]
        axarr[i].imshow(img)
        if show_box:
#             axarr[i].set(xlabel='cordenates = {}'.format(boxes_batch[i]))
            axarr[i].plot((int(boxes_batch[i][0]*len_x),int(boxes_batch[i][1]*len_x)),(int(boxes_batch[i][2]*len_y),int(boxes_batch[i][2]*len_y)),"r")
            axarr[i].plot((int(boxes_batch[i][0]*len_x),int(boxes_batch[i][1]*len_x)),(int(boxes_batch[i][3]*len_y),int(boxes_batch[i][3]*len_y)),"r")
            axarr[i].plot((int(boxes_batch[i][0]*len_x),int(boxes_batch[i][0]*len_x)),(int(boxes_batch[i][2]*len_y),int(boxes_batch[i][3]*len_y)),"r")
            axarr[i].plot((int(boxes_batch[i][1]*len_x),int(boxes_batch[i][1]*len_x)),(int(boxes_batch[i][2]*len_y),int(boxes_batch[i][3]*len_y)),"r")