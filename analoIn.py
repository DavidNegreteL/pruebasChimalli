from gpiozero import MCP3008
from time import sleep
    
if __name__ == '__main__':
    while True:
        cero = MCP3008(0)
        uno = MCP3008(1)
        dos = MCP3008(2)
        tres = MCP3008(3)
        cuatro = MCP3008(4)
        cinco = MCP3008(5)
        seis = MCP3008(6)
        siete = MCP3008(7)
        
        ceroVal = (cero.value * 3.3) * (299/1023)
        unoVal = (uno.value * 3.3) * (299/1023)
        dosVal = (dos.value * 3.3) * (299 / 1023)
        tresVal = (tres.value * 3.3) * (299/1023)
        cuatroVal = (cuatro.value * 3.3) * (299/1023)
        cincoVal = (cinco.value * 3.3) * (299 / 1023)
        seisVal = (seis.value * 3.3) * (299/1023)
        sieteVal = (siete.value * 3.3) * (299/1023)
        
        print(ceroVal,'|',unoVal,'|',dosVal,'|',tresVal,'|',cuatroVal,'|',cincoVal,'|',seisVal,'|',sieteVal )
        sleep(0.3)