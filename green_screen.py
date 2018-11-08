import numpy as np 
from scipy import misc
import matplotlib.pyplot as plt


def main():
    
    foreground_path = "test.png"
    background_path = "test2.jpeg"
    
    
    foreground_image = read_image(foreground_path)
    background_image = read_image(background_path)
    
    print(foreground_image.shape)
    print(background_image.shape)
    
    #is_green = find_green(foreground_image)
    
    #final_image = merge_image(foreground_image, background_image, is_green)
    
    display_image(foreground_image, background_image)
    



def read_image(path):
    
    img = misc.face()
    #misc.imsave(path, img)
    img = misc.imread(path)
    
    
    #Returns image as a np array. 
    return img


def find_green(image):
    
    
    
    #returns boolean array with true in green areas
    return

def merge_image(image, background, green_area):
    
    
    
    #returns final image as a np array
    return
    
def display_image(initial_image, fin    al_image):
    
    plt.imshow(initial_image)
    plt.show()
    plt.imshow(final_image)
    plt.show()
    #returns nothing lol
    return

def resize_image():
    filename = "image.jpg"
    new_image [][][] = resize_image()



if __name__ == "__main__":
    main()

# yeah python