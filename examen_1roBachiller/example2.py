

archivo = open("meteo.txt")
lista
temperatura_max = -100
temperatura_min = 100
nombre_zona_max = ""
nombre_zona_min = ""

for value in archivo.readlines():
    lista_value = value.split(",")
    nombre = lista_value[0]
    temperatura = int(lista_value[1])
    if temperatura > temperatura_max:
        temperatura_max = temperatura
        nombre_zona_max = nombre

    if temperatura < temperatura_min:
        temperatura_min = temperatura
        nombre_zona_min = nombre
    
    resultado = "En {} hace una temperatura de {}".format(nombre, temperatura)
    print(resultado)
    print("#########")

print("La poblacion mas caliente es " + nombre_zona_max)
print("La poblacion mas fria es " + nombre_zona_min)







# while True:
#     linea = archivo.readline()
#     if not linea:
#         break
#     print(linea, end="")

archivo.close()