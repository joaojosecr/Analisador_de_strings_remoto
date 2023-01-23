# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

import socket, sys

HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
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
            s=s[i+1:]
            return c,v,s
    return 0,0,'0'

def main(argv): 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Servidor executando!")
            while(True):       
                texto = input("Digite o texto a ser enviado ao servidor:\n")
                s.send(texto.encode()) #texto.encode - converte a string para bytes
                
                # vogais = s.recv(BUFFER_SIZE)
                # vogais=vogais.decode('utf-8')
                        
                
                # #if(v==True):
                # print("Quantidade de vogais: "+ str(vogais))
               
                
                
                data = s.recv(BUFFER_SIZE)
                texto_string = data.decode('utf-8') #converte os bytes em string
                print('Recebido do servidor', texto_string)
                
                c,v,i = desjuntar(texto_string)
                
            #if(c==True):
                print("\nQuantidade de consoantes: "+ str(c))            
            #if(v==True):
                print("Quantidade de vogais: "+ str(v))
            #if(i==True):
                print("Inverso do texto: "+ i)

                if (texto_string == 'bye'):
                    print('vai encerrar o socket cliente!')
                    s.close()
                    break
    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":   
    main(sys.argv[1:])