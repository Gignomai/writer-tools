import gi
from modules.search_dialog import SearchDialog

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class Toolbar(Gtk.Toolbar):
    def __init__(self, window):      
        Gtk.Toolbar.__init__(self)
        
        self.window = window
        
        tag_bold = window.textbuffer.create_tag("bold", weight=Pango.Weight.BOLD)
        tag_italic = window.textbuffer.create_tag("italic", style=Pango.Style.ITALIC)
        tag_underline = window.textbuffer.create_tag("underline", underline=Pango.Underline.SINGLE)
        self.tag_found = window.textbuffer.create_tag("found", background="yellow")
        
        self.insert(self.create_toolbutton("format-text-bold-symbolic", tag_bold), 0)
        self.insert(self.create_toolbutton("format-text-italic-symbolic", tag_italic), 1)
        self.insert(self.create_toolbutton("format-text-underline-symbolic", tag_underline), 2)

        self.insert(Gtk.SeparatorToolItem(), 3)
                
        self.insert(self.create_radiobutton("format-justify-left-symbolic", Gtk.Justification.LEFT), 4)
        self.insert(self.create_radiobutton("format-justify-center-symbolic", Gtk.Justification.CENTER), 5)
        self.insert(self.create_radiobutton("format-justify-right-symbolic", Gtk.Justification.RIGHT), 6)
        self.insert(self.create_radiobutton("format-justify-fill-symbolic", Gtk.Justification.FILL), 7)

        self.insert(Gtk.SeparatorToolItem(), 8)
        
        self.insert(self.create_button_clear(), 9)
        
        self.insert(Gtk.SeparatorToolItem(), 10)
        
        self.insert(self.create_button_search(), 11)
                
    def create_toolbutton(self, icon_name, tag):
        click_event = self.on_button_clicked
        
        button = Gtk.ToolButton()
        button.set_icon_name(icon_name)
        button.connect("clicked", click_event, tag)
        
        return button
        
    def create_radiobutton(self, icon_name, gtk_justification):
        click_event = self.on_button_clicked
        
        radiobutton = Gtk.RadioToolButton()
        radiobutton.set_icon_name(icon_name)
        radiobutton.connect("toggled", self.on_justify_toggled, gtk_justification)
        
        return radiobutton
        
    def create_button_clear(self):
        button_clear = Gtk.ToolButton()
        button_clear.set_icon_name("edit-clear-symbolic")
        button_clear.connect("clicked", self.on_clear_clicked)
        
        return button_clear
        
    def create_button_search(self):        
        button_search = Gtk.ToolButton()
        button_search.set_icon_name("system-search-symbolic")
        button_search.connect("clicked", self.on_search_clicked)
        
        return button_search
        
    def on_button_clicked(self, toolbutton, tag):
        bounds = self.window.textbuffer.get_selection_bounds()
        
        if len(bounds) == 2:
            start, end = bounds
            if start.has_tag(tag):
                self.window.textbuffer.remove_tag(tag, start, end)
            else:
                self.window.textbuffer.apply_tag(tag, start, end)
                
    def on_justify_toggled(self, justification):
        self.textview.set_justification(justification)
        
    def on_clear_clicked(self, toolbutton):
        start = self.window.textbuffer.get_start_iter()
        end = self.window.textbuffer.get_end_iter()
        self.window.textbuffer.remove_all_tags(start, end)

    def on_search_clicked(self, sthg):
        dialog = SearchDialog(self.window)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            cursor_mark = self.window.textbuffer.get_insert()
            start = self.window.textbuffer.get_iter_at_mark(cursor_mark)
            if start.get_offset() == self.window.textbuffer.get_char_count():
                start = self.window.textbuffer.get_start_iter()

            self.search_and_mark(dialog.entry.get_text(), start)

        dialog.destroy()
    
    def search_and_mark(self, text, start):
        end = self.window.textbuffer.get_end_iter()
        match = start.forward_search(text, 0, end)

        if match is not None:
            match_start, match_end = match
            self.window.textbuffer.apply_tag(self.tag_found, match_start, match_end)
            self.search_and_mark(text, match_end)
