from collections import namedtuple
import datetime
import csv
import os
import sys

articulo_list = []
venta_list = {}
csv_list ={}
new_articuloList = []

Salida1 = int(0) 
while Salida1 == int(0):
    venta_Info = namedtuple("Venta","Fecha_V,Desc_V,Cant_V,Precio_V")
    csv_Info = namedtuple("Datos","Folio_csv,Fecha_csv,Desc_csv,Cant_csv,Precio_csv")
    
    try:
        with open ("Ventas.csv", "r", newline="") as documento:
            leer = csv.reader(documento)
            next(leer)
            cont = 0
            for folio, fecha, desc, cant, pu in leer:
                cont +=1
                csv_list[cont] = csv_Info(folio, fecha, desc, cant, pu) 
    except FileNotFoundError:
        print()
        print(f'{"/"*25}ADVERTENCIA LEER ANTES DE CONTINUAR{"/"*25}')
        print(f'1.OMITIR ESTE MENSAJE SI ES LA PRIMERA VEZ QUE SE REGISTRA UNA VENTA')
        print(f'2.DE YA HABER REGISTRADO VENTAS SE LE INFORMA QUE EL PROGRAMA NO ENCONTRO')
        print(f'LOS DATOS DEL REGISTRO PORFAVOR VERIFICAR QUE EL ARCHIVO SE ENCUENTRE EN LA')
        print(f'CARPETA {os.getcwd()}')
        print(f'Y CIERRE EL PROGRAMA PORQUE SI REGISTRA UNA VENTA SE CREARA UN NUEVO ARCHIVO')
    except Exception:
        print(f'{"/"*25}ADVERTENCIA LEER ANTES DE CONTINUAR{"/"*25}')
        print(f'SE DETECTO UN PROBLEMA {sys.exc_info()[0]}')
        print(f'FAVOR DE CERRAR EL PROGRAMA Y REPORTAR')
    print(f'\n{"*"*50}')
    
    llaveAsignada = 1
    contador = 0
    elementosIN_csvList = len(csv_list)
    for ventas, datos in csv_list.items():
        contador +=1 
        numApoyo = int(datos[0])
        if llaveAsignada == numApoyo:
            Data_V = venta_Info(datos.Fecha_csv, datos.Desc_csv, datos.Cant_csv, datos.Precio_csv)
            new_articuloList.append(Data_V)
            if contador == elementosIN_csvList:
                new_articuloList2 = new_articuloList.copy()
                venta_list[llaveAsignada] = new_articuloList2
                del(new_articuloList[:])
                
        else:
            new_articuloList2 = new_articuloList.copy()
            venta_list[llaveAsignada] = new_articuloList2
            del(new_articuloList[:])
            llaveAsignada +=1
            Data_V = venta_Info(datos.Fecha_csv, datos.Desc_csv, datos.Cant_csv, datos.Precio_csv)
            new_articuloList.append(Data_V)
            if contador == elementosIN_csvList:
                new_articuloList2 = new_articuloList.copy()
                venta_list[llaveAsignada] = new_articuloList2
                del(new_articuloList[:])  
            
   

    print(f'\nBASE DE DATOS "LLANTAS DON ELIAZAR"')
    print(f'1.REGISTRAR UNA VENTA')
    print(f'2.CONSULTAR UNA VENTA')
    print(f'3.OBTENER UN REPORTE DE VENTAS PARA UNA FECHA ESPECIFICA')
    print(f'4.SALIR')
    op = input("OPCIÓN:")
    
    print()

    if op == "1":
        Folio = int()
        print("DIGITE EL NUMERO DE FOLIO DE VENTA")
        print("SI DIGITA UN FOLIO YA EXISTENTE NO SE REGISTRARA")
        print("EL SISTEMA MARCARA ERROR Y VOLVERA AL MENU")
        num_Folio = int(input("FOLIO: "))
        
        print()

        if num_Folio in venta_list.keys():
            print(f'{"*"*20}ADVERTENCIA{"*"*20}')
            print(f'\n{"¡"*10}FOLIO YA EXISTENTE{"!"*10}\n')
            
        else:
            Folio = num_Folio
            Salida2 = int(0)
            contCSV = len(csv_list)

            while Salida2 == int(0):
                contCSV = len(csv_list)
                print("AGREGAR ARTICULO")
                fecha_venta = str(datetime.date.today())
                desc_Articulo = str(input("DESCRIPCIÓN DEL ARTICULO: "))
                cantidad_Articulo = float(input("CANTIDAD: "))
                precio = float(input("PRECIO DEL ARTICULO: "))
                
                datos_Venta = venta_Info(fecha_venta, desc_Articulo,cantidad_Articulo,precio)
                articulo_list.append(datos_Venta)
                datos_csv = csv_Info(Folio, fecha_venta, desc_Articulo, cantidad_Articulo, precio)
                csv_list[contCSV+1] = datos_csv

                with open("Ventas.csv","w", newline="") as documento:
                    grabado = csv.writer(documento)
                    grabado.writerow(("Folio","Fecha","Descripción","Cantidad","PU"))
                    grabado.writerows([(info.Folio_csv, info.Fecha_csv, info.Desc_csv, info.Cant_csv, info.Precio_csv)for folio, info in csv_list.items()])

                print(f'\nDESEA AGREGAR OTRO ARTICULO SI[0], NO[1]')
                exit = int(input("OPCIÓN: "))
                Salida2 = exit
                
                print()      

            articulo_list2 = articulo_list.copy()
            venta_list[num_Folio] = articulo_list2
            del(articulo_list[:])
            
            print(f'\n***VENTA REGISTRADA CON EXITO***\n')

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
                    importe = float(elemento.Cant_V) * float(elemento.Precio_V)
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
            if op == "3":
                print(f'\n***INGRESE UNA FECHA PARA IMPRIMIR TODAS LAS VENTAS DE ESA FECHA***')
                print(f'¡PORFAVOR DIGITE LA FECHA EN EL SIGUIENTE FORMATO! (AÑO-MES-DÍA)')
                print(f'EJEMPLO:2008-07-23')
                fec = input("FECHA: ")
                pointSave = 0
                csv_data = len(csv_list)
                print(f'\n{"*"*50}')
                print(f'Folio, Fecha, Descripción, Cantidad, PU')
                for venta, datos in csv_list.items():
                    if datos[1] == fec:
                        print(f'{datos[0]}, {datos[1]}, {datos[2]}, {datos[3]}, {datos[4]}')
                    else:
                        pointSave +=1
                        if pointSave == csv_data:
                            print(f'{"*"*50}')  
                            print(f'\nNINGUNA VENTA ENCONTRADA CON ESA FECHA\n')
                            print(f'FAVOR DE VERIFICAR QUE: {fec} ESTE CORRECTO')                    
            else:
                if op == "4":
                    Salida1 = int(1)