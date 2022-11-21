import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Footer():
    def __init__(self, window):
        self.window = window
        
        check_editable = Gtk.CheckButton(label="Editable")
        check_editable.set_active(True)
        check_editable.connect("toggled", self.on_editable_toggled)
        window.grid.attach(check_editable, 0, 2, 1, 1)

        check_cursor = Gtk.CheckButton(label="Cursor Visible")
        check_cursor.set_active(True)
        check_editable.connect("toggled", self.on_cursor_toggled)
        window.grid.attach_next_to(check_cursor, check_editable, Gtk.PositionType.RIGHT, 1, 1)

        radio_wrapnone = Gtk.RadioButton.new_with_label_from_widget(None, "No Wrapping")
        window.grid.attach(radio_wrapnone, 0, 3, 1, 1)

        radio_wrapchar = Gtk.RadioButton.new_with_label_from_widget(radio_wrapnone, "Character Wrapping")
        window.grid.attach_next_to(radio_wrapchar, radio_wrapnone, Gtk.PositionType.RIGHT, 1, 1)

        radio_wrapword = Gtk.RadioButton.new_with_label_from_widget(radio_wrapnone, "Word Wrapping")
        window.grid.attach_next_to(radio_wrapword, radio_wrapchar, Gtk.PositionType.RIGHT, 1, 1)

        radio_wrapnone.connect("toggled", self.on_wrap_toggled, Gtk.WrapMode.NONE)
        radio_wrapchar.connect("toggled", self.on_wrap_toggled, Gtk.WrapMode.CHAR)
        radio_wrapword.connect("toggled", self.on_wrap_toggled, Gtk.WrapMode.WORD)

    def on_editable_toggled(self, widget):
        self.window.textview.set_editable(widget.get_active())

    def on_cursor_toggled(self, widget):
        self.window.textview.set_cursor_visible(widget.get_active())

    def on_wrap_toggled(self, widget, mode):
        self.window.textview.set_wrap_mode(mode)
