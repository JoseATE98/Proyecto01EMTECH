#importar librerias
from lifestore_file import lifestore_sales, lifestore_searches, lifestore_products
from functions import * 
import os
from tabulate import tabulate

print("lifestore_sales")
print("Tipo de variable: ", type(lifestore_sales))
print("Contenido: ", type(lifestore_sales[0][0]), type(lifestore_sales[0][1]), type(lifestore_sales[0][2]), type(lifestore_sales[0][3]), type(lifestore_sales[0][4]))
print("lifestore_searches")
print("Tipo de variable: ", type(lifestore_searches))
print("Contenido: ", type(lifestore_searches[0][0]), type(lifestore_searches[0][1]))
print("lifestore_products")
print("Tipo de variable: ", type(lifestore_products))
print("Contenido: ", type(lifestore_products[0][0]), type(lifestore_products[0][1]), type(lifestore_products[0][2]), type(lifestore_products[0][3]), type(lifestore_products[0][4]))
lifestore_products

def loginF():
  print("Bienvenido al sistema de análisis de datos de LifeStore.")
  print("Tienes que hacer login para poder acceder. Por favor, ingresa tus datos.")
  user = input("Usuario: ")
  passw = input("Contraseña: ")
  if user == 'admin':
    if passw == '123abc':
      print("Bienvenido al sistema Admin")
      return True
    else:
      print("Contraseña incorrecta")
      return False
  else:
    print("Usuario o contraseña incorrectas")
    return False

def estVen():
    print("Menu de ventas, elige la opción que desees consultar: ")
    print("1.- Consultar estadisticas de productos en ventas")
    print("2.- Consultar estadisticas de busquedas")
    print("3.- Consultar estadisticas de categorias en ventas")
    print("4.- Consultar estadisticas de categorias busquedas")
    print("5.- Salir")
    op = '6'
    while(not op in ['1','2','3','4','5']):
        op = input("Seleccione una opción: ")
        if not op in ['1','2','3','4','5']:
            print("Opcion incorrecta. Selecciona una opción adecuada.")
    if op == '5':
        return False        
    if op == '1':
        ban = True
        while(ban):
            orden = input('Teclea si deseas, Ordenar de mayor a menor(DES), menor a mayor (ASC): ')
            if orden != 'DES' and orden != 'ASC':
                print("Solo puedes teclear DES o ASC. Intenta de nuevo.")
            else:
                ban = False
        orden = True if orden == 'DES' else False
        ban = True
        while(ban):
            refun = input('Teclea si deseas tomar en cuenta las devoluciones (Y/N): ')
            if refun != 'Y' and refun != 'N':
                print("Solo puedes teclear Y o N. Intenta de nuevo.")
            else:
                ban = False
        refun = True if refun == 'Y' else False
        lim = int(input("Escribe el numero limite de resultados que deseas obtener: "))
        filt = input("Escribe la categoria que desees filtrar, sino deseas ninguna escribe 'all': ")
        print("El resultado de tu consulta es el siguiente: ")
        res = filtrar_VenyBus(productos_VenyBus(lifestore_sales, orden, refun),lim, filt)
        encabezado = ['#','Nombre', 'Ventas', 'Categoria']
        print(tabulate(res, headers=encabezado))
        print('\n')
    if op == '2':
        ban = True
        while(ban):
            orden = input('Teclea si deseas, Ordenar de mayor a menor(DES), menor a mayor (ASC): ')
            if orden != 'DES' and orden != 'ASC':
                print("Solo puedes teclear DES o ASC. Intenta de nuevo.")
            else:
                ban = False
        orden = True if orden == 'DES' else False
        lim = int(input("Escribe el numero limite de resultados que deseas obtener: "))
        filt = input("Escribe la categoria que desees filtrar, sino deseas ninguna escribe 'all': ")
        print("El resultado de tu consulta es el siguiente: ")
        res = filtrar_VenyBus(productos_VenyBus(lifestore_searches, orden),lim, filt)
        encabezado = ['#','Nombre', 'Ventas', 'Categoria']
        print(tabulate(res, headers=encabezado))
        print('\n')
    if op == '3':
        ban = True
        while(ban):
            orden = input('Teclea si deseas, Ordenar de mayor a menor(DES), menor a mayor (ASC): ')
            if orden != 'DES' and orden != 'ASC':
                print("Solo puedes teclear DES o ASC. Intenta de nuevo.")
            else:
                ban = False
        orden = True if orden == 'DES' else False
        ban = True
        while(ban):
            refun = input('Teclea si deseas tomar en cuenta las devoluciones (Y/N): ')
            if refun != 'Y' and refun != 'N':
                print("Solo puedes teclear Y o N. Intenta de nuevo.")
            else:
                ban = False
        refun = True if refun == 'Y' else False
        print("El resultado de tu consulta es el siguiente: ")
        res = categorias_VenyBus(lifestore_sales, orden, refun)
        encabezado = ['#','Categoria', 'Ventas']
        print(tabulate(res, headers=encabezado))
        print('\n')
    if op == '4':
        ban = True
        while(ban):
            orden = input('Teclea si deseas, Ordenar de mayor a menor(DES), menor a mayor (ASC): ')
            if orden != 'DES' and orden != 'ASC':
                print("Solo puedes teclear DES o ASC. Intenta de nuevo.")
            else:
                ban = False
        orden = True if orden == 'DES' else False
        ban = True
        print("El resultado de tu consulta es el siguiente: ")
        res = categorias_VenyBus(lifestore_searches, orden)
        encabezado = ['#','Categoria', 'Ventas']
        print(tabulate(res, headers=encabezado))
        print('\n')
    return True
    
