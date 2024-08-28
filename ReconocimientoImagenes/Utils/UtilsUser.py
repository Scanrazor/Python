nombreUsuario ="roman"
contraseña = "1234"

nameUser = input("Nombre usuario: ")
password = input("Contraseña: ")
def userCorrect(nameUser, password):
    if nameUser == nombreUsuario and password == contraseña:
        print("True")
        return True
    else:
        print("False")
        return False
    
userCorrect(nameUser, password)