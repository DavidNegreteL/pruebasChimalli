from gpiozero import Servo
from time import sleep

servo1 = Servo(12)
servo2 = Servo(13)
servo3 = Servo(26)
servo4 = Servo(25)

while True:
    servo1.min()
    servo2.min()
    servo3.min()
    servo4.min()
    sleep(2)
    servo1.mid()
    servo2.mid()
    servo3.mid()
    servo4.mid()
    sleep(2)
    servo1.max()
    servo2.max()
    servo3.max()
    servo4.max()
    sleep(2)