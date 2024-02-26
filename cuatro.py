#importamos las librerias de psutil para ver el espacio de la particion
#la libreria os para que cree el directorio de log
#y la libreria logging para los mensajes 
import psutil 
import logging
import os 

def ver_espacio():
    #Creamos la variable usuario para obtener el nombre del usuario y asi 
    #poder crear el directorio
    usuario = input("Introduce tu nombre de usuario: ")

    #comprobamos que el usuario existe 
    if os.path.exists(f'/home/{usuario}'): 
        #con os.chdir nos movemos a la ruta donde queremos crear el directorio
        os.chdir(f'/home/{usuario}')
        #con os.system creamos el directorio logs 
        os.system('mkdir logs')
        # y a continución creamos el archivo espacio.log 
        with open ('logs/espacio.log', 'w') as file: 
            pass
    else : 
        print("Error el introducir nombre de usuario o no existe")


    #ahora creamos la varaible espacio y llamamos a la funcion disk_usage indicando la raiz  
    espacio = psutil.disk_usage('/')
    #transformamos el resultado de espacio a un porcentaje con la funcion percent
    porcentaje = espacio.percent

    #configuramos logging para que se ejecute en la ruta creada 
    logging.basicConfig(filename=f'/home/{usuario}/logs/espacio.log')
    #por ultimo creamos un if que muestre los mensajes dependiendo del espacio ocupado
    if porcentaje >= 80: 
        logging.error(f'Espacio ocupado: {porcentaje}%  Error: El espacio ocupado es mayor que 80%')
    elif 60 <= porcentaje < 80: 
        logging.warning(f'Espacio ocupado: {porcentaje}%  Warning: El espacio ocupado supera el 60%')
    else: 
        logging.info(f'Espacio ocupado: {porcentaje}%  Info: Espacio libre suficiente')

#ver_espacio()