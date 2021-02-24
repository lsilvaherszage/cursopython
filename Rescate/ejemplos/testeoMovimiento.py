from controller import Robot
import time

timeStep = 32 #Cuantos ciclos de ejecucion tiene el simulador cada vez que hago un step
maxVel=6.28

robot = Robot() #creo un objeto de la clase Robot

wheel_left = robot.getMotor("left wheel motor") #recupero un objeto de la clase motor
wheel_right = robot.getMotor("right wheel motor")

wheel_left.setPosition(float("inf"))
wheel_right.setPosition(float("inf"))

def velocidad(vi, vd):
    wheel_left.setVelocity(vi)
    wheel_right.setVelocity(vd)

def setVi(valor):
    wheel_left.setVelocity(valor)

def setVd(valor):
    wheel_right.setVelocity(valor)

def parar():
    velocidad(0,0)

def espera(tiempoEspera):
    #tomo Tiempo origen
    #mientrar tiempo Actual-tiempo origen<tiempoEspera
    #   hacete un step
    tiempoArranque=robot.getTime()
    while robot.getTime()-tiempoArranque<tiempoEspera:
        robot.step(timeStep)

def girar90I():
    velocidad(-2, 2)
    espera(1.1)

def girar90D():
    velocidad(2, -2)
    espera(1.1)

while robot.step(timeStep) != -1:
    girar90I()
    parar()
    espera(1)
    girar90D()
    parar()    
    espera(1)
