import socket

HOST =  '' #'192.168.26.28'   # 192.168.15.8'
PORT = 5002

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # esta usando tcp
udp.bind((HOST, PORT))
#udp.listen()
print ('Aguardando conexão ')
lista_port_cliente = set()
cont = False
while True:
    mensagem, endereço_cliente = udp.recvfrom(1024)         #recebe
    #print('Cliente -> ',endereço_cliente )
    print(endereço_cliente,' ->  ',mensagem.decode('utf-8'))
    lista_port_cliente.add(endereço_cliente)
    #print('lista das portas cliente ->',lista_port_cliente)
    contIndic = 0
    for ips in lista_port_cliente:
        #print('ipList: ',ips,'  ipAtua ->',endereço_cliente)
        if ips != endereço_cliente:
            #mandar a mensagem
            print('entrou no if ->>>',ips )
            #print('tipo ip ',type(ips[0]),'tipo host  ',type(ips[1]), 'tipo msg  ', type(mensagem))
            mensagem = mensagem.decode('utf-8')
            print('s---> ',type(mensagem),'  ',mensagem)
            if contIndic == 0: #tupla n recebe index
                udp.sendto(bytes(mensagem,'utf-8'),(ips))
            elif cont:        
                udp.sendto(bytes(mensagem,'utf-8'),(ips))
        contIndic += 0.5
    cont = not cont

    
           
    strMensagem = str(mensagem)
    if strMensagem[0] == '&':
        break
    
udp.close()