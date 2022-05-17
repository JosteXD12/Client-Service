def Decodi(msj, contra):
    c = contra
    i = 0
    j = 0
    Contador = ''
    code = ''
    while i != len(msj):
        Contador = msj[i]
        if(ord(Contador) >= 65 and ord(Contador) <= 90):
            Contador = chr(ord(Contador) + c[j])
            if(ord(Contador) < 65):
                Contador = chr(ord(Contador) - 64 + 90)
        elif ord(Contador) == 126:
            Contador = chr(32)
        code += Contador
        i += 1
        if j < 2:
            j += 1
        else:
            j = 0
    return code
