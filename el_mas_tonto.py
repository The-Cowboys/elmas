#leer archivo usuarios y correos
#seleccionar el tonto
#mandar mail a los tontos  

from correo import enviar_correo
from leer_archivo import leer_archivo
from tonto import encontrar_tonto


usuarios = leer_archivo("usuarios.csv")
correos = [usuario[1] for usuario in usuarios]
print(correos)
tonto = encontrar_tonto(usuarios)
enviar_correo(correos, tonto[0])