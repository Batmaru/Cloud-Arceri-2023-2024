def GeneraListaDigit():
    lista = [[a, b, c, d] 
             for a in range(10) 
             for b in range(10) 
             for c in range(10) 
             for d in range(10)]
    return lista

print(GeneraListaDigit())