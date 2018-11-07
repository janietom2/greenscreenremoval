import numpy as np 
from scipy import misc
import matplotlib.pyplot as plt


def main():
    
    foreground_path = "testpath.png"
    background_path = "testpath.png"
    
    
    foreground_image = read_image(foreground_path)
    background_image = read_image(background_path)
    
    is_green = find_green(foreground_image)
    
    final_image = merge_image(foreground_image, background_image, is_green)
    
    display_image(foreground_image, final_image)
    



def read_image(path):
    
    
    
    #Returns image as a np array. 
    return


def find_green(image):
    
    
    
    #returns boolean array with true in green areas
    return

def merge_image(image, background, green_area):
    
    
    
    #returns final image as a np array
    return
    
def display_image(initial_image, final_image):
    
    
    #returns nothing lol
    return


if __name__ == "__main__":
    main()