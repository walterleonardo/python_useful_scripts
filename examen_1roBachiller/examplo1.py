# Este es el ejemplo 1
''' hola este es un comentario
que puedo escribir en dos lineas o mas '''

btx1a = ["Antonia", "Joan", "Isabel", "Isabel", "Alejandro","Estafania"]
btx1b = ["Josep","Josep","Josep", "Miquel", "Aina", "Isabel", "Joan"]
diccionarioDeNombres = {}


for value in btx1a:
    if value in btx1b:
        diccionarioDeNombres[value] = btx1a.count(value) + btx1b.count(value)
    else:
        diccionarioDeNombres[value] = btx1a.count(value)

for value in btx1b:
    if value not in btx1a:
        diccionarioDeNombres[value] = btx1b.count(value)
        


for i in diccionarioDeNombres.keys(): 
    print(i, diccionarioDeNombres[i])

'''
{
    "Antonia": 1,
    "Josep": 2,
    "Joan":2
}
'''

print(diccionarioDeNombres["Josep"])