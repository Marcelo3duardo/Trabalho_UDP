import asyncio
import socket
import time


async def cliente_A():
    HOST = '192.168.26.28'
    PORT = 5005

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    alter = 0
    #udp.connect((HOST, PORT))
    while True:
        mensagemVoltou = '!'
        if alter == 0: 
            mensagem = '0|'
            alter = 1
        else:
            mensagem = '1|'
            alter = 0
            
        mensagem += input('digite a mensagem : ')
        print(mensagem)
        time_init = time.time()
        udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))
            
        mensagem = str(mensagem)
        
        #rodar em paralelo async
        
        while mensagemVoltou == '!':
            mensagemVoltou, endereço_cliente = await udp.recvfrom(1024)
            time_fin = time.time()
            tempo_corrido = time_fin - time_fin
            if mensagemVoltou[0] == '!' > 1 and tempo_corrido > 200 :
                #reenvia a mensagem
                udp.sendto(bytes(mensagem,"utf-8"),(HOST, PORT))

        #mensagemconfirm, endereço_cliente = udp.recvfrom(1024)
        
    
        print('Mensagem Recebida:---> ',mensagemVoltou.decode('utf-8'))
        #print('confirmação de mensagem:',mensagemconfirm.decode('utf-8'))
        if mensagem[2] == '&' :
                break
    udp.close()

asyncio.run(cliente_A())