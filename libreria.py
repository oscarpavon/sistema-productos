
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from datetime import date
from datetime import datetime
import os.path
import json


builder = Gtk.Builder()
builder.add_from_file("ui.glade")

combolist = []
id_del_producto = -1

def dar_formato_de_guaranies_a_numero(numero):
    numero_texto = "{:,}".format(numero) + " Gs"
    return numero_texto 

def cambiar_texto_a_etiqueta(nuevo_texto,nombre_de_la_etiqueta):
    etiqueta = builder.get_object(nombre_de_la_etiqueta)
    etiqueta.set_text(nuevo_texto)


def leer_base_de_datos_productos():
    f = open("bd_productos.txt", "r")
    fr = f.read()
    productos_base_datos = json.loads(fr) 
    return productos_base_datos["productos"]


def escribir_base_de_datos(nombre,datos):
    file = open(nombre, 'w')
    file.write(datos)
    file.close()

def escribir_base_de_datos_productos(datos):
    escribir_base_de_datos("bd_productos.txt",datos)
    
def match_selected(completion, model, iter):
    combolist[0].set_active_iter (iter)

def changed(combo):
    print('active', combo.get_active())
    id_del_producto = combo.get_active()


def configurar_lista_productos():
   store = Gtk.ListStore(str)
   combo = Gtk.ComboBox(model=store, has_entry=True) 

   combo.set_entry_text_column(0) 
   productos = leer_base_de_datos_productos()
   for element in productos:
       store.append((element["nombre"],))

   completer = Gtk.EntryCompletion() 
   completer.set_model(combo.get_model()) 
   completer.set_text_column(0) 
   completer.connect("match-selected", match_selected)
  
   combo.get_child().set_completion(completer) 
   combo.connect('changed', changed)  
  
   box = builder.get_object("caja01")
   box.add(combo)
   combo.show()
   combolist.append(combo)


def cerra_ventana(widget,event):
    widget.hide()
    return True


def abrir_ventana_y_configurar(nombre):
    ventana_gastos = builder.get_object(nombre)    
    ventana_gastos.show()
    ventana_gastos.connect("delete-event",cerra_ventana)

def configurar_boton(nombre,accion):
    boton = builder.get_object(nombre)
    boton.connect("clicked",accion)

def consegir_texto_desde_entrada(nombre):
    entrada = builder.get_object(nombre)
    return entrada.get_text()   

def iniciar():
    ventana_principal = builder.get_object("ventana_principal")
    ventana_principal.connect("destroy",Gtk.main_quit)
    ventana_principal.show_all()
    Gtk.main()

def fecha_de_hoy():
    hoy = date.today()
    hoy = hoy.strftime("%m-%d-%Y")
    return hoy

nombre = "comida"
precio = 5000

gastos_data = []


def agregar_gasto():
    gasto = {"nombre": nombre, "precio": precio}
    gastos_data.append(gasto)

agregar_gasto()


gastos = { "gastos": gastos_data }

cod = json.dumps(gastos, indent=4)
print(cod)

