
import socket

HOST = '192.168.15.11' #'192.168.26.28' #'192.168.15.8'
PORT = 5002
PORT_MYC = 5040


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST,PORT_MYC))
#udp.bind((HOST, PORT)) #função para ficar escutando 
#udp.connect((HOST, PORT))
udp.sendto(bytes('iniciando c',"utf-8"),(HOST, PORT))
print(HOST)
while True:
    
    mensagemR, endereço_cliente = udp.recvfrom(1024) 
    
    #mensagem = input('digite a mensagem : ')
    mensagemR = mensagemR.decode('utf-8')
    print('Mensagem Recebida:---> ',mensagemR)
    aux = mensagemR.split('|')
    confirm = aux[0]
    mensagem = aux[1] 
    
    #udp.sendto(bytes(mensagemR,"utf-8"),(HOST, PORT) )
    udp.sendto(bytes(confirm,"utf-8"),(HOST, PORT) )
     
    
   
    #print('Mensagem Recebida:---> ',mensagemRecebida)
    if mensagemR[0] == '&' :
            break
udp.close()

