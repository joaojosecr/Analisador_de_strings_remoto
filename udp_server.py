    # -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

#https://pythontic.com/modules/socket/udp-client-server-example

import socket, sys
import threading
import tratar_strings
import PySimpleGUI as sg 


HOST = '127.0.0.1'  # endereço IP
PORT = 20005        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados
server = True
def juntar(v,c,cc,i):
    return (str(v)+'*'+str(c)+'%'+str(cc)+'$'+str(i))

class Tela():
    def __init__(self):
        global server
        # Layout
        layout = [
            [sg.Text('Servidor UDP em Python para analise de string. ')],
            [sg.Output(size=(60,6),key='output')]
        ]

        self.janela = sg.Window("Server").layout(layout)

        while(True):
            eventos, self.values = self.janela.read() 
            
            p=threading.Thread(target=self.Iniciar, args=())
            match(eventos):
                case None:
                    p.start()
                    print("Iniciando server.")
                    server=False
                    break

            
    def Iniciar(self):
                
        inicio(sys.argv[1:])

def inicio(argv):
    global server
    try:
        # Create a datagram socket
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        UDPServerSocket.bind((HOST, PORT))
        print("UDP server up and listening")
        # Listen for incoming datagrams
        
        while(server):
            if (server==False):
                UDPServerSocket.close()
                break
            bytesAddressPair = UDPServerSocket.recvfrom(BUFFER_SIZE)

            mensagem = bytesAddressPair[0]
            endereco = bytesAddressPair[1]
            string = mensagem.decode('utf-8')
            
            clientIP  = "Client IP Address:{}".format(endereco)

            vogais,consoantes,inverso, chars = tratar_strings.tratar(string)
            
            print("Mensagem do cliente: " + string)
            print(clientIP)    
            s=juntar(vogais,consoantes,chars,inverso)

            # envia resposta ao cliente           
            
            print("Enviado para cliente: \n\tNúmero de vogais: "+str(vogais)+ "\n\tNúmero de consoantes: "+str(consoantes)+ "\n\tNúmero de caracteres: "+str(chars)+ "\n\tInverso da mensagem: "+inverso)
            UDPServerSocket.sendto(str(s).encode(), endereco)


    except Exception as error:  
        print("Erro na execução do servidor!!")
        print(error)        
        return             



if __name__ == "__main__":  
    inicio(sys.argv[1:])
    #tela=Tela()
    