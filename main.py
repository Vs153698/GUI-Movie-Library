"""
This is the main file of the movie library
Pages:
1) Home
2) Movie List
3) Movie Detail

"""
# from widget package import __init__.py Window
from widget import Window,Left_Frame,Right_Frame
from data import geometry
if __name__=='__main__':

    # Root Window
    root=Window('Movie Library')


    # Left Frame
    leftframe=Left_Frame(root.window,'leftframe')

    # Right Frame
    rightframe=Right_Frame(root.window,'rightframe')

    # start root window mainloop
    root.start_method()



