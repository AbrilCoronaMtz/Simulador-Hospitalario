#Sistema hospitalario

En esta práctica se simula la llegada de pacientes a un hospital, se aplica programación paralela, concurrente y asíncrona en Python.

##Descripción
- **Registro**: El paciente llega y se registra, uso de hilos.
- **Diagnóstico**: El paciente es diagnosticado, uso de procesos.
- **Asignación de recursos**: Al paciente se le asigna una cama, uso de hilos.
- **Seguimiento y alta**: Se le da un seguimiento al paciente, uso de tareas asíncronas, se da de alta al paciente.

##Tecnologías usadas
- Python.
- Librerías: threading, multiprocessing, asyncio, time y random.

##Cómo ejecutar

1. Copiar o descargar el código
2. Asegurarse de tener Python (3.8 o superior) instalado
3. Ejecutar el programa

```bash
python Practica1.py

##Funcionamiento interno
* Se crean hilos para simular varios pacientes
* Cada paciente manda su diagnóstico a un pool de procesos para ejecutarlo en paralelo
* La asignación de camas tiene un semáforo para tener una cantidad específica de camas siendo usadas por los pacientes
* El seguimiento de los pacientes se realiza de forma asíncrona

##Autor
[Corona Martínez Abril Andrómeda]

##Licencia
Este proyecto es de uso libre con fines educativos.
