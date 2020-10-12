import os
import tkinter as tk              # To create the GUI
from PIL import Image, ImageTk  # To work with images
#from playsound import playsound # To play with oudio

WINDOW_TITLE = "My Wardrobe"

WINDOW_WIDTH  = 500
WINDOW_HEIGHT = 220

IMG_WIDTH  = 250
IMG_HEIGHT = 250

# Store all the tops into a file we can access and skip hidden files
ALL_TOPS = [str('tops/') + imagefile for imagefile in os.listdir('tops/') if not imagefile.startswith('.')]

class WardrobeApp:
    def __init__(self,root):
        self.root = root                         # Root will be a tkinter object

        self.top_images = ALL_TOPS               # Show top image in the window

        self.top_image_path = self.top_images[0]  # Save single top

        self.tops_frame = tk.Frame(self.root)    # Create and add top image into Frame (first image to be displayed)
        self.top_image_label = self.create_photo(self.top_image_path,self.tops_frame) # to pack this image into the tops frame and the pack the tops frame into the root
        self.top_image_label.pack(side=tk.TOP) # add it to pack

        self.tops_frame.pack(fill=tk.BOTH,expand=tk.YES)

        self.create_background() # Create background

    def create_background(self):
        self.root.title(WINDOW_TITLE) # Add title to window
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT)) #size of window

    def create_photo(self,image_path,frame):
        image_file = Image.open(image_path)
        image_resized = image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)
        image_label = tk.Label(frame, image = tk_photo, anchor = tk.CENTER)
        #weird tkinter quirk
        image_label.image = tk_photo

        #we can add later
        return image_label
        #7:19

root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
