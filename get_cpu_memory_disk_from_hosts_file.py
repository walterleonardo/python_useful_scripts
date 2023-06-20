"""
Tools to request CPU, Memory and disk utilization from a list of hosts in csv file
Work only in linux equipment need sh and sshpass
"""
import subprocess
import json
import os

def obtener_info(host, username, password):
    print(host, username, password)

    comando_cpu_info = f'sshpass -p "{password}" ssh {username}@{host} "cat /proc/cpuinfo | grep \'model name\'"'
    comando_cpu = f'sshpass -p "{password}" ssh {username}@{host} "top -bn1 | grep \'%Cpu\'"'
    comando_espacio_disco = f'sshpass -p "{password}" ssh {username}@{host} "df -h --output=source,used,pcent | grep -v \'Filesystem\'"'
    try:
        comando_cpu_info = subprocess.check_output(comando_cpu, shell=True).decode().strip().split(":")[1].strip()
        print(f"Información de {host}:")
        print(f"CPU: {comando_cpu_info}")
    except Exception:
        print("Exception")
    
    try:
        # Obtener uso de CPU
        resultado_cpu = subprocess.check_output(comando_cpu, shell=True).decode().strip()
        cpu_usage = float(resultado_cpu.split()[1])
        print(f"Información de {host}:")
        print(f"Uso de CPU: {cpu_usage}%")
    except Exception:
        print("Exception")

    try:
        # Obtener espacio libre en disco
        resultado_espacio_disco = subprocess.check_output(comando_espacio_disco, shell=True).decode().strip().split("\n")
        print("Espacio libre en disco:")
        for linea in resultado_espacio_disco:
            source, used, pcent = linea.split()
            print(f"{source}: {used} utilizado ({pcent})")
    except Exception:
        print("Exception")

def leer_archivo(nombre_archivo):
    diccionario = {}
    if not os.path.isfile(nombre_archivo):
        return diccionario
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                host, ip, user, password = linea.split(", ")
                diccionario[host] = {'ip': ip, 'username': user, 'password': password}

    return diccionario

def main():
    diccionario = leer_archivo("get_cpu_memory_disk_from_hosts_file.txt")
    # Iterar sobre la lista de hosts y obtener información
    print(json.dumps(diccionario, indent=4))
    for host_info in diccionario.keys():
        print(diccionario.get(host_info).get('ip'))
        obtener_info(diccionario.get(host_info).get('ip'), diccionario.get(host_info).get('username'), diccionario.get(host_info).get('password'))




if __name__ == "__main__":
    main()