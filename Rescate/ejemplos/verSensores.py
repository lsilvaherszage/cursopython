from controller import Robot
from controller import LED
from controller import Accelerometer

timeStep = 32
max_velocity = 6.28

robot = Robot()

#Motores
wheel_left = robot.getMotor("left wheel motor")
wheel_right = robot.getMotor("right wheel motor")

#Sensores de distancia
leftSensors = []
rightSensors = []
frontSensors = []

frontSensors.append(robot.getDistanceSensor("ps7"))
frontSensors[0].enable(timeStep)
frontSensors.append(robot.getDistanceSensor("ps0"))
frontSensors[1].enable(timeStep)

rightSensors.append(robot.getDistanceSensor("ps1"))
rightSensors[0].enable(timeStep)
rightSensors.append(robot.getDistanceSensor("ps2"))
rightSensors[1].enable(timeStep)

leftSensors.append(robot.getDistanceSensor("ps6"))
leftSensors[0].enable(timeStep)
leftSensors.append(robot.getDistanceSensor("ps5"))
leftSensors[1].enable(timeStep)

#Camaras
camaraI=robot.getCamera("camera_left")
camaraI.enable(timeStep)

camaraC=robot.getCamera("camera_centre")
camaraC.enable(timeStep)

camaraD=robot.getCamera("camera_right")
camaraD.enable(timeStep)

colour_camera = robot.getCamera("colour_sensor")
colour_camera.enable(timeStep)

#Emisor para mandar mensajes al supervisor
emitter = robot.getEmitter("emitter")

#Posicion
gps = robot.getGPS("gps")
gps.enable(timeStep)

#Sensores de temperatura
lhs = robot.getLightSensor("left_heat_sensor")
rhs = robot.getLightSensor("right_heat_sensor")

left_heat_sensor.enable(timeStep)
right_heat_sensor.enable(timeStep)
while robot.step(timeStep) != -1:
    wheel_left.setVelocity(0)
    wheel_right.setVelocity(0)
    print(frontSensors[0].getValue())
    #print(lhs.getValue())
    #elcolor= colour_camera.getImage()
    #print(elcolor)
    #x,y,z=gps.getValues()
    #print("X: ", x, "Y: ", y, "Z: ",z)

