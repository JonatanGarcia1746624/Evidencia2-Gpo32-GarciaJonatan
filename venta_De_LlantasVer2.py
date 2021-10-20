#IMPORTACIONES DE LAS LIBRERIAS A UTILIZAR
from collections import namedtuple
import datetime
import time

#CREACIÓN DE UNA LISTA Y UN DICCIONARIO QUE SE UTILIZARA 
#POSTERIORMENTE PARA TRABAJAR CON LAS TUPLAS ANIDADAS
articulo_list = []
venta_list = {}

Salida1 = int(0)
while Salida1 == int(0):
    #SUBCLASE DE LISTA CON LOS CAMPOS CORRESPONDIENTES PARA SU
    #POSTERIOR USO AL REGISTRAR LAS VENTAS
    venta_Info = namedtuple("Venta","Fecha_V,Desc_V,Cant_V,Precio_V")

    #UN MENU SENCILLO QUE NOS SERVIRA PARA QUE EL USUARIO 
    #SELECCIONE LA ACCIÓN A REALIZAR
    print(f'\nBASE DE DATOS "LLANTAS DON ELIAZAR"')
    print(f'1.REGISTRAR UNA VENTA')
    print(f'2.CONSULTAR UNA VENTA')
    print(f'3.SALIR')
    op = input("OPCIÓN:")
    
    print()

    if op == "1":
        #CREACION DE UN NUMERO DE FOLIO UNICO AQUI EL USUARIO
        #DEBERA DIGITAR UN NUMERO Y POSTERIORMENTE EL PROGRAMA
        #LE AVISARA SI EL NUMERO DE FOLIO YA EXISTE
        Folio = int()
        print("DIGITE EL NUMERO DE FOLIO DE VENTA")
        print("SI DIGITA UN FOLIO YA EXISTENTE NO SE REGISTRARA")
        print("EL SISTEMA MARCARA ERROR Y VOLVERA AL MENU")
        num_Folio = int(input("FOLIO: "))
        print()

        if num_Folio in venta_list.keys():
            print("¡¡¡FOLIO YA EXISTENTE!!!\n")
        else:
            Folio = num_Folio
            Salida2 = int(0)
            
            while Salida2 == int(0):
                #AQUI ES DONDE OCURRE LA MAGIA PUES COMO SE VIO ANTES
                #SE HARA USO DE LAS LISTAS ANIDADAS Y SE GUARDARAN
                #LOS DATOS RECIBIDOS CON UN FORMATO EN EL CUAL CADA
                #DATO CONTENGA SU ESPACIO CORRESPONDIENTE
                print("AGREGAR ARTICULO")
                fecha_venta = str(datetime.date.today())
                desc_Articulo = str(input("DESCRIPCIÓN DEL ARTICULO: "))
                cantidad_Articulo = float(input("CANTIDAD: "))
                precio = float(input("PRECIO DEL ARTICULO: "))
                datos_Venta = venta_Info(fecha_venta, desc_Articulo,cantidad_Articulo,precio)
                articulo_list.append(datos_Venta)
                #AQUI SE LE PREGUNTA AL USUARIO SI DESEA AGREGAR OTRO ARTICULO
                #DE SER ASÍ EL CILCO SE REPITE PERO EN CAMBIO SI NO ES ASÍ
                #EL CODIGO CONTINUARA SALIENDO DE UN WHILE EN EL QUE ESTA 
                #AHORA QUE EL USUARIO ESTA FUERA DEK WHILE LO QUE SIGUE ES
                #ESTA PARTE ES IMPORTANTE YA QUE AQUI LO QUE HACE EL PROGRAMA
                #ES GUARDAR TODOS LOS DATOS EN UNA LISTA Y LUEGO LES HACE UNA
                #COPIA QUE SE REGISTRARA EN EL DICCIONARIO CON SU FOLIO UNICO
                print(f'\nDESEA AGREGAR OTRO ARTICULO SI[0], NO[1]')
                exit = int(input("OPCIÓN: "))
                Salida2 = exit
                print()
            articulo_list2 = articulo_list.copy()
            venta_list[num_Folio] = articulo_list2
            #PARA QUE LOS DATOS NO SE QUEDEN GUARDADOS EN LA LISTA ANTERIOR
            #AQUI LO QUE SE HACE ES USAR LA FUNCIÓN "DEL" QUE BORRA MEDIANTE
            #NOTACIÓN DE SLICING TODOS LOS DATOS DE LA LISTA PARA DEJARLA
            #VACIA PARA SU POSTERIOR USO Y SE CONFIRMA EL REGISTRO DE VENTA
            del(articulo_list[:])
            print(f'\n***VENTA REGISTRADA CON EXITO***\n')
            #AQUI SE GUARDA LA POSICION DEL ANTERIOR REGISTRO PARA
            #DESPUES IMPRIMIR EL TICKET DE VENTA EL CUAL SE IMPRIME
            #MEDIANTE LOS METODOS ANTERIORES QUE TENIAMOS CON SU
            #RESPECTIVO NOMBRE Y SE HACEN LAS RESPECTIVAS OPERACIONES
            #PARA SACAR SL SUBTOTAL, IVA Y EL TOTAL
            pos = venta_list[num_Folio]
            print(f'FECHA DE VENTA: {fecha_venta}')
            subtotal = int(0)
            for elemento in pos:
                importe = elemento.Cant_V * elemento.Precio_V
                print(f'DESCRIPCIÓN ARTICULO: {elemento.Desc_V}')
                print(f'CANTIDAD: {elemento.Cant_V}')
                print(f'PRECIO UNITARIO: {elemento.Precio_V}')
                print(f'IMPORTE: {importe}')
                subtotal += importe
                print()
            print(f'SUBTOTAL: {subtotal}')
            print(f'IVA(16%): {subtotal * 0.16}')
            print(f'TOTAL: {(subtotal) + (subtotal * 0.16)}')
            Salida1 = int(0)
    else:
        #AHORA QUE SI EL USUARIO ESCOGIO CONSULTAR UN REGISTRO 
        #LO QUE SE HACE ES QUE MEDIANTE EL FOLIO QUE AQUI FUNCIONA
        #COMO UNA LLAVE DEL DICCIONARIO BUSCA EL REGISTRO EN CASO
        #DE EXISTIR E IMPRIME LOS DATOS USANDO EL MISMO METODO QUE
        #SE USO ANTERIORMENTE Y EN CASO DE NO ENCONTRAR EL FOLIO
        #EL PROGRAMA LE AVISA AL USUARIO Y REGRESA AL MENU
        if op == "2":
            print(f'\nCONSULTAR UNA VENTA')
            print(f'INGRESE EL FOLIO DE LA VENTA QUE DESEA CONSULTAR')
            num_Venta = int(input("Numero de Folio: "))
            if num_Venta in venta_list.keys():
                pos = venta_list[num_Venta]
                print("\n***FOLIO ENCONTRADO***\n")
                print(f'FECHA: {pos[0].Fecha_V}')
                subtotal = int(0)
                for elemento in pos:
                    importe = elemento.Cant_V * elemento.Precio_V
                    print(f'DESCRIPCIÓN ARTICULO: {elemento.Desc_V}')
                    print(f'CANTIDAD: {elemento.Cant_V}')
                    print(f'PRECIO UNITARIO: {elemento.Precio_V}')
                    print(f'IMPORTE: {importe}')
                    subtotal += importe
                    print()
                print(f'SUBTOTAL: {subtotal}')
                print(f'IVA(16%): {subtotal * 0.16}')
                print(f'TOTAL: {(subtotal) + (subtotal * 0.16)}')
            else:
                print("\n¡¡¡FOLIO NO ENCONTRADO!!!")
        else:
            #EN ESTA OPCIÓN LO UNICO QUE PASA ES QUE EL PROGRAMA FINALIZA
            if op == "3":
                Salida1 = int(1)