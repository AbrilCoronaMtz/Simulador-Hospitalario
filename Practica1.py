#Librerías
import threading
import multiprocessing
import asyncio
import time
import random

#Semáforo para camas
camas = threading.Semaphore(5)

#Para el registro se usa concurrente (hilos)
def registro(paciente):
    print(f"El paciente {paciente} está siendo registrado")
    time.sleep(random.uniform(1,3)) #Se simula el tiempo de registro
    print(f"El paciente {paciente} ha sido registrado")

#Para el dignóstico se usa paralela (Procesos)
def diagnostico(paciente):
    print(f"Diagnosticando al paciente {paciente}")
    time.sleep(random.uniform(2,4)) #Simula el tiempo de diagnóstico (dura más que el registro)
    print(f"El paciente {paciente} ha sido diagnosticado")

#Para la asignación de recursos se usa concurrente (hilos)
def asignacion(paciente):
    with camas:
        print(f"Al paciente {paciente} se le está asignando una cama y un doctor")
        time.sleep(random.uniform(2,5)) #Se simula el tiempo de asignación de recursos
        print(f"Al paciente {paciente} se le han asignado los recursos necesarios")

#Para el seguimiento se usa asíncrona
async def seguimiento(paciente):
    print(f"Comenzando seguimiento del paciente {paciente}")
    await asyncio.sleep(random.uniform(1,5)) #Se simula el tiempo del seguimineto
    print(f"El seguimiento del paciente {paciente} ha terminado")

def proceso(paciente,pool):
    #Registro
    registro(paciente)

    #Diagnóstico
    print(f"🔬 Mandando diagnóstico del paciente {paciente} al pool de procesos...")
    pool.apply(diagnostico, args=(paciente,))  # Diagnóstico paralelo

    #Asignación de recursos
    asignacion(paciente)

    #Seguimiento
    asyncio.run(seguimiento(paciente))

    #Alta
    print(f"El paciente {paciente} ha sido dado de alta")

#main para correr el código
def main():
    inicio = time.time()

    pacientes = 1000
    recepcionistas = []

    print("Comienza la simulación")

    pool = multiprocessing.Pool(processes=3) 

    for i in range(pacientes):
        recepcionista = threading.Thread(target=proceso, args=(i,pool))
        recepcionistas.append(recepcionista)
        recepcionista.start()

    for recepcionista in recepcionistas:
        recepcionista.join()

    # Cerrar el pool de procesos
    pool.close()
    pool.join()

    fin = time.time()

    print("Fin de la simulación")

    duracion = fin - inicio
    print(f"Tiempo de la simulación: {duracion: .2f}")

if __name__ == '__main__':
        main()