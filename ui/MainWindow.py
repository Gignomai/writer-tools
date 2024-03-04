from tkinter import Frame

from ui.MenuBar import MenuBar
from ui.SideFrame import SideFrame
from ui.MainFrame import MainFrame
from ui.StatusBar import StatusBar


class MainWindow(Frame):

    def __init__(self, root):
        super().__init__()

        self.root = root
        self.init_ui()

    def init_ui(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=5)

        # create a menubar
        MenuBar(self.root)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        SideFrame(self.root)
        MainFrame(self.root)

        StatusBar(self.root)
