

from libreria import * 

cuentas = [0]
entradas_hoy = []
lista_pedido_en_texto = []
    

entradas_temporales = []
def accion_abrir_ventana_gastos(boton):
    abrir_ventana_y_configurar("ventana_gastos")

def accion_abrir_ventana_productos(boton):
    abrir_ventana_y_configurar("ventana_productos")

def accion_abrir_ventana_pedidos(boton):
    abrir_ventana_y_configurar("ventana_pedido")

def accion_boton_pedido_listo(boton):
    print("pedido listo")
     
   # entrada_hoy_datos = {"fecha": fecha_de_hoy(), entradas_hoy} 
    entradas = {}
    entradas_bd = {"entradas": entradas}
    cuentas[0] = 0
    cuenta = dar_formato_de_guaranies_a_numero(0)
    cambiar_texto_a_etiqueta(cuenta,"etiqueta_valor_total_a_pagar")
    lista_pedido_en_texto.clear()
    
    etiqueta_lista = builder.get_object("etiqueta_lista_del_pedido")
    etiqueta_lista.set_text("Ningun producto agregado al pedido")

    ventana = builder.get_object("ventana_pedido")
    ventana.hide()
    
def accion_boton_agregar_al_pedido(boton):
    cuenta_total_del_pedido = cuentas[0] 
    productos = leer_base_de_datos_productos()
    producto = productos[id_del_producto[0]]

    precio = producto["precio"]
    nueva_cuenta = cuenta_total_del_pedido + int(precio)
    cuenta = dar_formato_de_guaranies_a_numero(nueva_cuenta)
    cambiar_texto_a_etiqueta(cuenta,"etiqueta_valor_total_a_pagar")
    
    cuentas[0] = nueva_cuenta
    entradas_temporales.append(producto)


    precio_formateado_de_producto = dar_formato_de_guaranies_a_numero(int(precio)) 
    etiqueta_lista = builder.get_object("etiqueta_lista_del_pedido")
    

    nuevo_producto = producto["nombre"] + "\n"
    
    lista_pedido_en_texto.append(nuevo_producto)

    lista_en_texto = ""
    for producto_texto in lista_pedido_en_texto:
        lista_en_texto += producto_texto
   
    etiqueta_lista.set_text(lista_en_texto)

configurar_boton("boton_gastos",accion_abrir_ventana_gastos)
configurar_boton("boton_pedidos",accion_abrir_ventana_pedidos)
configurar_boton("boton_productos",accion_abrir_ventana_productos)

configurar_boton("boton_agregar_al_pedido",accion_boton_agregar_al_pedido)
configurar_boton("boton_pedido_cliente_listo",accion_boton_pedido_listo)


##############################
#ventana productos
##############################

def agregar_producto_a_datos(nombre,precio,productos):
    producto = {"nombre": nombre, "precio": precio}
    productos.append(producto)

def accion_boton_agregar_producto(boton):
    nombre = consegir_texto_desde_entrada("entrada_producto_nombre") 
    precio = consegir_texto_desde_entrada("entrada_producto_valor") 
  
    productos = leer_base_de_datos_productos() 
    agregar_producto_a_datos(nombre,precio,productos)
    
    productos_base_datos = {"productos": productos}
    
    datos_serializados_productos = json.dumps(productos_base_datos, indent=4)
    escribir_base_de_datos_productos(datos_serializados_productos)


configurar_boton("boton_agregar_producto",accion_boton_agregar_producto)

configurar_lista_productos()

iniciar()
