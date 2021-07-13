from pybricks.geometry import Axis
from pybricks.hubs import InventorHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
from math import pi, sin


# Initialize the sensor.
def main():
    I: InventorHub = InventorHub()
    I.display.text("Hallo Buh")

    # Initialize the sensor.
    eyes = UltrasonicSensor(Port.A)

    # Initialize a timer.
    watch = StopWatch()

    # We want one full light cycle to last three seconds.
    PERIOD = 3000

    while True:
        # The phase is where we are in the unit circle now.
        phase = watch.time() / PERIOD * 2 * pi

        # Each light follows a sine wave with a mean of 50, with an amplitude of 50.
        # We offset this sine wave by 90 degrees for each light, so that all the
        # lights do something different.
        brightness = [sin(phase + offset * pi / 2) * 50 + 50 for offset in range(4)]

        # Set the brightness values for all lights.
        eyes.lights.on(brightness)

        # Wait some time.
        wait(50)


if __name__ == '__main__':
    main()
