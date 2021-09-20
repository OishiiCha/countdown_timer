from machine import Pin
import utime
import picoexplorer as display
from dht import DHT11, InvalidChecksum


# Wait 1 second to let the sensor power up
utime.sleep(1)

pin = Pin(0, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

#while True:
#    try:
#        print("Temperature: {}".format(sensor.temperature))
#        print("Humidity: {}".format(sensor.humidity))
#    except InvalidChecksum:
#        print("Checksum from the sensor was invalid")
#    utime.sleep(2)
    

width = display.get_width()
height = display.get_height()
display_buffer = bytearray(width * height * 2)
display.init(display_buffer)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

i = 0

while True:
    # the following two lines do some maths to convert the number from the temp sensor into celsius
    reading = sensor_temp.read_u16() * conversion_factor
    temperaturep = round(27 - (reading - 0.706) / 0.001721)

    # this if statement clears the display once the graph reaches the right hand side of the display
    if i >= (width + 1):
        i = 0
        display.set_pen(0, 0, 0)
        display.clear()

    # chooses a pen colour based on the temperature
    display.set_pen(0, 255, 0)
    if sensor.temperature > 25:
        display.set_pen(255, 0, 0)
    if sensor.temperature < 13:
        display.set_pen(0, 0, 255)

    # draws the reading as a tall, thin rectangle
    display.rectangle(i, height - (temperaturep * 5), 5, height)

    # draws a white background for the text
    if sensor.temperature > 25:
        display.set_pen(255, 255, 0)
    if sensor.temperature < 13:
        display.set_pen(255, 255, 100)
    display.rectangle(1, 1, 80, 50)

    # writes the reading as text in the white rectangle
    display.set_pen(0, 0, 4)
    display.text("{:.0f}".format(temperaturep) + "c " + "{}".format(sensor.temperature) + "c", 3, 3, 0, 3)

    # time to update the display
    display.update()

    # waits for 5 seconds
    utime.sleep(2)

    # the next tall thin rectangle needs to be drawn 6 pixels to the right of the last one
    i += 6
