from gpiozero import Button
from time import sleep

left = Button(2,True)
right = Button(6,False)
down = Button(17,False)

if __name__ == '__main__':
    while True:
        
        if right.is_pressed:
            print('Boton RIGHT presionado')
            sleep(0.4)
        elif down.is_pressed:
            print('Boton DOWN presionado')
            sleep(0.4)
        elif left.is_pressed:
            print('Boton LEFT presionado')
            sleep(0.4)
        else:
            print('Esperando')
            sleep(0.4)