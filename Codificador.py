from re import I

def Codi(msj, Contra):
    c = Contra
    i = 0
    j = 0
    caracter = ''
    code = ''
    while i != len(msj):
        caracter = msj[i]
        if(ord(caracter) >= 65 and ord(caracter) <= 90):
            caracter = chr(ord(caracter) + c[j])
            if(ord(caracter) > 90):
                caracter = chr(ord(caracter) - 90 + 64)
        elif ord(caracter) == 126:
            caracter = chr(32)
        code += caracter
        i += 1
        if j < 2:
            j += 1
        else:
            j = 0
    return code