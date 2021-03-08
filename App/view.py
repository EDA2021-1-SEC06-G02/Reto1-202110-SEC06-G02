"""
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

#default_limit = 1000
#sys.setrecursionlimit(default_limit*10)

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
    print("Escriba cualquier otro número para detener la ejecución del programa")

catalog = {}
cataOrdenPaises = {}

def initCatalog ():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

def printResultVideosByViews(listaOrdenada, sample=10):
    size = lt.size(listaOrdenada)
    if size > sample:
        print("Los primeros ", size, " videos ordenados por visitas son:")        
        i=1
        while i<= sample:
            video = lt.getElement(listaOrdenada,i)
            print(i,'- Titulo: '+ video['title'] + '. Visitas del Video: ' + video['views'] + '. Nombre del Canal: ' + video['channel_title']+'.')
            i+=1

def printResultVideosPais(listaOrdenada, sample=10):
    size = lt.size(listaOrdenada)
    if size > sample:
        print("Los primeros ", size, " videos ordenados por visitas son:")        
        i=1
        while i<= sample:
            video = lt.getElement(listaOrdenada,i)
            print(i,'- Titulo: '+ video['title'] + '. Pais del Video: ' + video['country'] + '. Nombre del Canal: ' + video['channel_title']+'.')
            i+=1

def VideoPaisConMasTendencia(catalog,paisInteres):
    return controller.VideoPaisConMasTendencia(catalog,paisInteres)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = int(input('Seleccione una opción para continuar\n'))
    if inputs == 1:
        print("Cargando información de los archivos ....")
        t1 = time.process_time()
        catalog = initCatalog()
        loadData(catalog)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")
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
                tiempo,listaOrdenada = controller.VideosByViews(catalog,numeroElementos)
                printResultVideosByViews(listaOrdenada)
                print("El tiempo de ejecución del ordenamiento es: ",tiempo)

    elif inputs == 3:
        if len(catalog)==0:
            print("No se han cargado datos al catálogo, por favor realize la opción 1 antes de proseguir.")
        else:
            if len(cataOrdenPaises)==0:
                print("Estamos ordenando la lista por orden de paises esto puede tardar unos cuantos segundos")
                tiempoO,cataOrdenPaises=controller.OrdenCatalogoPaises(catalog)
                print("El tiempo de ejecución del ordenamiento es: ",tiempoO)
            start_time = time.process_time()
            paisInteres = input("Ingrese el nombre del país del cual quiere conocer el video que más días a sido tendencia:\t")
            result,DiasEnTendencia=VideoPaisConMasTendencia(cataOrdenPaises,paisInteres)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)*1000
            if result==-1:
                print("El país ingresado no se encuentra en el arreglo, intente con otro país.")
            else:
                print("El título del video es: ",result['title'],"; el nombre del canal es: ",result['channel_title'],"; el país en el que es tendencia: ",result['country']," sus días siendo tendencia son: ",DiasEnTendencia)
            print("El tiempo de ejecución de la consulta es: ",elapsed_time_mseg)

    elif inputs == 4:
        if len(catalog)==0:
            print("No se han cargado datos al catálogo, por favor realize la opción 1 antes de proseguir.")
        else:
            pass
    
    elif inputs == 5:
        if len(catalog)==0:
            print("No se han cargado datos al catálogo, por favor realize la opción 1 antes de proseguir.")
        else:
            pass

    else:
        sys.exit(0)
sys.exit(0)