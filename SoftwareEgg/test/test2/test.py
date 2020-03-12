
import os
try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu


CURDIR = os.path.dirname(__file__)
UI_FILE = os.path.join(CURDIR, 'test.ui')

class Application:
    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file(UI_FILE)

        #3: Create the widget using a master as parent
        
        
        self.mainwindow = builder.get_object('Frame_1')
        
        #4: connect callbacks
        self.builder.connect_callbacks(self)
        
    def onClick(self):
        
        UsernameString = self.builder.tkvariables['tteexx']
        print(UsernameString.get())
        UsernameString.set("  dsf  sdf  ")
        
        builder2 = pygubu.Builder()
        builder2.add_from_file('test.ui')
        
        frame2 = builder2.get_object('Frame_2')
        builder2.connect_callbacks(self)

    def quit(self, event=None):
        self.mainwindow.quit()

        
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = Application()
    app.run()