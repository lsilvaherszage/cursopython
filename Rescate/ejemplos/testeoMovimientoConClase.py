import Robots

robot = Robots.MiRobotI() #creo un objeto de la clase Robot
pozo=b';;;\xff'


while robot.step() != -1:
    robot.caminata()
    robot.noTeCaigas()
        
