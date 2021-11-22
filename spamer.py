import socket
import random as rnd
import time
IP_ADDR = '127.0.0.1'
TCP_PORT=[50001]
#IP_ADDR = os.environ('IP_ADDR')
#TCP_PORT = os.envirion('TCP_PORT')

LETTERS = 'abcdifghijklmnopqrstuvwxyz'
print('Инициализируем TCP\IP')
#for p in range(len(TCP_PORT)):
def connect_n_send(addr, port, msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print('Устанавливаем соединен')
    s.connect((addr, port))
    s.send(str.encode(msg))
    s.close
    print (msg)
    
def gen_message(n):
    out = ''
    for i in range(n):
        if rnd.choice([0,1]):
            out = out + LETTERS[rnd.randrange(len(LETTERS))].upper()
        else:
            out = out + LETTERS[rnd.randrange(len(LETTERS))].lower() 
    return out
try:
    while(1):
        for m in range(len(TCP_PORT)):
            msg = "MESSAGE FOR PORT " + str(TCP_PORT[m]) + " IS : " + gen_message(rnd.randint(5, 50)) + "\r\n"
            connect_n_send(IP_ADDR, TCP_PORT[m], msg)
        time.sleep(1)
except Exception as exp:
    print("Error : ",   exp)
