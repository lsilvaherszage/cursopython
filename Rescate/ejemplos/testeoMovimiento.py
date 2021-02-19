from controller import Robot
import time

timeStep = 32 #Cuantos ciclos de ejecucion tiene el simulador cada vez que hago un step
maxVel=6.28

robot = Robot() #creo un objeto de la clase Robot

wheel_left = robot.getMotor("left wheel motor") #recupero un objeto de la clase motor
wheel_right = robot.getMotor("right wheel motor")

wheel_left.setPosition(float("inf"))
wheel_right.setPosition(float("inf"))

while robot.step(timeStep) != -1:
    wheel_left.setVelocity(maxVel/2)
    wheel_right.setVelocity(maxVel)