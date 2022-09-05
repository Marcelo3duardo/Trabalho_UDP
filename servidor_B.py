import socket

HOST =  '' 
PORT = 5002

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # esta usando tcp
udp.bind((HOST, PORT))

print ('Aguardando conexão ')
lista_port_cliente = set()
cont = False
aux = 0
while True:
    mensagem, endereço_cliente = udp.recvfrom(1024)         #recebe
    #print('Cliente -> ',endereço_cliente )
    print(endereço_cliente,' ->  ',mensagem.decode('utf-8'))
    lista_port_cliente.add(endereço_cliente)
    #print('lista das portas cliente ->',lista_port_cliente)

    for ips in lista_port_cliente:
        #print('ipList: ',ips,'  ipAtua ->',endereço_cliente)
        if ips != endereço_cliente:
            print('entrou no if ->>>',type(ips) )
            mensagem = mensagem.decode('utf-8')
            print('s---> ',mensagem)
            if cont: 
                print('enviando +++++++++++++++ ')
                udp.sendto(bytes(mensagem,'utf-8'),(ips))
            else:
                print('n enviou ---------------')
    aux += 1
    if aux % 2 == 0:
        cont = not cont






    
           
    strMensagem = str(mensagem)
    if strMensagem[0] == '&':
        break
    
udp.close()