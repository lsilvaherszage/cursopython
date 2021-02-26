from MiRobot import MiRobot

robot = MiRobot() #creo un objeto de la clase Robot

def caminataPorI():
    if robot.distanciaFrente()<0.04:
        robot.girar90D()
    else:
        if robot.distanciaIzquierda()>0.06:
            robot.velocidad(-1, 1)
        else:
            robot.velocidad(6, 6)

while robot.step() != -1:
    caminataPorI()