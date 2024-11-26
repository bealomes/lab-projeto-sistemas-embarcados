from gpiozero import PWMLED
from time import sleep

# Configura o pino dos leds
led = PWMLED(17)

# Acende e apaga suavemente o led
def fade_led():
	# Aumenta o brilho
	for value in range (0, 101):
		led.value = value/100
		sleep(0.01)

	# Diminui o brilho
	for value in range(100, -1, -1):
		led.value = value/100
		sleep(0.01)
while True:
	fade_led()
