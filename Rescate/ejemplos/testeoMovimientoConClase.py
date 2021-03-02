import Robots

robot = Robots.MiRobotD() #creo un objeto de la clase Robot


while robot.step() != -1:
    robot.caminata()