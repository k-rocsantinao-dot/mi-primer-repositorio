#diccionarios Cinemax

#funciones 

diccionario_peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}


diccionario_cartelera= {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3],

}


def leer_opcion():
    try:
        opcion = int(input("ingrese una opcion: "))
    except ValueError:
        print("ingrese un numero entero\n")
    else:
        valor = opcion
        if valor >= 1 and valor <= 6:
            return valor
        else:
            print("valor fuera de rango\n")
            return None

    

def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")


def cupos_genero(genero):
    nombre_genero= input("elija un genero: ").lower()
    for i in range(diccionario_peliculas[i]):
       print(i)

    

def busqueda_precio(p_min, p_max):
    p_min = input("")
    p_max = input("")
    pass

def buscar_codigo(codigo):

    pass
    
def actualizar_precio(codigo, nuevo_precio):
    pass



#validaciones para agregar pelicula-------------------------------------------------------------------------------------------------------------------------------------
def es_codigo_valido(codigo):
    if codigo != "" and codigo != " ":
        return True
    else:
        return False
def es_titulo_valido(titulo):
    if titulo != "" and titulo != " ":
        return True
    else:
        return False
    
def es_genero_valido(genero):
    if genero != "" and genero != " ":
        return True
    else:
        return False

def es_duracion_valido(duracion):
    if duracion.isdigit() and int(duracion)> 0:
        return True
    else:
        return False
def es_clasificacion_valido(clasificacion):
    if clasificacion == "A" or clasificacion == "B" or clasificacion == "C":
        return True
    else:
        return False
    
def es_idioma_valido(idioma):
    if idioma != "" and idioma != " ":
        return True
    else:
        return False
    
def es_pelicula_3d(es_3d):
    respuesta_usuario= input("la pelicula es 3d?: ")
    if respuesta_usuario == "s" or "S":
        return True
    else:
        return False
def es_precio_valido(precio):
    if precio.isdigit() and int(precio) > 0:
        return True
    else:
        return False
def es_cupos_valido(cupos):
    if cupos.isdigit() and int(cupos) >= 0:
        return True
    else:
        return False
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#opcion 4 agregar pelicula
def agregar_pelicula(diccionario_peliculas):
    codigo = input("ingrese codigo: ")
    while not es_codigo_valido(codigo):
        print("codigo no valido, intente otra vez")
        codigo = input("ingrese codigo: ")

    titulo = input("ingrese nombre de la pelicula: ")
    while not es_titulo_valido(titulo):
        print("titulo no valido, intente otra vez")
        titulo = input("ingrese nombre de la pelicula: ")

    genero = input("ingrese genero de la pelicula: ")
    while not es_genero_valido(genero):
        print("genero no valido, intente otra vez")
        genero = input("ingrese genero de la pelicula: ")
    
    duracion = input("ingrese duracion de la pelicula: ")
    while not es_duracion_valido(duracion):
        print("duracion no valida, intente otra vez")
        duracion = input("ingrese duracion de la pelicula: ")

    clasificacion= input("ingrese clasificacion de la pelicula:")
    while not es_clasificacion_valido(clasificacion):
        print("clasificacion no valida, intente otra vez")
        clasificacion = input("ingrese clasificacion de la pelicula: ")

    idioma= input("ingrese idioma de la pelicula: ")
    while not es_idioma_valido(idioma):
        print("idioma no valido, intente otra vez")
        idioma = input("ingrese idioma de la pelicula: ")

    es_3d= input()
    pass

    precio = input("ingrese precio de la pelicula: ")
    while not es_precio_valido(precio):
        print("precio no valido, intente otra vez")
        precio = input("ingrese precio de la pelicula: ")

    cupos = input("ingrese cupos de la pelicula: ")
    while not es_cupos_valido(cupos):
        print("precio no valido, intentalo otra vez")

    

        

#programa principal 

opcion = 0 

while opcion != 6:
    menu_principal()
    leer_opcion()
    opcion = leer_opcion

    match opcion:
        case 1:
            cupos_genero(genero)
            pass
        case 2:
            busqueda_precio()
            pass
        case 3:
            actualizar_precio()
            pass
        case 4:
            agregar_pelicula(diccionario_peliculas)
            pass
        case 5:
            #funcion eliminar pelicula
            pass
        case 6:
            #salir
            print("programa finalizado")

    

    
    
    












