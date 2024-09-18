import RPi.GPIO as GPIO
import time

# Configurações do GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

def contagem_regressiva(tempo):
    minutos, segundos = divmod(tempo, 60)
    while tempo:
        print(f'{minutos:02d}:{segundos:02d}', end='\r')
        time.sleep(1)
        tempo -= 1
        minutos, segundos = divmod(tempo, 60)
    print("Contagem finalizada")
    GPIO.output(LED_PIN, GPIO.HIGH)

def obter_tempo():
    while True:
        try:
            tempo = int(input("Digite o tempo em segundos: "))
            if tempo > 0:
                return tempo
            else:
                print("O número deve ser positivo")
        except ValueError:
            print("O valor digitado deve srr um número")

def main():
    try:
        tempo = obter_tempo()
        contagem_regressiva(tempo)
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
