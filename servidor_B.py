import socket
from traceback import print_tb

HOST =  '' 
PORT = 5002

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # esta usando tcp
udp.bind((HOST, PORT))


lista_port_cliente = set()
cont = False
aux = 0

def servidor_B():
    print('modos: \n    "0"-> padrao \n  "1"-> teste time_out')
    selecionar_teste = input("selecione o modo de teste : ")
    if selecionar_teste == "0":
        padrao()
    if selecionar_teste == "1":
        teste_timeout()
    



def teste_timeout():
    print ('Aguardando conexão ')
    while True:
        mensagem, endereço_cliente = udp.recvfrom(1024)         #recebe
        #print('Cliente -> ',endereço_cliente )
        print(endereço_cliente,' ->  ',mensagem.decode('utf-8'))
        lista_port_cliente.add(endereço_cliente)
        #print('lista das portas cliente ->',lista_port_cliente)

        for ips in lista_port_cliente:
            #print('ipList: ',ips,'  ipAtua ->',endereço_cliente)
            if ips != endereço_cliente:
                mensagem = mensagem.decode('utf-8')
                print('s---> ',mensagem)
                if cont: 
                    udp.sendto(bytes(mensagem,'utf-8'),(ips))
                else:
                    print('n enviou ')
        aux += 1
        if aux % 2 == 0:
            cont = not cont

            
        strMensagem = str(mensagem)
        if strMensagem[0] == '&':
            break
        
    udp.close()
    
def padrao():
    
    print ('Aguardando conexão ')
    while True:
        mensagem, endereço_cliente = udp.recvfrom(1024)         #recebe
        #print('Cliente -> ',endereço_cliente )
        print(endereço_cliente,' ->  ',mensagem.decode('utf-8'))
        lista_port_cliente.add(endereço_cliente)
        #print('lista das portas cliente ->',lista_port_cliente)

        for ips in lista_port_cliente:
            #print('ipList: ',ips,'  ipAtua ->',endereço_cliente)
            if ips != endereço_cliente:
                
                mensagem = mensagem.decode('utf-8')
                print('s---> ',mensagem)
                udp.sendto(bytes(mensagem,'utf-8'),(ips))
       
        strMensagem = str(mensagem)
        if strMensagem[0] == '&':
            break
        
    udp.close()
    
servidor_B()