#Nombre:      Entorno Necesario para el Tutorial
#Aunto:       Daniel Legorreta
#Correo:      d.legorreta.anguiano@gmail.com

from __future__ import print_function
from distutils.version import LooseVersion as Version
import sys


#Revision Version Python
try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_RED)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_BLUE)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'


try:
    import importlib
except ImportError:
        print(FAIL, "La version necesaria es Python 3.4 (or 2.7)"
                " la verson instalada es %s." % sys.version)

    
#Validacion de los Pkts
def import_version(pkt, ver_min, msg_falla=""):
    mod = None
    try:
        mod = importlib.import_module(pkt)
        if pkt in {'PIL'}:
            ver = mod.VERSION
        else:
                ver = mod.__version__
        if Version(ver) < ver_min:
            print(FAIL, "%s  tiene necesita la  %s o version mayor, pero se"+ 
                  "tiene instalada la version %s."
                  % (lib, ver_min, ver))
        else:
            print(OK,'%s version %s' % (pkt, ver))
    except ImportError:
        print(FAIL,'%s not installed. %s' % (pkt, msg_falla))
        
    return mod


#Revision de la Version de Isntalada de Python
print('Ubicacion de Python en:', sys.prefix)
print()
print("Versión de Python:")
print(sys.version)
pyversion = Version(sys.version)
if pyversion >= "3":
    if pyversion < "3.4":
        print("La version necesaria es Python 3.4 (o 2.7)"
                " pero esta instalada en %s." %sys.version)               
elif pyversion >= "2":
    if pyversion < "2.7":
        print("La version 2.7 es requerida,"
                    " pero se tienen instalada la version %s." % sys.version)
else:
    print("Version Desconocida de Python: %s" % sys.version)

print()
requeridos = {'numpy': "1.6.1", 'scipy': "0.9", 'matplotlib': "1.0",
                'IPython': "3.0", 'sklearn': "0.18", 'pandas': "0.19",
                'seaborn':"0.7.1",'statsmodels':"0.8.0",
                'yaml': "3.11", 'PIL': "1.1.7"}

print("Paquetes y versión que se tienen Instaladas:")
all(import_version(lib, required_version) for lib, required_version in list(requeridos.items()))   
print()
