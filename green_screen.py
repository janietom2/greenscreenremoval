import numpy as np 
from scipy import misc
import matplotlib.pyplot as plt
import sys
from enum import Enum




def main():
    
    foreground_path = "hang.jpg"
    background_path = "shiba.jpg"
    
    
    foreground_image = read_image(foreground_path)
    background_image = read_image(background_path)
    
    print(foreground_image.shape)
    print(background_image.shape)
    
    background_image = resize_image(foreground_image, background_image)
    
    print(foreground_image.shape)
    print(background_image.shape)
    
    is_green = find_green(foreground_image)
    
    final_image = merge_image(foreground_image, background_image, is_green)
    
    display_image(foreground_image, final_image)
    
    
def find_green_avg_std(img):
    
    green_values = list()
    
    for x in img:
        for y in x:
            green_values.append(y[1])
            
    avg = np.mean(green_values)
    std = np.std(green_values)
    
    return avg, std
    
    

def clean_noise(is_green):
    return
    

def resize_image(foreground_image, background_image):
    
    x_len = len(foreground_image)
    y_len = len(foreground_image[0])
    
    new = np.zeros(foreground_image.shape)
    
    if(x_len > len(background_image) or y_len > len(background_image[0])):
        print("Cannot use image smaller than original")
        sys.exit()
        
    if(x_len < len(background_image) and y_len < len(background_image[0])):
        
        new_x = 0
        new_y = 0
        
        center_x = int(len(background_image) / 2)
        center_y = int(len(background_image[0]) / 2)
        
        new_x = center_x - (int(len(foreground_image) / 2))
        new_y = center_y - (int(len(foreground_image[0]) / 2))
        copy = new_y
        
        for x in range(len(new)):
            new_x += 1
            new_y = copy
            for y in range(len(new[0])):
                new[x][y] = background_image[new_x][new_y]
                new_y += 1
                    
        return new
        
        
    
    for x in range(len(new)):
        for y in range(len(new[0])):
            new[x][y] = background_image[x][y]
        
    
    return new


def read_image(path):
    
    img = misc.face()
    img = misc.imread(path)
    #Returns image as a np array. 
    return img


def find_green(image):

    
    green_avg, green_std = find_green_avg_std(image)
    
    print(green_avg, " ", green_std)
    
    shape = image.shape
    shape = shape[0:2]
    is_green = np.zeros(shape)
        
    for x in range(len(image)): 
        for y in range(len(image[x])):
            if(image[x][y][0] < 75 and (image[x][y][1] > green_avg - green_std and image[x][y][1] < green_avg + green_std*2 )and image[x][y][2] < 75):
                is_green[x][y] = 1
    
    #returns boolean array with true in green areas
    return is_green

def merge_image(image, background, is_green):
    
    
    for x in range(len(image)):
        for y in range(len(image[x])):
            if is_green[x][y] == 1:
                image[x][y] = background[x][y]

    return image # returns final image as a np array
    
    
def display_image(initial_image, final_image):
    
    plt.imshow(initial_image)
    plt.show()
    plt.imshow(final_image)
    plt.show()
    #returns nothing lol
    return


if __name__ == "__main__":
    main()