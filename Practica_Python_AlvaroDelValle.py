# python .\Practica_Python_AlvaroDelValle.py
""" """

# 1
"""
nombre_empresa = "TechSolutions"
ano_fundacion = 2010
print(f"{nombre_empresa} {ano_fundacion}")
"""
#2
"""
# 2.1

numero=input("Escriba un numero:")
if numero.isnumeric:
    numero=int(numero)
    print("Es un numero")
    if numero > 0:
        print(f"{numero} es positivo")
    elif numero<0:
        print(f"{numero} es negativo")
else:
    print("Error")


# 2.1
numeros ={1,2,3,4,5,6,7,8,9,10}
for numero in numeros:
    print(numero)
    """
# 3
"""
# 3.1
def calcular_iva(precioBase):
    precioBase=int(precioBase)
    precioIva = (precioBase / 100)*121
    print(f"Nuevo precio: {precioIva}")

precioBase= input("Escrib el precio a sumar el iva: ")
calcular_iva(precioBase)

# 3.2
Escrib el precio a sumar el iva: 100
Nuevo precio: 121.0
"""
# 4
"""
# 4.1
empleados=["Ana", "Carlos", "María","Luis"]
# 4.2
empleados.append("Pedro")
for empleado in empleados:
    print(empleado)
# 4.3
info_empleado ={
    "nombre": "Ramon",
    "edad": 42,
    "departamento": "ventas"
}
print(info_empleado)
print(info_empleado["nombre"])
# 4.4
print(info_empleado["departamento"])
"""
# 5
"""
# 5.1
class Producto(object):
    def __init__(self,nombre,precio,cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

# 5.2
    def calcular_total(self):
        precio=int(self.precio)
        cantidad=int(self.cantidad)
        total=precio*cantidad
        return total
# 5.3
    def aumentar_total(self,aumento):
        aumento=int(aumento)
        resultadoAumento=(self.cantidad+aumento)
        self.cantidad=resultadoAumento
        return resultadoAumento
    
    def disminuir_total(self,reduccion):
        reduccion=int(reduccion)
        resultadoDisminucion=(self.cantidad-reduccion)
        self.cantidad=resultadoDisminucion
        return resultadoDisminucion
        


test=Producto("Silla",4,200)
#5.4
total= test.calcular_total()
print(f"Total del calculo: {total}")
#5.5
aumento =input("Cantidad a aumentar: ")
resultadoAumento=test.aumentar_total(aumento)
print(resultadoAumento)
print(f"Comprobación: {test.cantidad}")
#5.6
reduccion =input("Cantidad a reducir: ")
resultadoDisminucion=test.disminuir_total(reduccion)
print(resultadoDisminucion)
print(f"Comprobación: {test.cantidad}")
"""
# 6
"""
# 6.1 6.2
import ast
#ast modulo para pasar el txt a una lista
f=open("empleados.txt")
print(f.read())
#María sin í si no "MarÃ­a"
#test extra para pasarlo a array
e=open("empleados.txt","r")
# "r" para indicar read, lectura, si no se indica no funciona
empleados=e.read()
nombrestest=ast.literal_eval(empleados)
for empleado in nombrestest:
    print(empleado)
"""
# 6.3
productoscsv=open("productos.csv")
#mostrar el contenido del csv directamente
print(productoscsv.read())
#print(open("productos.csv").read())

import csv

class Producto(object):
    def __init__(self,nombre,precio,cantidad):
        #declarar tipo de dato
        self.nombre=nombre
        self.precio=float(precio)
        self.cantidad=int(cantidad)

    
# def leerCsv():
datoscsv=open("productos.csv","r")
reader=csv.reader(datoscsv)
productos=[Producto(nombre,precio,cantidad)
for nombre,precio,cantidad in reader]
#mostrar recorriendo el array
print("Mostrando los productos en la lsita de objetos csv:")
for producto in productos:
    print(f"Nombre: {producto.nombre} Precio: {producto.precio} Cantidad: {producto.cantidad}")