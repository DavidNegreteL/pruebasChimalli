from gpiozero import MCP3008
from gpiozero import RGBLED
from time import sleep

led = RGBLED(red = 21 , green = 20 , blue = 19)
    
if __name__ == '__main__':
    while True:
        redVol = MCP3008(0)
        greenVol = MCP3008(1)
        blueVol = MCP3008(2)
        
        redVal = (redVol.value * 3.3) * (299/1023)
        greenVal = (greenVol.value * 3.3) * (299/1023)
        blueVal = (blueVol.value * 3.3) * (299 / 1023)
        
        led.color = (redVal,greenVal,blueVal)
        print(redVal ,' | ',greenVal, ' | ',blueVal )
        sleep(0.3)