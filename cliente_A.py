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
        

        mensagemInput = input('digite a mensagem : ')
        
        checkS = findChecksum(mensagemInput)
        # juntando Ack, checkSum, mensagem
        mensagem = (Ack + checkS + '|' + mensagemInput)
        
        print(mensagem)
        
           
        mensagem = str(mensagem)
        
        ack_r = False
        
        
        udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))
        while not ack_r:
     
                    
            try:
                
                mensagemVoltou, endereço_cliente = udp.recvfrom(1024)
                #leu = select.select([udp.recvfrom(1024)],[],[],timeInSec)
             
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
    





def findChecksum(mensagem):
    
    # Dividindo a mensagem em 4 pacotes de K bits
   
    # Convertendo em binário
    binary_converted = ' '.join(map(bin, bytearray(mensagem, "utf-8")))
    # transformar em lista 
    #print('mensagem --> ',mensagem)
    # Transformando em lista para poder somar 
    list_binary_converted = binary_converted.split(' ')
    print ('valor em binário -->',type(binary_converted),' ---',binary_converted)
    # Somando tudo
    checksumV = somaBinaria(list_binary_converted)
    print ('valor da soma binária -->',checksumV)
    return checksumV

def somaBinaria(lista_binaria):
    soma = "0"
    for bit in range(len(lista_binaria)):
        soma = bin(int(soma,2) + int(lista_binaria[bit],2))
    print('Valor da soma ->',soma)
    # inverter somatório
    checkSum = ''
    strSoma = str(soma[2:])
    for caracDsoma in range(len(strSoma)):
        if strSoma[caracDsoma] == '1':
            checkSum += "0"
        else:
            checkSum += "1"
    print('checkSumF -->',checkSum)
    
    return checkSum
    
cliente_A()