
import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np

def display_random_image (images, label,image_path = 'local/data/imgs'):
    """
        Display a random image
    """
    
    images = images[images['label'] == label]
    index = np.random.randint(images.shape[0])
    plt.figure(figsize=(15,8))
    img = Image.open(os.path.join(image_path,images.iloc[index][0]))
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.title('Image #{} : Formato : {} '.format(index,images.iloc[index][6]))
    plt.show()