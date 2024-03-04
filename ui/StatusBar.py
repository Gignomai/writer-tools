from tkinter import Frame, Label


class StatusBar(Frame):

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.init_statusbar()

    def init_statusbar(self):
        bottom_frame = Frame(self.root)
        bottom_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='we')
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)

        left_label = Label(bottom_frame, text="Left", anchor='w')
        left_label.grid(row=0, column=0, sticky='we', padx=5)

        right_label = Label(bottom_frame, text="Right", anchor='e')
        right_label.grid(row=0, column=1, sticky='we', padx=5)
