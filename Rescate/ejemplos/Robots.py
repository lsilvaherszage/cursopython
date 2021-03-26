from controller import Robot
from abc import ABC, abstractmethod
import time
import struct

class MiRobotA(ABC):
    timeStep = 32 #Cuantos ciclos de ejecucion tiene el simulador cada vez que hago un step
    maxVel=6.28
    pozo=b';;;\xff'
    messageSent=False

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
            sd.enable(MiRobotA.timeStep)
        for sd in self.__sdIzquierda:
            sd.enable(MiRobotA.timeStep)
        for sd in self.__sdDerecha:
            sd.enable(MiRobotA.timeStep)
        for sd in self.__sdAtras:
            sd.enable(MiRobotA.timeStep)
        self.__camaraFrente=self.__robot.getCamera("camera_centre")
        self.__camaraFrente.enable(MiRobotA.timeStep)
        self.__camaraPiso=self.__robot.getCamera("colour_sensor")
        self.__camaraPiso.enable(MiRobotA.timeStep)

        #Emisor
        self.__emitter = self.__robot.getEmitter("emitter")

        #GPS
        self.__gps = self.__robot.getGPS("gps")
        self.__gps.enable(MiRobotA.timeStep)

        #Sensores de temperatura
        self.__left_heat_sensor = self.__robot.getLightSensor("left_heat_sensor")
        self.__right_heat_sensor = self.__robot.getLightSensor("right_heat_sensor")

        self.__left_heat_sensor.enable(MiRobotA.timeStep)
        self.__right_heat_sensor.enable(MiRobotA.timeStep)

    def __sendMessage(self, v1, v2, carac):
        message = struct.pack('i i c', v1, v2, carac)
        self.__emitter.send(message)

    def sendVictimMessage(self):   
        position = self.__gps.getValues()
        if not MiRobotA.messageSent:
            self.__sendMessage(int(position[0] * 100), int(position[2] * 100), b'H')
            MiRobotA.messageSent = True

    def stopAtHeatedVictim(self):
        if self.__left_heat_sensor.getValue() > 32 or self.__right_heat_sensor.getValue() > 32:
            print('Encontre una victima con temperatura')
            self.parar()
            self.sendVictimMessage()
            self.espera(3.1)
        else:
            MirobotA.messageSent = False

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
            self.step()

    def girar90I(self):
        self.velocidad(-2, 2)
        self.espera(1.05)

    def girar90D(self):
        self.velocidad(2, -2)
        self.espera(1.05)

    def step(self):
        return self.__robot.step(MiRobotA.timeStep)

    def distanciaFrente(self):
        valores=[sens.getValue() for sens in self.__sdFrente]
        return min(valores)
        #return sum(valores)/len(valores)

    def distanciaIzquierda(self):
        valores=[sens.getValue() for sens in self.__sdIzquierda]
        return min(valores)

    def distanciaDerecha(self):
        valores=[sens.getValue() for sens in self.__sdDerecha]
        return min(valores)
    
    def imagenFrente(self):
        return self.__camaraFrente.getImage()

    def colorPiso(self):
        return self.__camaraPiso.getImage()

    @abstractmethod
    def caminata(self):
        pass


class MiRobotI(MiRobotA):

    def caminata(self):
        if self.distanciaFrente()<0.04:
            self.girar90D()
        else:
            if self.distanciaIzquierda()>0.06:
                self.velocidad(-1, 1)
            else:
                self.velocidad(6, 6)
                
    def noTeCaigas(self):
        if self.colorPiso()==self.pozo:
            self.velocidad(-2,-2)
            self.esperar(1)
            self.girar90D()

class MiRobotD(MiRobotA):

    def caminata(self):
        if self.distanciaFrente()<0.04:
            self.girar90I()
        else:
            if self.distanciaDerecha()>0.06:
                self.velocidad(1, -1)
            else:
                self.velocidad(6, 6)

    def noTeCaigas(self):
        if self.colorPiso()==self.pozo:
            self.velocidad(-2,-2)
            self.esperar(1)
            self.girar90I()
