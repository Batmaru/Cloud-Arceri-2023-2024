def GeneraListaDigit():
    lista = []
    for i in range(0, 10000):
        s = str(i)
        s = "0" * (4 - len(s)) +s
        # s = s.zfill(4)
       # while len(s) < 4:
        #    s = "0" + s
        lista.append(s)
    return lista


#