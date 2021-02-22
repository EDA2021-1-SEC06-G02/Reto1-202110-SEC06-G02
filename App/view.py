﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1")
    print("3- Requerimiento 2")
    print("4- Requerimiento 3")
    print("5- Requerimiento 4")

catalog = {}

def initCatalog (estructuraDeDatos):
    return controller.initCatalog(estructuraDeDatos)

def loadData(catalog):
    controller.loadData(catalog)

def printResultVideosByViews(listaOrdenada):
    size = lt.size(listaOrdenada)
    print("Los primeros ", size, " videos ordenados por visitas son:")
    i=1
    while i<= size:
        video = lt.getElement(listaOrdenada,i)
        print(i,'- Titulo: '+ video['title'] + '. Visitas del Video: ' + video['views'] + '. Nombre del Canal: ' + video['channel_title']+'.')
        i+=1


"""
Menu principal
"""
while True:
    printMenu()
    inputs = int(input('Seleccione una opción para continuar\n'))
    if inputs == 1:
        verifica=True
        while verifica:
            print("Cuál estructura de datos quiere utilizar?")
            print("1- ArrayList")
            print("2- Single Linked")
            estructuraDeDatos=int(input("Ingrese su selección:\t"))
            if estructuraDeDatos==1 or estructuraDeDatos==2:
                verifica=False
            else:
                print("Opción invalida, elija una opción válida")
        print("Cargando información de los archivos ....")
        t1 = time.process_time_ns()
        catalog = initCatalog(estructuraDeDatos)
        loadData(catalog)
        t2 = time.process_time_ns()
        print ("Tiempo de ejecucion: {:.2f} nano seconds.".format(t2-t1))
        print('Videos cargados exitósamente: ' + str(lt.size(catalog['video'])))
        print('Categorias cargadas exitósamente: ' + str(lt.size(catalog['category'])))

    elif inputs == 2:
        if len(catalog)==0:
            print("No se han cargado datos al catálogo, por favor realize la opción 1 antes de proseguir.")
        else:
            numeroElementos= int(input("¿Cuantos elementos quiere comparar?:\t"))
            if numeroElementos>lt.size(catalog['video']):
                print("Está tratando de comparar más elementos de los que cuenta el catálogo de videos. El máximo de videos que se pueden comprar son: ",lt.size(catalog['video']))
            else:
                verifica=True
                while verifica:
                    print("¿Qué tipo de algoritmo de ordenamiento desea utilizar?")
                    print("1- Selection")
                    print("2- Insertion")
                    print("3- Shell")
                    algoritmo=int(input("Ingrese su selección:\t"))
                    if algoritmo>=1 or algoritmo<=3:
                        verifica=False
                    else:
                        print("Opción invalida, elija una opción válida")
                tiempo,listaOrdenada = controller.VideosByViews(catalog,numeroElementos, algoritmo)
                printResultVideosByViews(listaOrdenada)
                print("El tiempo de ejecución del ordenamiento es: ",tiempo)

    elif inputs == 3:
        if len(catalog)==0:
            print("No se han cargado datos al catálogo, por favor realize la opción 1 antes de proseguir.")
        else:
            pass

    elif inputs == 4:
        if len(catalog)==0:
            print("No se han cargado datos al catálogo, por favor realize la opción 1 antes de proseguir.")
        else:
            pass

    else:
        sys.exit(0)
sys.exit(0)
