#MRO hace referencia al orden establecido por pyhton en el que busca metodos y atributos

class A:
   def hablar(self):
       print("Hola desde A")
       
class F(A):
   def hablar(self):
       print("Hola desde F")
        
class B(F):
  pass
       
class C(A):
  pass

class D(B,C):
   pass
       
d= D()

d.hablar()


#Función mro para ver el orden en el que se heredan las funciones

print(D.mro())


#Llamar la dunción de una clase especifica
#Primero se pone la clase de la función especifica y luego como parametro de la función se pone el nombre del objeto

A.hablar(d)