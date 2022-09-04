import socket
from time import sleep
import select
import sys

#globais
HOST = '192.168.15.11' #'192.168.26.28'
PORT = 5002
PORT_MYA = 5001
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.setdefaulttimeout(4)
udp.settimeout(4)
#udp.setblocking(True) #nao deixa entrar no estado bloqueado
udp.bind((HOST, PORT_MYA))

def cliente_A():
    #HOST = '192.168.26.28'
    #PORT = 5005

    #udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    alter = 0
    #udp.connect((HOST, PORT))
    while True:
        mensagemVoltou = bytes('!',"utf-8")
        if alter == 0: 
            mensagem = '0|'
            alter = 1
        else:
            mensagem = '1|'
            alter = 0
        
        mensagem += input('digite a mensagem : ')
        print(mensagem)
        
       
            
        mensagem = str(mensagem)
        
        #rodar em paralelo async
        ack_r = False
        timeInSec = 2
        
        udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))
        while not ack_r:
           
            
            
            
            try:
                print('try ---')
                mensagemVoltou, endereço_cliente = udp.recvfrom(1024)
                #leu = select.select([udp.recvfrom(1024)],[],[],timeInSec)
                print('try +++')
            except socket.timeout:
                print('timeout ')
                sleep(1)
                udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))
                print('-> confirm')
            else:
                print('mensagem ', mensagemVoltou.decode('utf-8'))
                ack_r = True
            #envio
            '''udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))

            try:
                print('teste entrou no try')
                retorno = udp.recvfrom(1024)
                #mensagemVoltou, endereço_cliente = udp.recvfrom(1024)
                print('mensagem no try ->', retorno[0].decode('utf-8'))
            except socket.timeout:
                
                print("Timeout ",socket.timeout)
                udp.close()
            else:
                
                print('mensagem ->', retorno[0].decode('utf-8'))
                ack_r = True'''
                
            #udp.settimeout(2)
        #mensagemconfirm, endereço_cliente = udp.recvfrom(1024)

        #print('Mensagem Recebida:---> ',mensagemVoltou.decode('utf-8'))
        #print('confirmação de mensagem:',mensagemconfirm.decode('utf-8'))
            if mensagem[2] == '&' :
                break
    



cliente_A()