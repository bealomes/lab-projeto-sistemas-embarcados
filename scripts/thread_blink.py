import RPi.GPIO as GPIO
import time
import random
import threading

# Configuração dos pinos
LED_PIN = 18      # Pino do LED
BUTTON_PIN = 26  # Pino do botão

# Variável global para controlar a frequência do LED
led_frequency = 1.0

frequencies = [1.0, 0.5, 0.2]

# Mutex para proteger o acesso à variável led_frequency
mutex = threading.Lock()

# Configuração do GPIO
def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)  # Configura o LED como saída
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Configura o botão como entrada com pull-up

# Função para piscar o LED
def gpio_blink():
    global led_frequency
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(led_frequency)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(led_frequency)

# Função para alterar a frequência do LED ao pressionar o botão
def change_frequency():
    global led_frequency
    freq_index = 0
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Botão pressionado
            with mutex:  # Usa o mutex para evitar problemas de concorrência
                freq_index = (freq_index + 1) % len(frequencies)
                led_frequency = frequencies[freq_index]
            print(f"Frequência alterada para {led_frequency} segundos")
            time.sleep(0.5)  # Debounce para evitar múltiplas detecções

# Função para gerar e exibir uma contagem do tempo de execucao do programa
def random_count():
    count = 0
    while True:
        count += 1
        print(f"Tempo de programa: {count}", end='\r')
        time.sleep(1)  # Pausa de 1 segundos entre contagens

if __name__ == '__main__':
    try:
        setup_gpio()

        # Cria as threads para as diferentes funções
        thread1 = threading.Thread(target=gpio_blink)
        thread2 = threading.Thread(target=random_count)
        thread3 = threading.Thread(target=change_frequency)

        # Inicia as threads
        thread1.start()
        thread2.start()
        thread3.start()

        # Aguarda a conclusão das threads (loops infinitos)
        thread1.join()
        thread2.join()
        thread3.join()

    except KeyboardInterrupt:
        print("Interrompido pelo usuário.")
    finally:
        GPIO.cleanup()  # Limpa a configuração dos pinos GPIO ao encerrar o script