def estCal():
    print("Menu de Calificaciones, elige la opción que desees consultar: ")
    print("1.- Consultar estadisticas de productos por calificacion")
    print("2.- Consultar estadisticas de categorias por calificacion")
    print("3.- Salir")
    op = '4'
    while(not op in ['1','2','3']):
        op = input("Seleccione una opción: ")
        if not op in ['1','2','3']:
            print("Opcion incorrecta. Selecciona una opción adecuada.")
    if op == '3':
        return False
    if op == '1':
        ban = True
        while(ban):
            orden = input('Teclea si deseas, Ordenar de mayor a menor(DES), menor a mayor (ASC): ')
            if orden != 'DES' and orden != 'ASC':
                print("Solo puedes teclear DES o ASC. Intenta de nuevo.")
            else:
                ban = False
        orden = True if orden == 'DES' else False
        ban = True
        while(ban):
            refun = input('Teclea si deseas tomar en cuenta las devoluciones (Y/N): ')
            if refun != 'Y' and refun != 'N':
                print("Solo puedes teclear Y o N. Intenta de nuevo.")
            else:
                ban = False
        refun = True if refun == 'Y' else False
        lim = int(input("Escribe el numero limite de resultados que deseas obtener: "))
        filt = input("Escribe la categoria que desees filtrar, sino deseas ninguna escribe 'all': ")
        print("El resultado de tu consulta es el siguiente: ")
        res = filtrar_VenyBusC(productos_rating(lifestore_sales, orden, refun),lim, filt)
        encabezado = ['#','Nombre', 'Calificación', 'Categoria', 'Ventas']
        print(tabulate(res, headers=encabezado))
        print('\n')
    if op == '2':
        ban = True
        while(ban):
            orden = input('Teclea si deseas, Ordenar de mayor a menor(DES), menor a mayor (ASC): ')
            if orden != 'DES' and orden != 'ASC':
                print("Solo puedes teclear DES o ASC. Intenta de nuevo.")
            else:
                ban = False
        orden = True if orden == 'DES' else False
        ban = True
        while(ban):
            refun = input('Teclea si deseas tomar en cuenta las devoluciones (Y/N): ')
            if refun != 'Y' and refun != 'N':
                print("Solo puedes teclear Y o N. Intenta de nuevo.")
            else:
                ban = False
        refun = True if refun == 'Y' else False
        print("El resultado de tu consulta es el siguiente: ")
        res = categorias_rating(lifestore_sales, orden, refun)
        encabezado = ['#','Categoria', 'Calificacion', 'Ventas']
        print(tabulate(res, headers=encabezado))
        print('\n')
    return True

