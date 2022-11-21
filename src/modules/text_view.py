import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class TextView():
    def create_scrolledwindow():
        
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        return scrolledwindow

    def create_textview():
        textview = Gtk.TextView()        
        return textview
        
    
    def create_textbuffer(textview):
        textbuffer = textview.get_buffer()
        
        return textbuffer
