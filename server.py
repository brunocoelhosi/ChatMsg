import socket
import threading
HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen()

def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        i.send(mensagem)

def enviarMensagem(nome, sala, client):
    while True:
        mensagem = client.recv(1024)
        mensagem = f"{nome}: {mensagem.decode()}\n"
        broadcast(sala, mensagem)

salas = {}
while True:
    client, addr = sock.accept()
    client.send(b'SALA')
    nome = client.recv(1024).decode()
    sala = client.recv(1024).decode()

    #se sala n existir, crie uma
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)

    print(f'{nome} se conectou na sala {sala}! INFO {addr}\n')
    print(salas)
    broadcast(sala, f'{nome}: entoru na sala!\n')
    thread = threading.Thread(target=enviarMensagem,args =(nome,sala,client))
    thread.start()
    


