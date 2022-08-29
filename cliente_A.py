
import socket
import time

HOST = '192.168.26.28'
PORT = 5005

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
alter = 0
#udp.connect((HOST, PORT))
while True:
    
    if alter == 0: 
        mensagem = '0|'
        alter = 1
    else:
        mensagem = '1|'
        alter = 0
        
    mensagem += input('digite a mensagem : ')
    print(mensagem)
    inicio = time.time()
    udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))
         
    mensagem = str(mensagem)
    
    #rodar em paralelo async
    mensagemVoltou, endereço_cliente = udp.recvfrom(1024)
    
    
    #mensagemconfirm, endereço_cliente = udp.recvfrom(1024)
    
   
    print('Mensagem Recebida:---> ',mensagemVoltou.decode('utf-8'))
    #print('confirmação de mensagem:',mensagemconfirm.decode('utf-8'))
    if mensagem[2] == '&' :
            break
udp.close()

