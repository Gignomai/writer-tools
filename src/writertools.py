from modules.main_window import MainWindow

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
