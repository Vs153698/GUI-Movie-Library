import tkinter as tk
from data.colors import COLORS
from data.menus import MENU
# we will do exact import here because button and left frame is in same package
from widget.button.Button import Button
from widget.righframe.Right_Frame import Right_Frame
class Left_Frame:
    """
    It will create an frame inside the window
    """
    def __init__(self,window,name):
        self.frame = tk.Frame(master=window, name=name, bg=COLORS.BLACK)
        self.master=window
        self.add_frame()
        self.add_menu()

    def add_frame(self):
        self.frame.pack(side=tk.LEFT,fill=tk.Y,pady=(62,0))

    # method for click event
    # we used this function as paramter in button
    def handle_click(self,event):
        self.manage_button_colors(event)
        page_name=str(event.widget).split('.')[2]
        print(page_name)
        # self is left frame master=root
        # right frame is in children of master
        # right frame is in children of master
        rightframe=self.master.children['rightframe']
        # destroy children
        Right_Frame.destroy_children(rightframe)

        #add new page
        Right_Frame.frame_content(rightframe,page_name)
    def add_menu(self):
        # we will use for loop
        for menu_keys,menu_name in MENU.items():
            if menu_keys=='about':
                button=Button(self.frame,menu_keys,menu_name,COLORS.BLACK,COLORS.ORANGE, 18,2,handle_click=self.handle_click,side=tk.BOTTOM)
            else:
                button=Button(self.frame, menu_keys, menu_name, COLORS.BLACK, COLORS.ORANGE, 18, 2,handle_click=self.handle_click,side=tk.TOP)
                if menu_keys=='home':
                    self.selected_button_color(button.button)

    def manage_button_colors(self,event):
        # clicked button=event.widget
        # all the menu buttons --> event.widget.master.children
        for child in event.widget.master.winfo_children():
            if child == event.widget:
                child.configure(bg=COLORS.ORANGE,fg=COLORS.WHITE)
            else:
                child.configure(bg=COLORS.BLACK,fg=COLORS.ORANGE)
    def selected_button_color(self,button):
        button.configure(bg=COLORS.ORANGE,fg=COLORS.WHITE)