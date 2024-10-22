import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"Bien {usuario[1]}, se procederá a crear una nota...")
        titulo = input("Introduce el título de la nota: ")
        descripcion = input("Mete el contenido de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo = "", descripcion = "")
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: \"{nota.titulo}\"")
        else:
            print(f"No se ha guardado la nota, te pedimos disculpas {usuario[0]}")
            
    def mostrar(self, usuario):
        print(f"\nEntiendo {usuario[id]}, aquí tienes tus notas: ")
        
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        for nota in notas:
            print("\n**************************************")
            print(nota[2])
            print(nota[3])
            print("**************************************")
            
    def borrar(self, usuario):
        print(f"\nComprendo, se procedera a borrar notas")
        
        titulo = input("Introduzca el titulo de nota a borrar")
        
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        
        if eliminar[0] >= 1:
            print(f"Se ha borrado al nota: {nota.titulo}")
        else: 
            print(f"Ha ocurrido un error, no se ha logrado borrar la nota, intente nuevamente más tarde")