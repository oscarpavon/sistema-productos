from libreria import *

software_list = [
]

class TreeViewFilterWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__(title="Treeview Filter Demo")
        self.set_border_width(10)

        # Setting up the self.grid in which the elements are to be positioned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        # Creating the ListStore model
        self.software_liststore = Gtk.ListStore(str, int)
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))
        self.current_filter_language = None

        # Creating the filter, feeding it with the liststore model
        self.language_filter = self.software_liststore.filter_new()
        # setting the filter function, note that we're not using the
        self.language_filter.set_visible_func(self.language_filter_func)

        # creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView(model=self.language_filter)
        for i, column_title in enumerate(
            ["Nombre", "Cantidad"]
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        # creating buttons to filter by programming language, and setting up their events
        self.buttons = list()
        button_add = Gtk.Button(label="Agregar")
        button_mod = Gtk.Button(label="Modificar")

        self.button_add_inventary = Gtk.Button(label="Agregar al inventario")

        self.buttons.append(button_add)
        self.buttons.append(button_mod)

        button_add.connect("clicked",self.on_add_button)
        self.button_add_inventary.connect("clicked",self.on_new_inventary_item)

        for prog_language in ["None"]:
            button = Gtk.Button(label=prog_language)
            self.buttons.append(button)
            button.connect("clicked", self.on_selection_button_clicked)
       
        self.entry_name = Gtk.Entry()
        self.entry_count = Gtk.Entry()         
        self.label_name = Gtk.Label()         

        self.label_name.set_text("Nombre")

        self.label_count = Gtk.Label()         

        self.label_count.set_text("Cantidad")

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(
            self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1
        )
    
        self.grid.attach_next_to(self.label_name,button_add,Gtk.PositionType.BOTTOM,1,1)
        self.grid.attach_next_to(self.label_count,self.label_name,Gtk.PositionType.RIGHT,1,1)

        self.grid.attach_next_to(self.entry_name,self.label_name,Gtk.PositionType.BOTTOM,1,1)

        self.grid.attach_next_to(self.entry_count,self.entry_name,Gtk.PositionType.RIGHT,1,1)

        self.grid.attach_next_to(self.button_add_inventary,self.entry_count,Gtk.PositionType.RIGHT,1,1)
        

        self.scrollable_treelist.add(self.treeview)

        self.show_all()
        
        self.entry_name.hide()
        self.entry_count.hide()
        self.label_name.hide()
        self.label_count.hide()
        self.button_add_inventary.hide()

    def language_filter_func(self, model, iter, data):
        """Tests if the language in the row is the one in the filter"""
        if (
            self.current_filter_language is None
            or self.current_filter_language == "None"
        ):
            return True
        else:
            return model[iter][2] == self.current_filter_language

    def on_selection_button_clicked(self, widget):
        """Called on any of the button clicks"""
        # we set the current language filter to the button's label
        self.current_filter_language = widget.get_label()
        print("%s language selected!" % self.current_filter_language)
        # we update the filter, which updates in turn the view
        self.language_filter.refilter()
    def on_add_button(self,button):
        self.entry_name.show()
        self.entry_count.show()
        self.label_name.show()
        self.label_count.show()
        self.button_add_inventary.show()

    def on_new_inventary_item(self,button):
        name = self.entry_name.get_text()
        software_list.append((name,12))
        self.software_liststore.append((name,12))
        self.entry_name.hide()
        self.button_add_inventary.hide()
        self.entry_name.set_text("")
        self.entry_count.set_text("0")
        
        self.entry_count.hide()
        self.label_name.hide()
        self.label_count.hide()

