#Nombre:      Instalacion de lo faltante del entorno para el Tutorial
#Aunto:       Daniel Legorreta
#Correo:      d.legorreta.anguiano@gmail.com

from __future__ import print_function
import importlib 
import pip 
import sys


#Funcion para instalar paquete faltante
def install_pendientes(packages):
    pip.main(['install', packages])

#Modulos Requeridos
requeridos = {'numpy': "1.6.1", 'scipy': "0.9", 'matplotlib': "1.0",
                'IPython': "3.0", 'sklearn': "0.18", 'pandas': "0.19",
                'seaborn':"0.7.1",'statsmodels':"0.8.0",
                'yaml': "3.11", 'PIL': "1.1.7"}


#Validacion de los Pkts
def validacion_instalacion(pkt,msg_falla=""):
    mod = None
    try:
        mod = importlib.util.find_spec(pkt)
        if(mod is None):
                print()
                print("%s se intenta instalar"% pkt)
                install_pendientes(pkt)
                           
                #print("%s se encuentra instalado"% mod.name) 
        else:
                print("%s se encuentra instalado"% mod.name) 
    except ImportError:
        print("Revisar la lista de paquetes, hay un error!")
        
#Instalacion de todos los paquetes
print(">>Instalacion de Paquetes Faltantes")
print()
[validacion_instalacion(paquetes) for paquetes in list(requeridos.keys())]  
print("....................................................................................")
print("Si algun paquete no fue instalado revisa el mensaje de error")
print("posiblemente sea necesario instalar directamente con \'pip\' o revisar si el nombre es correcto.")
print("Proceso Concluido!")
              