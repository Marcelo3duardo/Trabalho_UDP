import socket
import time

#globais
HOST = '192.168.26.28'
PORT = 5005
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.settimeout(2)

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
        while not ack_r:
            #envio
            udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))
            time_init = time.time()
            try:
                mensagemVoltou, endereço_cliente = udp.recvfrom(1024)
            except socket.timeout:
                print("Timeout")
            else:
                print('mensagem ->', mensagemVoltou.decode('utf-8'))
                ack_r = True

        #mensagemconfirm, endereço_cliente = udp.recvfrom(1024)

        #print('Mensagem Recebida:---> ',mensagemVoltou.decode('utf-8'))
        #print('confirmação de mensagem:',mensagemconfirm.decode('utf-8'))
        if mensagem[2] == '&' :
                break
    udp.close()



cliente_A()