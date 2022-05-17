import socket
from Cliente import iniciarCliente
from Decodificador import Decodi
from DinamicaPass import EstablecerPass

def iniciarServidor(host,puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,puerto))
    s.listen(5) #La cantidad de peticiones
    
    bandera = True
    msg_rec = ''

    while bandera:
        #Establecer conexcion
        (c, addr) = s.accept()
        print("Se establecio conexion con: %s" % str(addr))

        msg = 'Conexion establecido con : %s' % socket.gethostname() + "\r\n"
        c.send(msg.encode('utf8'))

        #Ejecutamos decodificador para el mensaje 

        msg_rec = c.recv(1024).decode("ascii")
        print(f"Mensaje codificado {msg_rec}")
        msg_rec = Decodi(msg_rec, EstablecerPass('352'))
        print(f"Mensaje descodificado {msg_rec}")
        c.close()
        bandera = False
    # segunda parte, conectarse a otro servidor..
    host = "25.10.252.91"
    puerto = 44440
    iniciarCliente(host, puerto, msg_rec, '352')

if __name__ == "__main__":
    host = "25.14.79.15"
    puerto = 44440
    iniciarServidor(host,puerto)