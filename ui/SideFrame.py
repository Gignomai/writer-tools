from tkinter import Frame


class SideFrame(Frame):

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.init_side_frame()

    def init_side_frame(self):
        # create the Button bar panel
        left_frame = Frame(self.root, bg='grey')
        left_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
