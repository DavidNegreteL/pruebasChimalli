from gpiozero import LED
from time import sleep
inA1 = LED(27)
inB1 = LED(22)
inA2 = LED(23)
inB2 = LED(24)
def adelante():
    inA1.on()
    inB1.off()
    inA2.on()
    inB2.off()
    
def atras():
    inA1.off()
    inB1.on()
    inA2.off()
    inB2.on()
    
def izq():
    inA1.on()
    inB1.off()
    inA2.off()
    inB2.on()
    
def der():
    inA1.off()
    inB1.on()
    inA2.on()
    inB2.off()
    
def paro():
    inA1.off()
    inB1.off()
    inA2.off()
    inB2.off()
    
if __name__ == '__main__':
     while True:
         adelante()
         sleep(1)
         paro()
         sleep(1)
         atras()
         sleep(1)
         paro()
         sleep(1)
         der()
         sleep(1)
         paro()
         sleep(1)
         izq()
         sleep(1)
         paro()
         sleep(3)
         