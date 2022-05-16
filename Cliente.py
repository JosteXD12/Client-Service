import socket

def iniciarCliente(host,puerto,msg_env):
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.connect((host,puerto))
    msg_rec = c.recv(1024)
    print (msg_rec.decode('utf8'))
    c.send(msg_env.encode('ascii'))
    c.close()

if __name__ == "__main__":
    host = "10.0.0.3"
    puerto = 8080
    msg = "hola"
    while True:
        print("Digite el mensaje a enviar: ")
        msg = input()
        iniciarCliente(host,puerto,msg)
