ESTE ARCHIVO ES PARA SABER EL CONTEXTO EN MI GITHUB

# Sistema de Detección de Intrusiones con Redes Neuronales

Este proyecto consiste en un modelo de machine learning diseñado para detectar posibles intrusiones en una red utilizando una red neuronal.

## Características
- Clasificación binaria (tráfico normal vs ataque)
- Modelo basado en redes neuronales con TensorFlow/Keras
- Preprocesamiento y normalización de datos
- Evaluación mediante matriz de confusión
- Interfaz web desarrollada con Flask
- Sistema de predicción en tiempo real

## Modelo
El modelo recibe 5 características de entrada:
- duration
- protocol
- src_bytes
- dst_bytes
- count

Arquitectura de la red:
- Capas: 32 → 16 → 8 → 1 neuronas
- Funciones de activación: ReLU en capas ocultas y Sigmoid en la salida
- Función de pérdida: Binary Crossentropy
- Optimizador: Adam

## Resultados
- Precisión aproximada: 92%
- Dataset balanceado
- Buen rendimiento al detectar ataques

## Uso
Para ejecutar la aplicación:
