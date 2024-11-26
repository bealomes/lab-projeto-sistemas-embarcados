from gpiozero import DistanceSensor, LED
from time import sleep

# Configurando o sensor e o LED
sensor = DistanceSensor(trigger=26, echo=24)
led = LED(18)

# Defina a distância mínima em cm para acionar o LED
distancia_minima = 10  # 10 cm

while True:
    sleep(0.1)
    
    # Medindo a distância em metros e convertendo para cm
    distance_cm = sensor.distance * 100
    print(f"Distância: {distance_cm:.2f} cm")
    
    # Acender o LED se a distância for menor que a mínima
    if distance_cm < distancia_minima:
        led.on()
    else:
        led.off()

