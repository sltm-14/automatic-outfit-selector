import os
import tkinter as tk              # To create the GUI
from PIL import Image, ImageTk  # To work with images
#from playsound import playsound # To play with oudio

WINDOW_TITLE = "My Wardrobe"

WINDOW_WIDTH  = 220
WINDOW_HEIGHT = 500
IMG_WIDTH     = 250
IMG_HEIGHT    = 250

# Store all the tops into a file we can access and skip hidden files
ALL_TOPS = [str('tops/') + imagefile for imagefile in os.listdir('tops/') if not imagefile.startswith('.')]

class WardrobeApp:
    def __init__(self,root):
        # Root will be a tkinter object
        self.root = root

        # Show top image in the window
        self.top_images = ALL_TOPS

        # Save single top
        self.top_image_path = self.top_images[1]

        # Create and add top image into Frame (first image to be displayed)
        self.tops_frame = tk.Frame(self.root)
        self.top_image_label = self.create_photo(self.top_image_path,self.tops_frame)

        # add it to pack
        self.top_image_label.pack(side=tk.TOP)

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

    def create_buttons(self):
        top_prev_button = tk.Button(self.tops_frame,text="Prev", command = self.get_next_top)
        top_prev_button.pack(side=tk.LEFT)

        top_next_button = tk.Button(self.tops_frame,text="Next", command = self.get_prev_top)
        top_next_button.pack(side=tk.LEFT)

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

        #Use update function to change the images
        self.update_image(next_image,image_label)

    def get_next_top(self):
        self._get_next_item(self.top_image_path, self.top_images)

    def get_prev_top(self):
        self._get_next_item(self.top_image_path, self.top_images, increment=False)

    def update_image(self,new_image_path,image_label):
        #collect and change image into tk photo obj
        image_file = Image.open(new_image_path)
        image_resized = image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)

        #Update based on provided image Label
        image_label.configure(image = tk_photo)

        #weird tkinter.image = tk_photo
        image_label.image = tk_photo

    def create_photo(self,image_path,frame):
        image_file = Image.open(image_path)
        image_resized = image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)
        image_label = tk.Label(frame, image = tk_photo, anchor = tk.CENTER)
        #weird tkinter quirk
        image_label.image = tk_photo

        # we can add later
        return image_label
        #7:19

root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
