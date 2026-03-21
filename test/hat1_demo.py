"""Test motors"""

import time
import unittest

from buildhat import Hat, Motor
from buildhat.exc import DeviceError, MotorError

# Standard-HAT auf UART0 + Reset GPIO4
Hat(device="/dev/ttyAMA0", reset_gpio=4, boot0_gpio=22)

m = Motor("A")
m.set_default_speed(20)
print("HAT1 Motor A erkannt:", m.get_position())