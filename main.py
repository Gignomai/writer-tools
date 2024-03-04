from tkinter import Tk
from ui.MainWindow import MainWindow


def main():
    root = Tk()
    root.geometry("600x400")
    root.title("Writer's Tool")

    MainWindow(root)

    root.attributes('-zoomed', True)
    root.mainloop()


if __name__ == '__main__':
    main()
