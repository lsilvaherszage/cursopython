        self.sd0 = self.__robot.getDistanceSensor("ps0")
        self.sd1 = self.__robot.getDistanceSensor("ps1")
        self.sd2 = self.__robot.getDistanceSensor("ps2")
        self.sd3 = self.__robot.getDistanceSensor("ps3")
        self.sd4 = self.__robot.getDistanceSensor("ps4")
        self.sd5 = self.__robot.getDistanceSensor("ps5")
        self.sd6 = self.__robot.getDistanceSensor("ps6")
        self.sd7 = self.__robot.getDistanceSensor("ps7")
        self.leftSensors = []
        self.rightSensors = []
        self.frontSensors = []
        self.frontSensors.append(self.sd7)
        self.frontSensors[0].enable(MiRobot.timeStep)
        self.frontSensors.append(self.sd0)
        self.frontSensors[1].enable(MiRobot.timeStep)
        self.rightSensors.append(self.sd1)
        self.rightSensors[0].enable(MiRobot.timeStep)
        self.rightSensors.append(self.sd2)
        self.rightSensors[1].enable(MiRobot.timeStep)
        self.leftSensors.append(self.sd6)
        self.leftSensors[0].enable(MiRobot.timeStep)
        self.leftSensors.append(self.sd5)
        self.leftSensors[1].enable(MiRobot.timeStep)


    def cercaIzquierda(self):
        di = (self.leftSensors[0].getValue() + self.leftSensors[1].getValue()) / 2 
        if di < 0.05:
            return True
        else:
            return False

    def cercaDerecha(self):
        dd = (self.rightSensors[0].getValue() + self.rightSensors[1].getValue()) / 2 
        if  dd < 0.05:
            return True
        else:
            return False

    def cercaFrente(self):
        df = (self.frontSensors[0].getValue() + self.frontSensors[1].getValue()) / 2
        if df < 0.05:
            return True
        else:
            return False


    def sensorDis(self, val):                
        sensor = self.__robot.getDistanceSensor(val)
        sensor.enable(MiRobot.timeStep)
        valor = sensor.getValue()
        return valor