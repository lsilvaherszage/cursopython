from controller import Robot
import time

timeStep = 32

robot = Robot()

wheel_left = robot.getMotor("left wheel motor")
wheel_right = robot.getMotor("right wheel motor")

max_velocity = wheel_left.getMaxVelocity()
print(max_velocity)

wheel_left.setPosition(float("inf"))
wheel_right.setPosition(float("inf"))

while robot.step(timeStep) != -1:
    wheel_left.setVelocity(0)
    wheel_right.setVelocity(0)