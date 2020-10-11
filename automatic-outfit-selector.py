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

        self.top_image_pat = self.top_images[0]  # Save single top

        self.tops_frame = tk.Frame(self.root)    # Create and add top image into Frame (first image to be displayed)


        self.create_background() # Create background

    def create_background(self):
        self.root.title(WINDOW_TITLE) # Add title to window
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT)) #size of window

        def create_photos(self):
            image_file = Image.open(image_path)
            image_resize = imge_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
            tk_photo = imageTk.PhotoImage(image_resize)
            image_label = tk.Label(frame, image = tk_photo, anchor = tk.Center)
            #weird tkinter quirk
            image_label.image = tk_photo

            #we can add later
            return image_label
            #7:19

root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
