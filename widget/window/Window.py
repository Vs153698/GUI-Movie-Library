import tkinter as tk
from data.colors import COLORS
from data.geometry import GEOMETRI
from data.menus import MENU

class Window:
    """
    This file will create a window
    """
    def __init__(self,title):
        self. window= tk.Tk()
        self.window.title(title)
        self.window.configure(bg=COLORS.BLACK)
        self.set_size()


    def start_method(self):
        self.window.mainloop()

    def set_size(self):
        w,h=GEOMETRI.MAIN_WINDOW_WIDTH,GEOMETRI.MAIN_WINDOW_HEIGHT
        self.window.geometry(f'{w}x{h}')
