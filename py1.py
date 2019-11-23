name=input()
#hay que ponerle una f al string para interpretar una variable
print(f"hola, como estás {name}!")

x=34

if x>0:
    print("x es positivo")
elif x<0:
    print("x es negativo")
else:
    print("x es cero")


name="Ruty"#Esto es un string
coordinadas=(10.1,50.6)
names=["Ruty", "Joaquin","Ivan", "Juanca"]#Esto es una lista

#Hacer un loop en un rango de números sin incluir al 5
for i in range(5):
    print(i)

names2=["Yeny","Carolina","Giraldo", "Rivera"]

for m in names:
    print(m)
#Aqui hice una lista con varios tipos de variables
l=[28,"Alice",True]
print(l[0])
print(l[1])
print(l[2])

#aqui hago sets, donde hay identificadores únicos sin orden
conjunto=set()
conjunto.add(1)
conjunto.add(8)
conjunto.add(10)
conjunto.add(4)
print(conjunto)

#Uso de Diccionarios, relacion y asignaciones entre elementos y variables
edad={"Andrés":34,"Yeny":29}
#Aqui reasigna la edad de yeny
edad["Yeny"]=20
edad["Andrés"] +=1
print(edad)