def estFin():
    print("Menu de Finanzas, elige la opción que desees consultar: ")
    print("1.- Consultar numeros de ventas")
    print("2.- Consultar numeros de ventas agrupados")
    print("3.- Salir")
    op = '4'
    while(not op in ['1','2','3']):
        op = input("Seleccione una opción: ")
        if not op in ['1','2','3']:
            print("Opcion incorrecta. Selecciona una opción adecuada.")
    if op == '3':
        return False
    if op == '1':
        mes, ano = 0, 0
        ban = True
        while(ban):
            filtM = input('Selecciona si deseas filtras por mes (Y/N): ')
            if filtM != 'Y' and filtM != 'N':
                print("Solo puedes teclear Y o N. Intenta de nuevo.")
            else:
                ban = False
        filtM = True if filtM == 'Y' else False
        if filtM:
            mes = input("Selecciona un mes del 01 al 12: ")
        ban = True
        while(ban):
            filtA = input('Selecciona si deseas filtras por año (Y/N): ')
            if filtA != 'Y' and filtA != 'N':
                print("Solo puedes teclear Y o N. Intenta de nuevo.")
            else:
                ban = False
        filtA = True if filtA == 'Y' else False
        if filtA:
            ano = input("Selecciona un año para filtrar: ")
        res = valorVentas(lifestore_sales,[filtM, mes, filtA, ano])
        print("Informe de ventas")
        if filtA:
            print("Ventas filtradas en el año: ", ano)
        if filtM:
            print("Ventas filtradas en el mes: ", mes)
        print("SubTotal de ventas: $", res[0])
        print("Devoluciones: $", res[1])
        print("Numero de productos vendidos: #", res[3])
        print("Numero de productos decueltos: #", res[4])
        print("Numero de productos totales: #", res[3] - res[4])
        print("Ventas totales: $", res[2])
    if op == '2':
        ban = True
        while(ban):
            filtM = input('Selecciona si deseas filtras por mes(M) o dia(D): ')
            if filtM != 'M' and filtM != 'D':
                print("Solo puedes teclear M o D. Intenta de nuevo.")
            else:
                ban = False
        filtM = 0 if filtM == 'D' else 1
        ban = True
        while(ban):
            filtA = input('Selecciona si ordendar por fecha(F) o ventas(V): ')
            if filtA != 'F' and filtA != 'V':
                print("Solo puedes teclear F o V. Intenta de nuevo.")
            else:
                ban = False
        filtA = 0 if filtA == 'F' else 1
        res = ventasAgrupadas(lifestore_sales, filtM, filtA)
        print("Informe de ventas")
        encabezado = ['Fecha', 'Subtotal', 'Devuelto', 'Total', '#Ventas', '#Devuelto']
        print(tabulate(res, headers=encabezado))
        print('\n')
    return True

def menuP():
    print("Bienvenido al sistema, por favor selecciona una opcion de las siguientes: ")
    print("1.- Estadisticas de Ventas")
    print("2.- Estadisticas de calificaciones")
    print("3.- Estadisticas financieras")
    print("4.- Salir")
    op = '5'
    while(not op in ['1','2','3','4']):
        op = input("Seleccione una opción: ")
        if not op in ['1','2','3','4']:
            print("Opcion incorrecta. Selecciona una opción adecuada.")
    if op == '4':
        return 0
    elif op == '1':
        menVen = True
        while(menVen):
            menVen = estVen()
    elif op == '2':
        menCal = True
        while(menCal):
            menCal = estCal()
    elif op == '3':
        menFin = True
        while(menFin):
            menFin = estFin()
        

def main():
    retries = 3
    login = False
    while(not login and retries > 0):
        login = loginF()
        if not login:
            print("Vuelve a intentar")
        retries -= 1
        os.system("cls") 
    if not login:
        print("Excediste los intentos, vuelve a intentarlo despues")
    else:
        menuPR = 1
        while(menuPR != 0):
            menuPR = menuP()
        print("Gracias por consultar LifeStore")
            
main()
