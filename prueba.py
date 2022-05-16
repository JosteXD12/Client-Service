import socket

def decodificar(msg, clv):
    i=0
    j=0
    d = [3,5,2]
    b = []
    c = 0
    count = 0
    while count < len(msg):
        c = ord(msg[count]) #ord convierte de letra a numero
        #c = mc - int(clv) # esta es la descodificacion segun la clave
        
        # print("c con clave: " +str(c))
        # if(c < 65 and c != 126):
        #     c = c%26
        # elif (c > 90):
        #     c = c%26
        # print("c listo para comparar: " +str(c))

        if(c >= 65 and c <= 90):
            c = c - d[j]
            if(c < 65):
                c = c - 64 + 90
        elif(c == 126):
            c = 32
        b.append(c)
        i = i + 1
        if(j < 2):
            j = j + 1
        else:
            j=0
        count = count + 1
    messageDecoded = ''
    for n in b:
        messageDecoded = messageDecoded + chr(n) #chr convierte de numero a letra
    return str(messageDecoded)

def codificar(msg, clv):
    i=0
    j=0
    d = [3,5,2]
    b = []
    count = 0
    while count < len(msg):
        c = ord(msg[count]) #ord convierte de letra a numero
        if(c >= 65 and c <= 90):
            c = c + d[j]
            if(c > 90):
                c = c + 64 - 90
        elif(c == 32):
            c = 126
        #c = c + int(clv) # codificamos la letra segun la clave
        
        # print("c condificando con clave: " +str(c))
        # if(c < 65 and c != 126):
        #     c = c%26
        # elif (c > 90):
        #     c = c%26
        # print("c condificando listo para comparar: " +str(c))


        b.append(c)
        i = i + 1
        if(j < 2):
            j = j + 1
        else:
            j=0
        count = count + 1
    messageEncoded = ''
    for n in b:
        messageEncoded = messageEncoded + chr(n) #chr convierte de numero a letra
    return str(messageEncoded)