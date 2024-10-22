"""_summary_

Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la BBDD
- Si elegimos login, logueará en BBDD con las validaciones y confirmaciones correspondientes
- Crear nota, mostar, modificar, borrar.
"""
from usuarios import acciones

print("""
Acciones disponibles (ingresa el número correspondiente):
    1) Registro
    2) Login
""")

doThis = acciones.Acciones()
accion = input("¿Qué quieres hacer:")

if accion == '1':
    doThis.registro()
    

elif accion == '2':
    doThis.login()