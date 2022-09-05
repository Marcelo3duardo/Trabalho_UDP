import socket
from time import sleep
import select
import sys

#globais
HOST = '192.168.43.28' #'192.168.26.28'
PORT = 5002
PORT_MYA = 5001
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.setdefaulttimeout(4)
udp.settimeout(4)
#udp.setblocking(True) #nao deixa entrar no estado bloqueado
udp.bind((HOST, PORT_MYA))

def cliente_A():
   
    alter = 0
    #udp.connect((HOST, PORT))
    while True:
        #mensagemVoltou = bytes('!',"utf-8")
        if alter == 0: 
            Ack = '0|'
            alter = 1
        else:
            Ack = '1|'
            alter = 0
        
        k = 1024/4
       
        
        mensagemInput = input('digite a mensagem : ')
        
        checkS = str(findChecksum(mensagem,k))
        mensagem += (Ack,checkS,'|', mensagemInput)
        
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
                
                
            if mensagem[2] == '&':
                break
    





def findChecksum(mensagem, k):
    
    # Dividindo a mensagem em 4 pacotes de K bits
    c1 = mensagem[0:k]
    c2 = mensagem[k:2*k]
    c3 = mensagem[2*k:3*k]
    c4 = mensagem[3*k:4*k]

    # Calculando a soma binaria dos pacotes
    Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]

    # Adding the overflow bits
    if(len(Sum) > k):
        x = len(Sum)-k
        Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
    if(len(Sum) < k):
        Sum = '0'*(k-len(Sum))+Sum

    # Calculating the complement of sum
    Checksum = ''
    for i in Sum:
        if(i == '1'):
            Checksum += '0'
        else:
            Checksum += '1'
        return Checksum
    
    return Checksum
    #mensagem = [str(mensagem), Checksum]
    
cliente_A()