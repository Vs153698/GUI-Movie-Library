import tkinter as tk
from data.colors import COLORS
from PIL import Image,ImageTk
class Home:
    """This is a homepage class of our movie library"""
    def __init__(self,window,bg_color,relief=tk.SUNKEN,side=tk.LEFT):
        self.frame=tk.Frame(master=window,
                            bg=bg_color,
                            name='home',
                            relief=relief
                            )
        self.side=side
        self.bg_color = bg_color
        self.frame_content()

        self.add_frame()
    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH,expand=True)
    def frame_content(self):
        course=tk.Label(self.frame,
                        text = "Movie Library",
                        bg=self.bg_color,
                        fg =COLORS.BLACK,
                        font=('Helvetica',20,'bold'))
        course.place(x=335,y=20)
        developer = tk.Label(self.frame,
                          text="(Vaibhav S. Bhadouria)",
                          bg=self.bg_color,
                          fg=COLORS.BLACK,
                          font=('Helvetica', 16, 'bold'))
        developer.place(x=310, y=60)
        self.render_image()
        course = tk.Label(self.frame,
                          text="Capstone Project - Movie Library with Tkinter",
                          bg=COLORS.BLACK,
                          fg=COLORS.WHITE,
                          font=('Helvetica', 20, 'bold'))
        course.place(x=120, y=630)

    def render_image(self):
        load = Image.open('images/home/python_logo.png')
        render = ImageTk.PhotoImage(load)
        img_lb = tk.Label(self.frame, image=render, bg=COLORS.ORANGE)
        img_lb.image = render
        img_lb.place(x=160, y=100)
