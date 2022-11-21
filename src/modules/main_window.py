from modules.toolbar import Toolbar
from modules.text_view import TextView
from modules.footer import Footer

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Writer's Tool")

        # self.set_default_size(1000, 800)
        self.maximize()
        
        self.grid = Gtk.Grid()
        self.add(self.grid)
        
        scrolledwindow = TextView.create_scrolledwindow()
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = TextView.create_textview()
        self.textbuffer = TextView.create_textbuffer(self.textview) 
        self.textbuffer.set_text(
            """
            This is some text inside of a Gtk.TextView.
            Select text and click one of the buttons 'bold', 'italic', 
            or 'underline' to modify the text accordingly.
            """
        )
        scrolledwindow.add(self.textview)
                        
        self.grid.attach(Toolbar(self), 0, 0, 3, 1)
        
        Footer(self)
