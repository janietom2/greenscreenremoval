import numpy as np 
from scipy import misc
import matplotlib.pyplot as plt
from enum import Enum




def main():
    
    foreground_path = "test.png"
    background_path = "test2.jpeg"
    
    
    foreground_image = read_image(foreground_path)
    background_image = read_image(background_path)
    
    print(foreground_image.shape)
    print(background_image.shape)
    
    is_green = find_green(foreground_image)
    
    #final_image = merge_image(foreground_image, background_image, is_green)
    
    display_image(foreground_image, background_image)
    



def read_image(path):
    
    img = misc.face()
    #misc.imsave(path, img)
    img = misc.imread(path)
    
    
    #Returns image as a np array. 
    return img


def find_green(image):

    
    shape = image.shape
    shape = shape[0:2]
    is_green = np.zeros(shape)
    
    x_coord = 0
    y_coord = 0
    
    
    for x in range(len(image)):
        x_coord += 1
        
        for y in range(len(image[x])):
            y_coord += 1
            
            if(image[x][y][0] < 5 and image[x][y][1] > 245 and image[x][y][2] < 5):
                is_green[x][y] = 1
    
    #returns boolean array with true in green areas
    return is_green

def merge_image(image, background, green_area):
    
    
    
    
    
    #returns final image as a np array
    return
    
def display_image(initial_image, final_image):
    
    plt.imshow(initial_image)
    plt.show()
    plt.imshow(final_image)
    plt.show()
    #returns nothing lol
    return


if __name__ == "__main__":
    main()