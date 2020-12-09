import threading
import socket

host = '127.0.0.1' #localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast (message):
  for client in clients:
    client.send(message)
    
def handle (client):
  while True:
    try:
      message = client.recv(1024)
      broadcast(message + "")
    except:
      index = clients.index(client)
      clients.remove(client)
      client.close()
      nickname = nicknames[index]
      broadcast(nickname + " has left the chat room!".encode('ascii'))
      nicknames.remove(nickname)
      break



def receive ():
  while True:
    client, address = server.accept()
    print("Connected with " + str(address))
    
    client.send('NICK'.encode('ascii'))
    nickname = client.recv(1024).decode('ascii')
    nicknames.append(nickname)
    lients.append(client)
    
    print("Nickname of the client is " + nickname + " !")
    broadcast(nickname + ' has entered the chat!'.encode('ascii'))
    client.send('Connected to the server!'.encode('ascii'))
    
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
print("server is listening")
receive()
