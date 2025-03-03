"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""

from os import system
from Package.class_video import Video
from Package.data import *

bandera_ingreso = False
bandera_seguir = True

while bandera_seguir:
    opcion = (input("""
                    a.Normalizar objetos:\n
                    b.Mostrar temas\n
                    c.Ordenar temas\n
                    d.Promedio de visitas\n
                    e.Maxima reproduccion\n
                    f.Busqueda por codigo\n
                    g.Listar por colaborador \n
                    h.Listar por mes\n
                    i.Salir\n
                    Elija una opcion: """))

    match opcion:
        case "a":
            for i in range(len(lista_videos)):
                lista_videos[i].dividir_titulo()
                lista_videos[i].obtener_codigo_url()
                lista_videos[i].formatear_fecha()

        # case "b":

        # case "c":
        # case "e":

        # case "f":

        # case "g":

        # case "h":

        # case None:


system("pause")
system("cls")
