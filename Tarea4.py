#importamos las librerias de psutil para ver el espacio de la particion
#la libreria os para que cree el directorio de log
#y la libreria logging para los mensajes 
import os
import psutil
import logging

#Funcion para crear los directorios, en este caso he utilizado os.makedirs en lugar de 
#chdir y system, ademas lo he empaquetado en una funcion para que sea mas facil despues 
#realizar la lógica de si existe o no el directorio
def crear_directorio_logs(usuario):
    ruta_logs = f'/home/{usuario}/logs'
    if not os.path.exists(ruta_logs):
        os.makedirs(ruta_logs)
        print(f'Se ha creado el directorio de logs en {ruta_logs}')
    else:
        print(f'El directorio de logs en {ruta_logs} ya existe. No ha sido necesario crearlo.')

#Funcion para configurar el directorio del logging que la recoge de la funcion ver_espacio
def configurar_registro(ruta_archivo):
    logging.basicConfig(filename=ruta_archivo)


#Por ultimo la funcion ver_espacio comprueba si existe el directorio, en caso de que no,
def ver_espacio():
    #DESCOMENTAR EL INPUT PARA QUE PIDA EL NOMBRE A TRAVES DE LA TERMINAL (NO HACER SI SE USA COMO SERVICIO) O SUSTITUIR EL NOMBRE DE USUARIO POR EL PROPIO 
    #usuario = input("Introduce tu nombre de usuario: ")
    usuario = 'brus'
    if os.path.exists(f'/home/{usuario}'):

        #llama a la funcion crear_directorio_logs,
        crear_directorio_logs(usuario)

        #despues usa psutil para ver el espacio del disco y lo transforma a porcentaje
        espacio = psutil.disk_usage('/')
        porcentaje = espacio.percent
        
        #luego se llama a la funcion configurar registro con los datos del usuario
        configurar_registro(f'/home/{usuario}/logs/espacio.log')

        #y por ultimo se realiza el if que se encarga de los mensajes 
        if porcentaje >= 80:
            logging.error(f'Espacio ocupado: {porcentaje}%  Error: El espacio ocupado es mayor que 80%')
        elif 60 <= porcentaje < 80:
            logging.warning(f'Espacio ocupado: {porcentaje}%  Warning: El espacio ocupado supera el 60%')
        else:
            logging.info(f'Espacio ocupado: {porcentaje}%  Info: Espacio libre suficiente')
    else:
        print("Error al introducir nombre de usuario o no existe")

#He comentado la llamada dado que al llamarlo desde Tarea5 la funcion se ejecutaba dos veces
#ver_espacio()
