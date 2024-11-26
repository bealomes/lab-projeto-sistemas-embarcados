#include <Arduino.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

// Definição dos pinos dos LEDs
#define LED1 2  // LED controlado pela Task 1
#define LED2 4  // LED controlado pela Task 2

// Handles das tasks
TaskHandle_t task1Handle = NULL;
TaskHandle_t task2Handle = NULL;

// Protótipos das funções das tasks
void vTaskLed1(void *pvParameters);
void vTaskLed2(void *pvParameters);

void setup() {
    Serial.begin(115200);
    delay(1000);

    // Configura os pinos dos LEDs como saída
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    // Inicializa os LEDs desligados
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);

    // Criação da Task 1 (LED1)
    xTaskCreatePinnedToCore(
        vTaskLed1,        // Função da Task
        "TaskLed1",       // Nome da Task
        1024,             // Tamanho da pilha
        NULL,             // Parâmetro
        2,                // Prioridade (Alta)
        &task1Handle,     // Handle da Task
        1                 // Núcleo 1
    );

    // Criação da Task 2 (LED2)
    xTaskCreatePinnedToCore(
        vTaskLed2,        // Função da Task
        "TaskLed2",       // Nome da Task
        1024,             // Tamanho da pilha
        NULL,             // Parâmetro
        1,                // Prioridade (Baixa)
        &task2Handle,     // Handle da Task
        0                 // Núcleo 0
    );
}

void loop() {
    vTaskDelay(portMAX_DELAY);
}

// Task 1: Acende e apaga o LED1 e notifica a Task 2
void vTaskLed1(void *pvParameters) {
    while (1) {
        Serial.println("Task 1: Acendendo LED1");
        digitalWrite(LED1, HIGH); // Acende o LED1
        vTaskDelay(pdMS_TO_TICKS(500)); // Aguarda 500ms
        digitalWrite(LED1, LOW); // Apaga o LED1
        Serial.println("Task 1: LED1 apagado");
        vTaskResume(task2Handle); // Retoma a Task 2
        vTaskSuspend(NULL); // Suspende a Task 1
    }
}

// Task 2: Acende e apaga o LED2 e notifica a Task 1
void vTaskLed2(void *pvParameters) {
    while (1) {
        Serial.println("Task 2: Acendendo LED2");
        digitalWrite(LED2, HIGH); // Acende o LED2
        vTaskDelay(pdMS_TO_TICKS(500)); // Aguarda 500ms
        digitalWrite(LED2, LOW); // Apaga o LED2
        Serial.println("Task 2: LED2 apagado");
        vTaskResume(task1Handle); // Retoma a Task 1
        vTaskSuspend(NULL); // Suspende a Task 2
    }
}
