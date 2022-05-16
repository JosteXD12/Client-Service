import socket

def iniciarServidor(host,puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,puerto))
    s.listen(5) #La cantidad de peticiones

    while True:
        #Establecer conexcion
        (c, addr) = s.accept()

        print("Se establecio conexion con: %s" % str(addr))

        msg = 'Conexion establecido con : %s' % socket.gethostname() + "\r\n"
        c.send(msg.encode('utf8'))
        msg_rec = c.recv(1024)
        print(msg_rec.decode('ascii'))
        c.close()

if __name__ == "__main__":
    host = ""
    puerto = 8080
    iniciarServidor(host,puerto)