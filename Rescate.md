# Rescate

El simulador que vamos a utilizar es Webots versión 2020ar1.

Lo pueden bajar de este [link](https://github.com/cyberbotics/webots/releases/tag/R2020a-rev1)

El ambiente de simulación está en el mismo repositorio que estos documentos. Para no tener que buscarlo, acá está el [link](https://github.com/gzabala/cursopython/blob/master/Rescate/RescueMaze_Release7.zip) 

Robot es la clase que encapsula al robot en Webots. Tiene los siguientes componentes:

![Componentes](images/componentesRobot.png)

La ubicación de los sensores de distancia y leds es:

![Sensores](images/ubicacionDistYLeds.png)

Motores:
Para recuperarlos usamos

`getMotor("left wheel motor")`



