﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as She
from DISClib.Algorithms.Sorting import selectionsort as Sel
from DISClib.Algorithms.Sorting import insertionsort as Inser
from DISClib.Algorithms.Sorting import mergesort as Merge
from DISClib.Algorithms.Sorting import quicksort as Quick
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'video': None, 'category': None}
    catalog['video'] = lt.newList('ARRAY_LIST',cmpfunction=cmpVideosByViews)
    catalog['category'] = lt.newList('ARRAY_LIST')#, cmpfunction=compareCategories
    return catalog

def addVideo(catalog, video):
    lt.addLast(catalog['video'], video)

def addCategory(catalog, category):
    cat = newCategory(category['id'], category['name'])
    lt.addLast(catalog['category'], cat)

def newCategory(id, name):
    Category = {'Category_id': '', 'name': ''}
    Category['Category_id'] = id
    Category['name'] = name.strip()
    return Category


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

def busquedaBinariaPaises(listaOrdenada, elemento):
    i, lon = 1, lt.size(listaOrdenada)
    elemento=elemento.lower()
    while i <= lon:
        m = (i + lon) // 2
        EM = lt.getElement(listaOrdenada,m)['country'].lower()
        if EM == elemento:
            return m
        elif elemento < EM:
            lon = m - 1
        else:
            i = m + 1
    return -1

def busquedaBinariaID(listaOrdenada, elemento):
    i, lon = 1, lt.size(listaOrdenada)
    elemento=elemento.lower()
    while i <= lon:
        m = (i + lon) // 2
        EM = lt.getElement(listaOrdenada,m)['video_id'].lower()
        if EM == elemento:
            return m
        elif elemento < EM:
            lon = m - 1
        else:
            i = m + 1
    return -1

def busquedaBinariaCategoryID(listaOrdenada, elemento):
    i, lon = 1, lt.size(listaOrdenada)
    while i <= lon:
        m = (i + lon) // 2
        EM = lt.getElement(listaOrdenada,m)['category_id']
        if EM == elemento:
            return m
        elif elemento < EM:
            lon = m - 1
        else:
            i = m + 1
    return -1

def busquedaBinariaCategory_Name(listaOrdenada, elemento):
    elemento=elemento.lower()
    i, lon = 1, lt.size(listaOrdenada)
    while i <= lon:
        m = (i + lon) // 2
        EM = lt.getElement(listaOrdenada,m)['name'].lower()
        if EM == elemento:
            return m
        elif elemento < EM:
            lon = m - 1
        else:
            i = m + 1
    return -1

def asignarNombreCategoryToID(catalog,elemento):
    categoryName=CategoryByName(catalog)
    index=busquedaBinariaCategory_Name(categoryName,elemento)
    if (index==-1):
        return index
    category_id=lt.getElement(categoryName,index)['Category_id']
    return category_id

def VideoPaisConMasTendencia(listaOrdenada,paisInteres):
    indexProvi=busquedaBinariaPaises(listaOrdenada,paisInteres)
    if(indexProvi==-1):
        return -1,0
    else:
        listaSoloPaises=subListaDePais(listaOrdenada,indexProvi,paisInteres)
        listaOrdenID=VideoConMasTendencia(listaSoloPaises)
        videoTendenciaID,DiasEnTendencia=VideoConMasDiasEnTendencia(listaOrdenID)
        videoTendencia=lt.getElement(listaOrdenID,busquedaBinariaID(listaOrdenID,videoTendenciaID))
        return videoTendencia,DiasEnTendencia

def VideoConMasDiasEnTendencia(listaOrdenID):
    contador=0
    Mayor=0
    MayorID=''
    i=0
    elementoComparado=lt.getElement(listaOrdenID,i)['video_id'].lower()
    while i<=lt.size(listaOrdenID):
        if elementoComparado==lt.getElement(listaOrdenID,i)['video_id'].lower():
            contador+=1
        else:
            if contador>Mayor:
                Mayor=contador
                MayorID=elementoComparado
            elementoComparado=lt.getElement(listaOrdenID,i)['video_id'].lower()
            contador=1
        i+=1
    return MayorID,Mayor

def VideoConMasTendencia(listaOrdenada):
    return VideosByID(listaOrdenada)

