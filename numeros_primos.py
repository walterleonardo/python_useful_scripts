"""
un generador de numeros primos
"""

def primos(a=2 ,b=200):
    #numeros primos
    for n in range(a,b):
        for x in range(2,n):
            if n % x == 0:
                print(n , "equals" , x , "*" , n//x)
                break
        else:
                ###LOOP
                print(n, "es un numero primo")

primos(2,200)
