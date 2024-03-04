from tkinter import Menu

from ui.FileMenu import FileMenu
from ui.HelpMenu import HelpMenu


class MenuBar(Menu):

    def __init__(self, root):
        super().__init__()

        self.root = root
        self.init_ui()

    def init_ui(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        FileMenu(menubar)
        HelpMenu(menubar)
