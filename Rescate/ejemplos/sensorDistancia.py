from controller import Robot
import time

timeStep = 32 #Cuantos ciclos de ejecucion tiene el simulador cada vez que hago un step
maxVel=6.28

robot = Robot() #creo un objeto de la clase Robot

wheel_left = robot.getMotor("left wheel motor") #recupero un objeto de la clase motor
wheel_right = robot.getMotor("right wheel motor")

sdfd=robot.getDistanceSensor("ps0")
sdfd.enable(timeStep)

sdfi=robot.getDistanceSensor("ps7")
sdfi.enable(timeStep)

wheel_left.setPosition(float("inf"))
wheel_right.setPosition(float("inf"))

while robot.step(timeStep) != -1:
    wheel_left.setVelocity(maxVel)
    wheel_right.setVelocity(maxVel)
    sd=sdfd.getValue()
    si=sdfi.getValue()

    if sd<0.1:
        wheel_left.setVelocity(-maxVel)
    elif si<0.1:
        wheel_right.setVelocity(-maxVel)

    # La velocidad que tenga en cada motor en este punto, es la VERDADERA, LA QUE EL SIMULADOR VA A APLICAR