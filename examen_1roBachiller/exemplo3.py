
primer_palabro = input("Por favor ingresa un texto:")
segundo_palabro = input("Por favor ingresa otro texto:")

def compara_palabros(primer_palabro, segundo_palabro):
    if len(primer_palabro) != len(segundo_palabro):
        return False
    largo_texto = len(primer_palabro)
    for i in range(largo_texto):
        if primer_palabro[i] != segundo_palabro[largo_texto - i  -1]:
            return False
    return True
        


print(compara_palabros(primer_palabro, segundo_palabro))