def VideosConMasViewsPorPais(listaOrdenada,paisInteres,idCategoria):
    indexProvi=busquedaBinariaPaises(listaOrdenada,paisInteres)
    if(indexProvi==-1):
        return -1
    else:
        listaSoloPaises=subListaDePais(listaOrdenada,indexProvi,paisInteres)
        listaOrdenadaCategoria=VideosByCategoryID(listaSoloPaises)
        indexCategory=busquedaBinariaCategoryID(listaOrdenadaCategoria,idCategoria)
        listaSoloCategoria=subListaDeCategories(listaOrdenadaCategoria,indexCategory,idCategoria)
        listaPaisViews=VideosByViews(listaSoloCategoria)
    return listaPaisViews

def subListaDePais(listaOrdenada,index,elemento):
    elemento=elemento.lower()
    i=index-1
    l=index+1
    limIzq=0
    limDer=lt.size(listaOrdenada)
    VerIzq=True
    VerDer=True
    while i >= 0 and VerIzq:
        if not(lt.getElement(listaOrdenada,i)['country'].lower()==elemento):
            VerIzq=False
            if i==0:
                limIzq=i
            else:
                limIzq=i+1
        i-=1
    while l <= lt.size(listaOrdenada) and VerDer:
        if not(lt.getElement(listaOrdenada,l)['country'].lower()==elemento):
            VerDer=False
            if l==lt.size(listaOrdenada):
                limDer=l
            else:
                limDer=l-1
        l+=1
    sub_list = lt.subList(listaOrdenada, limIzq, limDer-limIzq)
    sub_list = sub_list.copy()
    return sub_list

def subListaDeCategories(listaOrdenada,index,elemento):
    i=index-1
    l=index+1
    limIzq=0
    limDer=lt.size(listaOrdenada)
    VerIzq=True
    VerDer=True
    while i >= 0 and VerIzq:
        if not(lt.getElement(listaOrdenada,i)['category_id']==elemento):
            VerIzq=False
            if i==0:
                limIzq=i
            else:
                limIzq=i+1
        i-=1
    while l <= lt.size(listaOrdenada) and VerDer:
        if not(lt.getElement(listaOrdenada,l)['category_id']==elemento):
            VerDer=False
            if l==lt.size(listaOrdenada):
                limDer=l
            else:
                limDer=l-1
        l+=1
    sub_list = lt.subList(listaOrdenada, limIzq, limDer-limIzq)
    sub_list = sub_list.copy()
    return sub_list


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))

def cmpByCountry(video1, video2):
    return ((video1['country']).lower() < (video2['country']).lower())

def cmpByID(video1, video2):
    return ((video1['video_id']).lower() < (video2['video_id']).lower())

def cmpByCategoryID(video1, video2):
    return ((video1['category_id']).lower() < (video2['category_id']).lower())

def cmpCategoryByName(categoria1, categoria2):
    return ((categoria1['name']).lower() < (categoria2['name']).lower())

# Funciones de ordenamiento

def VideosByViews(listaOrdenada):
    sub_list = lt.subList(listaOrdenada, 0, lt.size(listaOrdenada))
    sub_list = sub_list.copy()
    sorted_list = Merge.sort(sub_list, cmpVideosByViews)
    return sorted_list

def VideosByCountry(catalog):
    sub_list = lt.subList(catalog['video'], 0, lt.size(catalog['video']))
    sub_list = sub_list.copy()
    sorted_list = Merge.sort(sub_list, cmpByCountry)
    return sorted_list

def VideosByID(listaOrdenada):
    sub_list = lt.subList(listaOrdenada, 0, lt.size(listaOrdenada))
    sub_list = sub_list.copy()
    sorted_list = Merge.sort(sub_list, cmpByID)
    return sorted_list

def VideosByCategoryID(listaOrdenada):
    sub_list = lt.subList(listaOrdenada, 0, lt.size(listaOrdenada))
    sub_list = sub_list.copy()
    sorted_list = Merge.sort(sub_list, cmpByCategoryID)
    return sorted_list

def CategoryByName(catalog):
    sub_list = lt.subList(catalog['category'], 0, lt.size(catalog['category']))
    sub_list = sub_list.copy()
    sorted_list = Merge.sort(sub_list, cmpCategoryByName)
    return sorted_list




"""    categories = video['category'].split(",")
    for category in categories:
        addVideoCategory(catalog, category.strip(), video)
def addVideoCategory(catalog, category_id, video):
    categories = catalog['category']
    positioncategory = lt.isPresent(categories, category_id)
    if positioncategory > 0:
        category = lt.getElement(categories, positioncategory)
    else:
        category = newCategory(category_id)
        lt.addLast(categories, category)
    lt.addLast(category['category'], video)"""