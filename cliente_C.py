
import socket

HOST = '192.168.15.8' #'192.168.26.28' #'192.168.15.8'
PORT = 5002
PORT_MYC = 9050


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST,PORT_MYC))

def cliente_C():
    udp.sendto(bytes('iniciando c',"utf-8"),(HOST, PORT))
    print(HOST)
    while True:
        
        mensagemR, endereço_cliente = udp.recvfrom(1024) 
        
        #mensagem = input('digite a mensagem : ')
        mensagemR = mensagemR.decode('utf-8')
        print('Mensagem Recebida:---> ',mensagemR)
        aux = mensagemR.split('|')
        confirm = aux[0]
        checkSumR = aux[1]
        mensagem = aux[2]
        
        calculoCheckSum = findChecksum(mensagem)
        if checkSumR == calculoCheckSum:
            print('checkSum conferido')
        #udp.sendto(bytes(mensagemR,"utf-8"),(HOST, PORT) )
        udp.sendto(bytes(confirm,"utf-8"),(HOST, PORT) )

        #print('Mensagem Recebida:---> ',mensagemRecebida)
        if mensagemR[0] == '&' :
                break
    udp.close()

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

cliente_C()