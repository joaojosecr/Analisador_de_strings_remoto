# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

import socket, sys
import platform 
from os import system
import time
import tratar_strings
import PySimpleGUI as sg #pip install pysimplegui
from keyboard import press #pip install keyboard

HOST = '127.0.0.1'  # endereço IP
PORT = 20005        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados


def desjuntar (s):
    i=0
    for i in range(len(s)):
        if s[i]=='*':
            v=s[0:i]
            s=s[i:]
            i=0
        if s[i]=='%':
            c=s[1:i]
            s=s[i:]
        if s[i]=="$":
            cc=s[1:i]
            s=s[i+1:]
            return v,c,cc,s
    return 0,0,0,'0'

def limpa_console():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

class Tela():
    def __init__(self):

        # Layout
        layout = [
            [sg.Text('Digite o texto a ser enviado ao servidor:')],
            [sg.Input(key='texto',do_not_clear=False),sg.Button('Enviar',bind_return_key=True)],
            [sg.Checkbox('Número de vogais      ',key='vogais',default=True),sg.Checkbox('Número de consoantes',key='consoante',default=True)],
            [sg.Checkbox('Número de caracteres',key='chars',default=True),sg.Checkbox('Inverso do texto',key='inverso',default=True)],
            [],
            [sg.Output(size=(60,7),key='output')]
        ]
        self.janela = sg.Window("Cliente").layout(layout)
        
        while(True):
            eventos, self.values = self.janela.read() 
            if eventos == sg.WIN_CLOSED:
                break
            if eventos == 'Enviar':
                self.Iniciar()
            
   
    def Iniciar(self):
        # Extrair dados     
        # self.button, self.values = self.janela.read()
        self.janela.find_element('output').Update('')
        
       
        self.texto = self.values['texto']
        self.vogais = self.values['vogais']
        self.consoantes = self.values['consoante']
        self.inverso = self.values['inverso']
        self.chars = self.values['chars']

        
        inicio(self.texto,self.vogais,self.consoantes,self.chars,self.inverso)


def inicio(texto,v,c,cc,i): 
    try:
            
            # Cria o socket UDP
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as UDPClientSocket:
            
            # Envia texto para o servidor
            UDPClientSocket.sendto(texto.encode(), (HOST, PORT))
            print("Mensagem: "+texto)

            
            s = UDPClientSocket.recvfrom(BUFFER_SIZE)[0].decode('utf-8')
            
            vogais,consoantes,chars,inverso = desjuntar(s)
            
            if(v==True):
                print("\nQuantidade de vogais: "+ str(vogais))
            if(c==True):
                print("Quantidade de consoantes: "+ str(consoantes))            
            if(cc==True):
                print("Quantidade de caracteres: "+ str(chars))
            if(i==True):
                print("Inverso do texto: "+ inverso)         
            # except Exception:
            #     print("Sem resposta do servidor.")

    except Exception as error:
        print("Sem conexão!")
        print(error)
        return


# if __name__ == "__main__":   
#     main(sys.argv[1:])

tela = Tela()
