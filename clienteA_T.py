from asyncio.windows_events import NULL
import socket
from time import sleep
import select
import sys

#globais
HOST = '192.168.15.8' #'192.168.26.28'
PORT = 5002
PORT_MYA = 5001
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.setdefaulttimeout(4)
udp.settimeout(4)
#udp.setblocking(True) #nao deixa entrar no estado bloqueado
udp.bind((HOST, PORT_MYA))

def cliente_A():
   
    Ack = '0'
    #udp.connect((HOST, PORT))
    while True:
        #mensagemVoltou = bytes('!',"utf-8")
        

        mensagemInput = input('digite a mensagem : ')
        
        checkS = findChecksum(mensagemInput)
        # juntando Ack, checkSum, mensagem
        mensagem = (Ack + '|' + checkS + '|' + mensagemInput)
        
        print(mensagem)
        
           
        mensagem = str(mensagem)
        
        ack_r = False
        
        
        
        while not ack_r:
            if Ack == '0': 
                print("Estado 1 ")
            else:
                print("Estado 4 ")
            udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))
                    
            try:
                print("estado 2")
                mensagemVoltou, endereço_cliente = udp.recvfrom(1024)
                #leu = select.select([udp.recvfrom(1024)],[],[],timeInSec)
             
            except socket.timeout:
                print('timeout ')
                sleep(1)
                #udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))
                
            else:
                print('mensagem ', mensagemVoltou.decode('utf-8'))
                #ack_r = True
            
                if mensagemVoltou.decode('utf-8') == Ack:
                    #esta certo
                    ack_r = True
                    print("Estado 3") 
                    if Ack == '0':    
                        Ack = '1'
                    else:
                        Ack = '0'
                        
                
            if mensagem[2] == '&':
                break
    





def findChecksum(mensagem):
    
   
    # Convertendo em binário
    binary_converted = ' '.join(map(bin, bytearray(mensagem, "utf-8")))

    # Transformando em lista para poder somar 
    list_binary_converted = binary_converted.split(' ')

    # Somando tudo
    checksumV = somaBinaria(list_binary_converted)

    return checksumV

def somaBinaria(lista_binaria):
    soma = "0"
    for bit in range(len(lista_binaria)):
        soma = bin(int(soma,2) + int(lista_binaria[bit],2)) #
    
    # Inverter somatório
    checkSum = ''
    strSoma = str(soma[2:])
    while (len(strSoma) < 16):
        strSoma = "0" + strSoma

    if (len(strSoma) > 16):
        # retirar o bit mais a esquerda
        strSoma = strSoma[(len(strSoma) - 16):]
    

    for caracDsoma in range(len(strSoma)):
        if strSoma[caracDsoma] == '1':
            checkSum += "0"
        else:
            checkSum += "1"
    
    return checkSum
    
cliente_A()
