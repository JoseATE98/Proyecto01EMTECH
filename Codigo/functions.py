from lifestore_file import lifestore_sales, lifestore_searches, lifestore_products
def searchProd(id):
  """
  Funcion       searchProd
  Definicion:   Esta funcion se encarga de buscar un produto en la lista de productos 
                por el ID y retornar toda la fila perteneciente al mismo.

  Inputs:       id(int):        ID del producto a buscar.

  Outputs:      producto(list): Producto correspondiente al ID buscado.
  """
  for producto in lifestore_products:        #Recorre lista de productos
    if producto[0] == id: 
      return producto                        #Regresa en caso de encontrar un producto
  return [id, 'No existe', 0, 'None', 0]


def productos_VenyBus(ventas, orden = True, refund = True):
  """
  Funcion       productos_VenyBus
  Definicion:   Funcion encargada de buscar los productos mas vendidos, los menos
                vendidos, asi como tambien trabaja con las busquedas mas realizadas
                y menos realizadas.

  Inputs:       ventas(lista):  La coleccion en la que se tiene que buscar y ordenar.
                orden(Bool):    Define el orden de mayor a menor (True) o visecersa.
                refund(Bool):   Decide si se tiene que contar los productos devueltos.

  Outputs:      nwventas(list): Lista que contiene el ID de los articulos y el numero
                                de ventas/busquedas que contiene.
  """
  nwventas = [] #Variable con lista vacia
  posnw = 0
  for venta in ventas: #Recorre la lista en la que se busca
    if len(venta) == 2 or refund or not venta[4]: #Comprueba que lista se recorre, si se cuentan los devueltos y si es devuelto el que se analiza.
      exist = False
      for i, nwventa in enumerate(nwventas): #Se comprueba si el producto esta o no agregado a la lista
        if nwventa[0] == venta[1]:
          exist = True
          posnw = i
      if exist: #En caso de existir se le suma una busqueda/venta
        nwventas[posnw][1] += 1
      else: #En caso de que no se agrega el nuevo valor
        nwventas += [[venta[1], 1]]
  nwventas = sorted(nwventas, key=lambda x: x[1], reverse=orden) #Se ordena por medio de las busquedas
  return nwventas #Se retorna la lista de respuesta


def filtrar_VenyBus(ventas, limit = 50, filter='all'):
  """
  Funcion       filtrar_VenyBus
  Definicion:   Funcion encargada de filtrar los resultados obtenidos, se observa si
                se tiene algun limite o si solo se quieren buscar de cierta categoria.

  Inputs:       ventas(lista):  Coleccion que se tiene que filtrar [ID, cantidad]
                limit(int):     Limite de registros a mostrar
                filter(string): Filtro que filtra sobre el tipo de categoria que se esta buscando

  Outputs:      nw(list): Lista que contiene los articulos filtrados [Numero, Nombre, Cantidad, Categoria]
  """
  nwventas = ventas
  i = 1
  nw = [] #Se crea lista vacia 
  for nwventa in nwventas: #Se recorre la lista que contiene las busquedas
    prod = searchProd(nwventa[0]) #Se busca el producto por ID
    if prod[3] == filter or filter == 'all': #Se ve si se tiene un filtro
      nw += [[i, prod[1], nwventa[1], prod[3]]] #Se agrega el producto
      i += 1
  return nw[0:min(limit, len(nw))] #Retorta lista final

