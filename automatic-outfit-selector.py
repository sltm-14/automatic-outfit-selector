import os
import random

import tkinter as tk              # To create the GUI
from PIL import Image, ImageTk    # To work with images

WINDOW_TITLE = "My Wardrobe"

WINDOW_WIDTH  = 220
WINDOW_HEIGHT = 550
IMG_WIDTH     = 250
IMG_HEIGHT    = 250

# Store all the tops into a file we can access and skip hidden files
ALL_TOPS    = [str('tops/') + imagefile for imagefile in os.listdir('tops/') if not imagefile.startswith('.')]
ALL_BOTTOMS = [str('bottoms/') + imagefile for imagefile in os.listdir('bottoms/') if not imagefile.startswith('.')]

class WardrobeApp:
    def __init__(self,root):
        # Root will be a tkinter object
        self.root = root

        # Show top and bottoms image in the window
        self.top_images = ALL_TOPS
        self.bottom_images = ALL_BOTTOMS

        # Save single top
        self.top_image_path = self.top_images[0]
        self.bottom_image_path = self.bottom_images[0]

        # Create and add top image into Frame (first image to be displayed)
        self.tops_frame = tk.Frame(self.root)
        self.top_image_label = self.create_photo(self.top_image_path,self.tops_frame)
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_image_label = self.create_photo(self.bottom_image_path,self.bottom_frame)

        # add it to pack
        self.top_image_label.pack(side=tk.TOP)
        self.bottom_image_label.pack(side=tk.TOP)

        # Create background
        self.create_background()

    def create_background(self):
        # Add title to window
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT)) #size of window

        #add all buttons
        self.create_buttons()

        # add clothing
        self.tops_frame.pack(fill=tk.BOTH,expand=tk.YES)
        self.bottom_frame.pack(fill=tk.BOTH,expand=tk.YES)

    def create_buttons(self):
        top_prev_button = tk.Button(self.tops_frame,text="Prev", command = self.get_next_top)
        top_prev_button.pack(side=tk.LEFT)

        top_next_button = tk.Button(self.tops_frame,text="Next", command = self.get_prev_top)
        top_next_button.pack(side=tk.LEFT)

        bottom_prev_button = tk.Button(self.bottom_frame,text="Prev", command = self.get_next_bottom)
        bottom_prev_button.pack(side=tk.LEFT)

        bottom_next_button = tk.Button(self.bottom_frame,text="Next", command = self.get_prev_bottom)
        bottom_next_button.pack(side=tk.LEFT)

        create_outfit_button = tk.Button(self.tops_frame, text="Create Outfit", command=self.create_outfit)
        create_outfit_button.pack(side=tk.RIGHT)

    def update_photo(self, new_image, image_label):
        new_image_file = Image.open(new_image)
        image = new_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo


    def _get_next_item(self,current_item,category,increment = True):

        # If we know where the current item index is in a category, then we find the pic before/after it
        item_index = category.index(current_item)
        final_index = len(category)-1
        next_index = 0

        #consider the edge cases
        if increment and item_index == final_index:
            #add the end and need to up,cycle up to beggining
            next_index = 0
        elif not increment and item_index == 0:
            #cycle back to expand
            next_index = final_index
        else:
            #regular up and down
            #based on nincrement
            increment = 1 if increment else -1
            next_index = item_index + increment

        next_image = category[next_index]

        # Reset and updated image based on next_image path
        if current_item in self.top_images:
            image_label = self.top_image_label
            self.top_image_path = next_image
        else:
            image_label = self.bottom_image_label
            self.bottom_image_path = next_image

        #Use update function to change the images
        self.update_photo(next_image,image_label)

    def get_next_top(self):
        self._get_next_item(self.top_image_path, self.top_images)

    def get_prev_top(self):
        self._get_next_item(self.top_image_path, self.top_images, increment=False)

    def get_next_bottom(self):
        self._get_next_item(self.bottom_image_path, self.bottom_images)

    def get_prev_bottom(self):
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=False)

    def create_photo(self,image_path,frame):
        image_file = Image.open(image_path)
        image_resized = image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)
        image_label = tk.Label(frame, image = tk_photo, anchor = tk.CENTER)
        #weird tkinter quirk
        image_label.image = tk_photo

        # we can add later
        return image_label

    def create_outfit(self):
        # randomly select an outfit
        new_top_index = random.randint(0, len(self.top_images)-1)
        new_bottom_index = random.randint(0, len(self.bottom_images)-1)

        # add the clothes onto the screen
        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)

root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
