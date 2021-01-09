# This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
# Use with other I2C sensors would be similar.
import time
import board
import busio
import adafruit_tca9548a
import adafruit_pcf8591.pcf8591 as PCF
from adafruit_pcf8591.analog_in import AnalogIn
from adafruit_pcf8591.analog_out import AnalogOut


# Create I2C bus as normal
i2c = busio.I2C(board.SCL, board.SDA)

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)



# For each sensor, create it using the TCA9548A channel instead of the I2C object
pcf = PCF.PCF8591(tca[0])

# After initial setup, can just use sensors as normal.
pcf_in_0 = AnalogIn(pcf, PCF.A0)
print(pcf_in_0)