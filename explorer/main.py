from pybricks.hubs import InventorHub
from pybricks.parameters import Port
from pybricks.pupdevices import UltrasonicSensor, Motor
from pybricks.tools import wait
from micropython import umath


# Initialize the sensor.
def main():
    I: InventorHub = InventorHub()
    t: int = 0
    d: int = 0

    for t in range(5, 0, -1):
        tc = str(t)
        I.display.text(tc)
        wait(1)
    I.speaker.beep(440, 100)

    # Initialize the sensor.
    sonar = UltrasonicSensor(Port.A)
    motor = Motor(Port.B)

    while True:
        motor.run_time(100, 30, wait=False)
        d = sonar.distance()
        if d < 2000:
            print("Distance: {}mm".format(d))


if __name__ == '__main__':
    main()
