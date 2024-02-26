import psutil

# Obtener información sobre las particiones del disco y le damos el valor a la 
#variable particiones 
particiones = psutil.disk_partitions()

# Para mostrar la informacion de cada particion utilizanos un ciclo for que introduce
# en la variable 'particion' cada cada una de estas 
print("Particiones del disco:")
for particion in particiones:
    # Obtenemos la informacion del uso del disco con la funcion disk_usage y le damos 
    # el valor a la variable espacio
    espacio = psutil.disk_usage(particion.mountpoint)
    #Despues imprimimos el directorio de cada particion con 'particion.device'
    # y el porcentaje de uso con 'espacio.percent
    print(f"{particion.device} {espacio.percent:.1f}%")


