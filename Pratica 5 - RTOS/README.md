# Prática 5 - Uso de RTOS na ESP32

Nessa prática foi introduzida a programação de Sistemas Operacionais em Tempo Real por meio do FreeRTOS utilizando ESP32.
Escolhemos como aplicação um "ping-pong" entre duas tasks, cada uma utilizando um núcleo da ESP32. Primeiramente, a primeira task imprime um "ping" e acende um Led no pino 2, após isso ela adormece e notifica a segunda task que imprime um "pong" e acende um Led no pino 4.
