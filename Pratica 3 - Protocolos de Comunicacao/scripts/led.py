import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
botao_pin = 6  # Pino do botão
led_pin = 26   # Pino do LED

# Configurando GPIOs de entrada e saída
GPIO.setup(botao_pin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

# Acende e desliga led
def acende(pin):
	if GPIO.input(pin):
		GPIO.output(led_pin, GPIO.LOW)
	else:
		GPIO.output(led_pin, GPIO.HIGH)

# Adiciona detecção de evento do botão
GPIO.add_event_detect(botao_pin, GPIO.BOTH, callback=acende, bouncetime=200)


try:
    while True: # loop principal
        pass  
except KeyboardInterrupt: # se programa encerrado limpa os pinos
	GPIO.cleanup()

