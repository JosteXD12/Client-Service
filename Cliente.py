
import socket
from Codificador import Codi
from DinamicaPass import EstablecerPass

def iniciarCliente(host, puerto, msg_env, password):
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.connect((host,puerto))
    msg_rec = c.recv(1024)
    print (msg_rec.decode('utf8'))

    #codifica el mensaje

    print("Mensaje anterior: " + msg_env)
    msg_env = Codi(msg_env, EstablecerPass(password))
    print("Mensaje Codificado: " + msg_env)
    c.send(msg_env.encode('ascii'))
    c.close()

if __name__ == "__main__":
    host = "10.0.0.3"
    puerto = 44440
    msg = ""
    while True:
        msg = input("Digite el mensaje a enviar: ")
        iniciarCliente(host, puerto, msg, '352')
