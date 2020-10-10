import tkinter as tk              # To create the GUI
from PIL import Image, ImageTk  # To work with images
#from playsound import playsound # To play with oudio

class WardrobeApp:
    def __init__(self,root):
        self.root = root


root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
