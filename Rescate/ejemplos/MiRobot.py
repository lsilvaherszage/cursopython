from controller import Robot
import time

class MiRobot():
    timeStep = 32 #Cuantos ciclos de ejecucion tiene el simulador cada vez que hago un step
    maxVel=6.28
    pozo=b';;;\xff'

    def __init__(self):
        self.__robot = Robot() #creo un objeto de la clase Robot
        self.__wheel_left = self.__robot.getMotor("left wheel motor") #recupero un objeto de la clase motor
        self.__wheel_right = self.__robot.getMotor("right wheel motor")

        self.__wheel_left.setPosition(float("inf"))
        self.__wheel_right.setPosition(float("inf"))
        self.__valSens = 0

        #Ejercicio 3: Extender la clase MiRobot con los 8 sensores de distancia (de ps0 a ps7). El acceso a ellos es privado.
        #sensores de movimiento
        self.__sensores = [self.__robot.getDistanceSensor("ps0"), self.__robot.getDistanceSensor("ps1"), self.__robot.getDistanceSensor("ps2"), self.__robot.getDistanceSensor("ps3"), self.__robot.getDistanceSensor("ps4"), self.__robot.getDistanceSensor("ps5"), self.__robot.getDistanceSensor("ps6"), self.__robot.getDistanceSensor("ps7")]
        for sens in self.__sensores:
            sens.enable(MiRobot.timeStep)
        
        #disposicion Frente: 0 y 7, Izquierda: 5 y 6, Derecha: 1 y 2, Atras: 3 y 4  
        self.__sensFrente = [self.__sensores[0], self.__sensores[7]]
        self.__sensIzquierda = [self.__sensores[5], self.__sensores[6]]
        self.__sensDerecha = [self.__sensores[1], self.__sensores[2]]
        self.__sensAtras = [self.__sensores[3], self.__sensores[4]]

        #6. Extender la clase con la cámara inferior y recorrer el "mundoConPantanosYPozos" sin caerse.
        #izquierda, centro, derecha, abajo
        self.__camaras = [self.__robot.getCamera('camera_left'), self.__robot.getCamera('camera_centre'), self.__robot.getCamera('camera_right'), self.__robot.getCamera('colour_sensor')]
        for cams in self.__camaras:
            cams.enable(MiRobot.timeStep)    
            # cams.getImage()    Yo le mando el mensaje getImage a la camara cuando necesite obtener la
    
        #7. Extender la clase con el sensor de temperatura y detectar las víctimas termales, enviando el mensaje y deteniéndose 3 segundos.




        
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
        self.espera(1.05) #maquina del profe
        ##elf.espera(.6)

    def girar90D(self):
        self.velocidad(2, -2)
        self.espera(1.05) #maquina del profe
        #self.espera(.6)

    def step(self):
        return self.__robot.step(MiRobot.timeStep)
    
    #Ejercicio 4:Crear los métodos distanciaIzquierda(), distanciaDerecha() y distanciaFrente() 
    # que me devuelve la distancia del robot con algún objeto, 
    # UTILIZANDO ALGUNA FORMULA QUE CONSIDERE LOS SENSORES PERTINENTES.  
    
    def distanciaFrente(self):
        val = [va.getValue() for va in self.__sensFrente]        
        #return sum(val)/len(val)        
        return min(val)

    def distanciaIzquierda(self):
        val = [va.getValue() for va in self.__sensIzquierda] 
        #return sum(val)/len(val)        
        return min(val)
    
    def distanciaDerecha(self):
        val = [va.getValue() for va in self.__sensDerecha] 
        #return sum(val)/len(val)
        return min(val)

    def distanciaAtras(self):
        val = [va.getValue() for va in self.__sensAtras] 
        #return sum(val)/len(val)
        return min(val)
    
    def caminata(self):
        if self.distanciaFrente()<0.04:
            self.girar90D()
        else:
            if self.distanciaIzquierda()>0.06:
                self.velocidad(1, 3)
            else:
                self.velocidad(6, 6)
    
    def colorPiso(self):
        #return self.__camaraPiso.getImage()
        return self.__camaras[3].getImage() 
    
    def noTeCaigas(self):
        if self.colorPiso()==self.pozo:
           self.parar()
           self.velocidad(-2,-2) 
           self.espera(1)                    
           self.girar90D()
            
    
   
    
    