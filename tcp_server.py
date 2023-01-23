# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

import socket, sys
from threading import Thread
import tratar_strings

HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados

def juntar(v,c,i):
    return (str(v)+'*'+str(c)+'%'+str(i))
    
def on_new_client(clientsocket,addr):
    while True:
        try:
            data = clientsocket.recv(BUFFER_SIZE)
            if not data:
                break
            texto_recebido = data.decode('utf-8') # converte os bytes em string
            print('recebido do cliente {} na porta {}: {}'.format(addr[0], addr[1],texto_recebido))
            
            vogais,consoantes,inverso = tratar_strings.tratar(texto_recebido)
            s=juntar(vogais,consoantes,inverso)
            # envia o mesmo texto ao cliente           
            clientsocket.send(str(s).encode())
            print("Enviado para cliente: " + s)

            if (texto_recebido == 'bye'):
                print('vai encerrar o socket do cliente {} !'.format(addr[0]))
                clientsocket.close() 
                return 
        except Exception as error:
            print("Erro na conexão com o cliente!! Erro: "+ str(error))
            return


def main(argv):
    try:
        # AF_INET: indica o protocolo IPv4. SOCK_STREAM: tipo de socket para TCP,
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            while True:
                server_socket.listen()
                clientsocket, addr = server_socket.accept()
                print('Conectado ao cliente no endereço:', addr)
                t = Thread(target=on_new_client, args=(clientsocket,addr))
                t.start()   
    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)        
        return             



if __name__ == "__main__":   
    main(sys.argv[1:])