def categorias_VenyBus(ventas, orden = True, refund = True):
  """
  Funcion       categorias_VenyBus
  Definicion:   Funcion encargada de obtener las ventas/busquedas por categoria

  Inputs:       ventas(lista):  La coleccion en la que se tiene que buscar y ordenar.
                orden(Bool):    Define el orden de mayor a menor (True) o visecersa.
                refund(Bool):   Decide si se tiene que contar los productos devueltos.

  Outputs:      nw(list): Lista que contiene los articulos filtrados [Numero, Categoria, ventas]
  """
  nwventas = [] #Se crea lista vacia
  posnw = 0
  for venta in ventas: #Se recorre la coleccion a buscar
    if len(venta) == 2 or refund or not venta[4]: #Se revisa si se cuentan los que se retornan
      exist = False
      prod = searchProd(venta[1]) #Se busca el producto
      for i, nwventa in enumerate(nwventas): #Se revisa si la categoria esta agregada
        if nwventa[0] == prod[3]:
          exist = True
          posnw = i
      if exist: #si esta agregada se le suma uno
        nwventas[posnw][1] += 1
      else: #Sino esta agregada se agrega un registro nuevo
        nwventas += [[prod[3], 1]]
  nwventas = sorted(nwventas, key=lambda x: x[1], reverse=orden) #Se ordenan por el # de ventas/busqeudas
  i = 1
  nw = [] #Se crea lista vacia
  for nwventa in nwventas: #Se coloca lista para imprimir 
    nw += [[i, nwventa[0], nwventa[1]]]
    i += 1
  return nw #Se retrna lista

def productos_rating(ventas, orden = True, refund = True):
  """
  Funcion       productos_rating
  Definicion:   Funcion encargada de obtener el rating de los productos dados

  Inputs:       ventas(lista):  La coleccion en la que se tiene que buscar y calificar.
                orden(Bool):    Define el orden de mayor a menor (True) o visecersa.
                refund(Bool):   Decide si se tiene que contar los productos devueltos.

  Outputs:      nwventas(list): Lista que contiene los articulos filtrados [ID, ventas, calificacion]
  """
  nwventas = [] #Creamos lista vacia
  posnw = 0
  for venta in ventas: #Recorremos la lista de ventas
    if refund or not venta[4]: #Vemos si contamos productos devueltos o no
      exist = False
      for i, nwventa in enumerate(nwventas): #Recorremos para comprobar si esta agregado
        if nwventa[0] == venta[1]:
          exist = True
          posnw = i
      if exist: #Si esta agregado sumamos uno y la calificacion
        nwventas[posnw][1] += 1
        nwventas[posnw][2] += venta[2]
      else: #Sino esta agregado lo agregamos
        nwventas += [[venta[1], 1, venta[2]]]
  for i, nwventa in enumerate(nwventas): #Recorremos cada articulo para poder sacar el promedio
    nwventas[i][2] = round(nwventas[i][2]/nwventas[i][1], 2)
  nwventas = sorted(nwventas, key=lambda x: (x[2],x[1]), reverse=orden) #Se ordena por medio del promedio y luego por las ventas
  return nwventas


def filtrar_VenyBusC(ventas, limit = 50, filter='all'):
  """
  Funcion       filtrar_VenyBusC
  Definicion:   Funcion encargada de filtrar los resultados obtenidos, se observa si
                se tiene algun limite o si solo se quieren buscar de cierta categoria.

  Inputs:       ventas(lista):  Coleccion que se tiene que filtrar [ID, cantidad, calificacion]
                limit(int):     Limite de registros a mostrar
                filter(string): Filtro que filtra sobre el tipo de categoria que se esta buscando

  Outputs:      nw(list): Lista que contiene los articulos filtrados [Numero, Nombre, Calificacion, Categoria, Cantidad]
  """
  nwventas = ventas
  i = 1
  nw = []
  for nwventa in nwventas: #Recorrer productos calificados
    prod = searchProd(nwventa[0]) #Buscar producto
    if prod[3] == filter or filter == 'all': #Aplicar filtros
      nw += [[i, prod[1], nwventa[2], prod[3], nwventa[1]]] #Agregar nuevo registro en orden para imprimir
      i += 1
  return nw[0:min(limit, len(nw))]

