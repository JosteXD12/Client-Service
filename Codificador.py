from http import client
import Cliente

def tam():  # mismo que un difene
    tam = 100


def Codeficador():
    msg = Cliente.msg()
    if __name__ == "__main__":  # main
        i = 0
        j = 0
        d = [3, 5, 2]
        b = '[tam]'  # char con el valor de define
        C = ''
        Contador = 0
        while Contador <= len(msg): # realizamos un ciclo hasta completar el mensaje
            c = ord(msg[Contador])  #realizamos el conteo de caracteres del mensaje y lo convertimos a int para poder trabajar con ascii
            if c >= 65 and c <= 90:
                c -= d[j]
                if c < 65:
                    c = c - 64 + 90 # valanceo 
            elif c == 126:
                c = 32

            b.append(C)
            i += 1
            if j < 2:
                j += 1
            else:
                j = 0
            Contador +=1
        MsgCode = ""
        for n in b:
            MsgCode += chr(n) #conversion de int a string 
        return MsgCode
