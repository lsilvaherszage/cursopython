from MiRobot import MiRobot

robot = MiRobot() #creo un objeto de la clase Robot

while robot.step() != -1:
    robot.girar90I()
    robot.parar()
    robot.espera(1)
    # robot.girar90D()
    # robot.parar()    
    # robot.espera(1)