def categorias_rating(ventas, orden = True, refund = True):
  """
  Funcion       categorias_rating
  Definicion:   Funcion encargada de obtener el rating por categoria

  Inputs:       ventas(lista):  La coleccion en la que se tiene que buscar y ordenar.
                orden(Bool):    Define el orden de mayor a menor (True) o visecersa.
                refund(Bool):   Decide si se tiene que contar los productos devueltos.

  Outputs:      nw(list): Lista que contiene los articulos filtrados [Numero, Categoria, Calificacion, ventas]
  """
  nwventas = [] #Se crea lista vacia 
  posnw = 0
  for venta in ventas: #Recorrer ventas
    if refund or not venta[4]: #ver si se cuentas las devueltas
      exist = False 
      prod = searchProd(venta[1]) #Se busca el producto
      for i, nwventa in enumerate(nwventas): #Se busca si existe en la lista
        if nwventa[0] == prod[3]:
          exist = True
          posnw = i
      if exist: #Si existe se suma
        nwventas[posnw][1] += 1
        nwventas[posnw][2] += venta[2]
      else: #Si no se agrega uno nuevo
        nwventas += [[prod[3], 1, venta[2]]]
  for i, nwventa in enumerate(nwventas): #Se recorre para sacar calificacion de producto
    nwventas[i][2] = round(nwventas[i][2]/nwventas[i][1], 2)
  nwventas = sorted(nwventas, key=lambda x: (x[2],x[1]), reverse=orden) #Se ordenan por calificacion y ventas
  i = 1
  nw = []
  for nwventa in nwventas:
    nw += [[i, nwventa[0], nwventa[2], nwventa[1]]] #Acomodar para imprimir
    i += 1
  return nw

def valorVentas(ventas, filtros): 
    """
    Funcion       valorVentas
    Definicion:   Funcion encargada de obtener datos de ventas en cantidades filtrados por año o mes
    
    Inputs:         ventas(lista):    La coleccion en la que se tiene que buscar y ordenar.
                    filtros(lista):   Decide los filtros por los que se buscara [Fil_mes_activo, mes, filt_anio_activo, ano]
    
    Outputs:      nw(list): Lista que contiene los datos de ventas [subTotal, artDevueltos, #ventas, #devueltos]
    """
    subTotal = 0
    subRef = 0
    vnt = 0
    vntR = 0
    filtM, mes, filtA, ano = filtros
    print(filtros)
    for sale in ventas:
      prod = searchProd(sale[1])
      if (not filtA or sale[3].split('/')[2] == str(ano)) and (not filtM or sale[3].split('/')[1] == str(mes)):
        if sale[4]:
          subRef += prod[2]
          vntR += 1
        subTotal += prod[2]
        vnt += 1
    return [subTotal, subRef, subTotal-subRef, vnt, vntR]

def ventasAgrupadas(ventas, catgA, orden):
    """
    Funcion       ventasAgrupadas
    Definicion:   Funcion encargada de obtener datos de ventas en cantidades agrupadas por mes o día
    
    Inputs:         ventas(lista):    La coleccion en la que se tiene que buscar y ordenar.
                    categA(int):      Se decide si se agrupan por mes o dia.
                    orden(int):       Se decide si se ordena por ventas o meses
    
    Outputs:      nw(list): Lista que contiene los datos de ventas [subTotal, artDevueltos, #ventas, #devueltos]
    """
    categ = []
    for sale in ventas:
      prod = searchProd(sale[1])
      exist = False
      for i, icat in enumerate(categ):
        if sale[3].split('/')[catgA] == icat[0]:
          exist = True
          pos = i
      if exist:
        categ[pos][1] += prod[2]
        categ[pos][2] += 1
        if sale[4]:
          categ[pos][3] += prod[2]
          categ[pos][4] += 1
      else:
        categ += [[sale[3].split('/')[catgA], 0, 0, 0, 0]]
    categ = sorted(categ, key=lambda x: x[orden])
    return categ
    
