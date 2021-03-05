#from controller import Robot
from MiRobot import MiRobot

r = MiRobot() #creo un objeto de la clase Robot
pozo=b';;;\xff'
#color=

while r.step() != -1:
    r.caminata()
    r.noTeCaigas()

    # if pozo ==r.colorPiso():
    #     print(r.colorPiso())
    #r.velocidad(2,2)
    #robot.girar90I()
    #robot.parar()
    #robot.espera(1)
    # robot.girar90D()
    # robot.parar()    
    # robot.espera(1)