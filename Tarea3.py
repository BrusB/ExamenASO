import os



# Creamos el bucle para las carpetas
for i in range(5):
    # Crear la variable nombre carpeta y le damos el valor folder mas el numero de cada iteración
    nom_carpeta = f"folder{i}"
    
    # Para crear la carpeta usamos os.makedirs que crea el directorio
    # Agregando exists_ok=True le indicamos que si algunos d elos directorios ya existe
    # no se genere un error si no que continue
    os.makedirs(nom_carpeta, exist_ok=True)
    
    # Bucle para crear los ficheros dentro de la carpeta
    for n in range(10):
        # Creamos la variable que contiene el nombre de los ficheros 
        nom_archivo = f"fichero{n}.txt"
        
        # Creamos la variable con el contenido del archivo
        texto = f"Este es el contenido del fichero {n}"
        
        # os.path.join recoge el nombre de la carpeta y del archivo par acrear el directorio
        # w es de write, es decir se abre cada archivo con permiso de escritura 
        # por ultimo file.write() escribe el texto dentro del archivo 
        with open(os.path.join(nom_carpeta, nom_archivo), "w") as file:
            file.write(texto)

print("Archivos creados")


