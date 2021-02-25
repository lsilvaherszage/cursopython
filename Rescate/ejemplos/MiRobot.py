from controller import Robot
import time

class MiRobot():
    timeStep = 32 #Cuantos ciclos de ejecucion tiene el simulador cada vez que hago un step
    maxVel=6.28

    def __init__(self):
        self.__robot = Robot() #creo un objeto de la clase Robot
        self.__wheel_left = self.__robot.getMotor("left wheel motor") #recupero un objeto de la clase motor
        self.__wheel_right = self.__robot.getMotor("right wheel motor")

        self.__wheel_left.setPosition(float("inf"))
        self.__wheel_right.setPosition(float("inf"))
        self.__sdFrente=[self.__robot.getDistanceSensor("ps0"),  self.__robot.getDistanceSensor("ps7")]
        self.__sdIzquierda=[self.__robot.getDistanceSensor("ps5"),  self.__robot.getDistanceSensor("ps6")]
        self.__sdDerecha=[self.__robot.getDistanceSensor("ps1"),  self.__robot.getDistanceSensor("ps2")]
        self.__sdAtras=[self.__robot.getDistanceSensor("ps3"),  self.__robot.getDistanceSensor("ps4")]
        for sd in self.__sdFrente:
            sd.enable(MiRobot.timeStep)
        for sd in self.__sdIzquierda:
            sd.enable(MiRobot.timeStep)
        for sd in self.__sdDerecha:
            sd.enable(MiRobot.timeStep)
        for sd in self.__sdAtras:
            sd.enable(MiRobot.timeStep)


    def setVi(self, valor):
        self.__wheel_left.setVelocity(valor)

    def setVd(self, valor):
        self.__wheel_right.setVelocity(valor)

    def velocidad(self, vi, vd):
        self.setVi(vi)
        self.setVd(vd)
    
    def parar(self):
        self.velocidad(0,0)

    def espera(self, tiempoEspera):
        #tomo Tiempo origen
        #mientrar tiempo Actual-tiempo origen<tiempoEspera
        #   hacete un step
        tiempoArranque=self.__robot.getTime()
        while self.__robot.getTime()-tiempoArranque<tiempoEspera:
            self.__robot.step(MiRobot.timeStep)

    def girar90I(self):
        self.velocidad(-2, 2)
        self.espera(1.05)

    def girar90D(self):
        self.velocidad(2, -2)
        self.espera(1.05)

    def step(self):
        return self.__robot.step(MiRobot.timeStep)

    def distanciaFrente(self):
        valores=[val.getValue() for val in self.__sdFrente]
        return min(valores)
        #return sum(valores)/len(valores)

    def distanciaIzquierda(self):
        valores=[val.getValue() for val in self.__sdIzquierda]
        return min(valores)
