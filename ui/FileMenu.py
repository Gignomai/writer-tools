from tkinter import Menu


class FileMenu(Menu):

    def __init__(self, menubar):
        super().__init__()

        self.menubar = menubar
        self.init_file_menu()

    def init_file_menu(self):
        # create the file_menu
        file_menu = Menu(
            self.menubar,
            tearoff=0
        )

        # add menu items to the File menu
        # file_menu.add_command(label="Exit", command=self.on_exit)
        file_menu.add_command(label='New')
        file_menu.add_command(
            label='Open...',
            command=self.on_open
        )
        file_menu.add_command(label='Close')
        file_menu.add_separator()

        # add Exit menu item
        file_menu.add_command(
            label='Exit',
            command=self.master.destroy
        )

        # add the File menu to the menubar
        self.menubar.add_cascade(
            label="File",
            menu=file_menu
        )

    def on_open(self):
        print("open a file")
