#Autor: Vicmel Gabriel Molina Castillo
#Fecha: 18/03/2023
#Descripcion: Programa que valida nombre, edad y correo
menu="""
bienvenidos al registro de usuarios, llene los campos
que le soliciten y seleccione un numero del 1 al 3
[1]Digitar su nombre
[2]Digitar su edad
[3]Digitar su correo electronico
[4]Salir
"""
print(menu)
while True:
    op=input("Ingrese el numero de la opcion: ")
    if op=="1":
        nombre=input("Digite su nombre: ")
        if nombre.isalpha():
            print("Su nombre es: ",nombre)
        else:
            print("Ingrese un nombre valido")
    if op=="2":
        edad=input("Digite su edad: ")
        if edad.isdigit():
            print("Su edad es: ",edad)
        else:
            print("Ingrese una edad valida")
    if op=="3":
        correo=input("Digite su correo: ")
        if correo.find('@') >=0 and correo.find('.') >=1:
            print("Su correo es: ",correo)
        else:
            print("Ingrese un correo valido")
    if op=="4":
        exit()
        



  

    
   
