import numpy as np 
from scipy import misc
import matplotlib.pyplot as plt
import sys
from tkinter import *
from tkinter import messagebox
import urllib.request
from jsonread import *
from random import *

def main():

    foreground_image = read_image(entry_1.get())

    if entry_2.index("end") == 0:
        randNum = randint(0, 24)
        b_img = getJson(entry_3.get())
        i_img = b_img['data']['children'][randNum]['data']['url']
        print(i_img)
        urllib.request.urlretrieve(i_img, "reddit.jpg")
        background_image = read_image("reddit.jpg")
    else:
        background_image = read_image(entry_2.get())


    print(foreground_image.shape)
    print(background_image.shape)
    
    background_image = resize_image(foreground_image, background_image)
    
    print(foreground_image.shape)
    print(background_image.shape)
    
    is_green = find_green(foreground_image)

    fix_green = fix_image_noise(foreground_image, is_green)

    final_image = merge_image(foreground_image, background_image, fix_green)
    
    display_image(foreground_image, final_image)
    
    
def find_green_avg_std(img):
    
    green_values = list()
    
    for x in img:
        for y in x:
            green_values.append(y[1])
            
    avg = np.mean(green_values)
    std = np.std(green_values)
    
    return avg, std


def resize_image(foreground_image, background_image):
    
    x_len = len(foreground_image)
    y_len = len(foreground_image[0])
    
    new = np.zeros(foreground_image.shape)
    
    if x_len > len(background_image) or y_len > len(background_image[0]):
        print("Cannot use image smaller than original")
        messagebox.showerror("Error", "Foreground cannot be bigger than background")
        return
        # sys.exit()
        
    if x_len < len(background_image) and y_len < len(background_image[0]):
        
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
    # Returns image as a np array.
    return img


def find_green(image):

    green_avg, green_std = find_green_avg_std(image)
    
    print(green_avg, " ", green_std)
    
    shape = image.shape
    shape = shape[0:2]
    is_green = np.zeros(shape)
        
    for x in range(len(image)): 
        for y in range(len(image[x])):
            # if image[x][y][0] < 50 and image[x][y][1] > green_avg - green_std and image[x][y][1] < green_avg + green_std*2 and image[x][y][2] < 10:
            red = int(image[x][y][0])
            blue = int(image[x][y][2])
            color_sum = red + blue
            if image[x][y][1] > color_sum:
                # print( str(image[x][y][1]) + " vs " + str(color_sum))
                is_green[x][y] = 1
    
    # Returns boolean array with true in green areas
    return is_green


def fix_image_noise(image, is_green):

    green_avg, green_std = find_green_avg_std(image)

    for x in range(len(image)):
        for y in range(len(image[x])):
            if image[x][y][1] > 80 and image[x][y][2] > 50 and image[x][y][1] < 40:
                is_green[x][y] = 0

    return is_green



def merge_image(image, background, is_green):

    for x in range(len(image)):
        for y in range(len(image[x])):
            if is_green[x][y] == 1:
                image[x][y] = background[x][y]

    return image  # returns final image as a np array
    
    
def display_image(initial_image, final_image):

    plt.interactive(False)
    plt.imshow(initial_image)
    plt.show()
    plt.imshow(final_image)
    plt.show()

    return


window = Tk()
window.title("Green Screen")
window.geometry("600x200")
window.resizable(False, False)
window.configure(background='grey')

label_1 = Label(window, text="Foreground Image:", background="grey", justify="left")
entry_1 = Entry(window)

label_2 = Label(window, text="Background Image:", background="grey", justify="left")
entry_2 = Entry(window)

label_3 = Label(window, text="Background Image (Reddit URL):", background="grey", justify="left")
entry_3 = Entry(window)

button_1 = Button(window, text="Load Image", command=main, background="grey")

label_1.grid(row=0, column=0, columnspan=1)
entry_1.grid(row=0, column=1, columnspan=1)

label_2.grid(row=1, column=0)
entry_2.grid(row=1, column=1)

label_3.grid(row=2, column=0)
entry_3.grid(row=2, column=1)

button_1.grid(row=3, column=0)

label_4 = Label(window, text="Developed by: Victor Fernandez, Danner Pachecho & Jose Nieto", background="grey", justify="left")
label_4.grid(row="4", column=0, ipady=(20))

label_5 = Label(window, text="Repo: https://github.com/janietom2/greenscreenremoval", background="grey", justify="left")
label_5.grid(row="5", column=0, ipady=(5))


window.mainloop()

