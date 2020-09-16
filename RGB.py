from gpiozero import RGBLED
from time import sleep
led = RGBLED(red = 21 , green = 20 , blue = 19)
def coloresBase():
    
    #Todo apagados
    led.color = (1, 1, 1)
    sleep(1)
    #Rojo maxima intensidad
    led.color = (0, 1, 1)
    sleep(1)
    #verde  maxima intensidad
    led.color = (1, 0, 1)
    sleep(1)
    #Azul  maxima intensidad
    led.color = (1, 1, 0)
    sleep(1)
    #Todos a media intensidad
    led.color = (0.5, 0.5, 0.5)
    sleep(1)
    #"Blanco" Todos máxima intensidad
    led.color = (0, 0, 0)
    sleep(1)
    
if __name__ == '__main__':
    while True:
        coloresBase()