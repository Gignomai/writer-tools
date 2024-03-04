from tkinter import Frame


class MainFrame(Frame):

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.init_main_frame()

    def init_main_frame(self):
        # create the Button bar panel
        right_frame = Frame(self.root, bg='grey')
        right_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
