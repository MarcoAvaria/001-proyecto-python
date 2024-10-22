import usuarios.usuario as user

class Acciones:
    
    def registro(self):
        print("Entiendo, vamos a comenzar el registro...")
        
        nombre = input("Cuál es tu nombre?: ")
        apellidos = input("Cuáles son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
    
        usuario = user.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"Listo {registro[1].nombre}, te has registrado con el mail {registro[1].email}")
        else:
            print("No has logrado registrarte, registro sin éxito")
        
    def login(self):
        print("\nComprendo, por favor ingresa tus datos para loguearte")
        
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            usuario = user.Usuario('', '', email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has identificado en el sistema el {login[5]}")
                self.proximasAcciones(login)
                 
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f'Login incorrecto, vuelve a intentarlo más tarde')
            
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota
        - Mostrar tus notas
        - Eliminar nota
        - Salir      
        """)
        
        accion = input('¿Qué quieres hacer?: ')
        if accion == "crear":
            print('Vamos a crear')
        elif accion == "mostrar":
            print('Vamos a mostrar')
        if accion == "eliminar":
            print('Vamos a eliminar')
        if accion == "salir":
            exit()