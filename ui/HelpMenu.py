from tkinter import Menu


class HelpMenu(Menu):

    def __init__(self, menubar):
        super().__init__()
        self.menubar = menubar
        self.init_help_menu()

    def init_help_menu(self):
        # create the Help menu
        help_menu = Menu(
            self.menubar,
            tearoff=0
        )

        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About...')

        # add the Help menu to the menubar
        self.menubar.add_cascade(
            label="Help",
            menu=help_menu
        )

    def on_exit(self):
        self.quit()
