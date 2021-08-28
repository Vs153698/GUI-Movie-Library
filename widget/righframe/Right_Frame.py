import tkinter as tk
from data.colors import COLORS
from pages.home.Home import Home
from pages.movielist.Movie_List import MovieList,MovieDetail

class Right_Frame:
    """
    this will contain all items of right frame like movie list, homepage, movie detail and about page
    """
    bg_color=COLORS.ORANGE
    def __init__(self,window,name,relief=tk.SUNKEN,side=tk.LEFT):
        self.frame=tk.Frame(
            master=window,
            name = name,
            relief=relief,
            bg=Right_Frame.bg_color
        )
        self.side=side
        self.add_frame()
    def add_frame(self):
        # frame content
        self.frame_content()
        self.frame.pack(side=self.side,fill=tk.BOTH,expand=True)

    def frame_content(self,page_name='home'):
        try:
            incomingframe=self.frame
        except:
            incomingframe=self
        finally:
            if page_name == "home":
                # add home page
                Home(incomingframe,Right_Frame.bg_color)
            elif page_name == "movieList":
                # add movie list page
                MovieList(incomingframe,Right_Frame.bg_color)
            elif page_name == "movieDetail":
                # add movie detail page
                MovieDetail(incomingframe,Right_Frame.bg_color)

    def destroy_children(frame):
        # destroy yhe children
        for child in frame.winfo_children():
            child.destroy()
