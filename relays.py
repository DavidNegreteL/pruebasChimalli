from gpiozero import LED
from time import sleep
rele1 = LED(4)
rele2 = LED(5)
rele3 = LED(6)
rele4 = LED(17)
tiempo = 1

def blink():
    rele1.off()
    sleep(tiempo)
    rele1.on()
    sleep(tiempo)
    
    rele2.off()
    sleep(tiempo)
    rele2.on()
    sleep(tiempo)
    
    rele3.off()
    sleep(tiempo)
    rele3.on()
    sleep(tiempo)
    
    rele4.off()
    sleep(tiempo)
    rele4.on()
    sleep(tiempo)
    
if __name__ == '__main__':
    while True:
        blink()
    '''rele1.off()
    rele2.on()
    rele3.off()
    rele4.on()'''
    