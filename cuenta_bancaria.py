class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente (Persona):
    def __init__(self, nombre, apellido, cuenta,balance):
        super().__init__( nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre} apellido: {self.apellido}  con cuenta {self.cuenta} tiene un balance de: {self.balance}"
    def deposit(self):
        pass

    def retirar(self):
        pass



def crear_usuario(cuenta):

    cuenta =+1

    str_cuenta=str(cuenta)

    if len(str_cuenta) <5:
        cuenta = "0"*(5-len(str_cuenta))+str_cuenta


    nombre= input("Ingresa tu nombre: ")
    apellido= input("Ingresa tu apellido: ")
    balance= input("Ingresa  con cuanto deseas abriur tu cuenta: ")
    cliente = Cliente(nombre, apellido, cuenta,  balance)

    return cliente



def main():
    exit=False
    cuenta=0

    print("Bienvenido a Banamemex: ")

    usuario=crear_usuario(cuenta)

    print("Binvenido " +usuario.__str__())

    while exit == False:
        print("Seleccione una opcion:  \n1- Retirar\n2- Depositar\n3- Salir")
        opcion=int(input())

        if opcion==3:
            exit=True



    print("Vuelva Pronto ")






    return usuario



if __name__ == '__main__':
    main()
