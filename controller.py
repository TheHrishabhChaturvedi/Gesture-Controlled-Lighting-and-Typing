import pyfirmata
comport = 'COM3'
board = pyfirmata.Arduino(comport)
# Define LEDs (connected to Arduino digital pins 8–12)
led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')
def led(fingerUp):
 print("Detected Finger Pattern:", fingerUp)
 leds = [led_5, led_1, led_2, led_3, led_4]

 for i in range(5):
 leds[i].write(fingerUp[i])
