"""
Tools to request CPU, Memory and disk utilization from a list of hosts
Work only in linux equipment need sh and sshpass
"""
import subprocess

def obtener_info(host, username, password):
    comando_cpu_info = f'sshpass -p "{password}" ssh {username}@{host} "cat /proc/cpuinfo | grep \'model name\'"'
    comando_cpu = f'sshpass -p "{password}" ssh {username}@{host} "top -bn1 | grep \'%Cpu\'"'
    comando_espacio_disco = f'sshpass -p "{password}" ssh {username}@{host} "df -h --output=source,used,pcent | grep -v \'Filesystem\'"'
    
    comando_cpu_info = subprocess.check_output(comando_cpu, shell=True).decode().strip().split(":")[1].strip()
    print(f"Información de {host}:")
    print(f"CPU: {comando_cpu_info}")
    # Obtener uso de CPU
    resultado_cpu = subprocess.check_output(comando_cpu, shell=True).decode().strip()
    cpu_usage = float(resultado_cpu.split()[1])
    print(f"Información de {host}:")
    print(f"Uso de CPU: {cpu_usage}%")
    
    # Obtener espacio libre en disco
    resultado_espacio_disco = subprocess.check_output(comando_espacio_disco, shell=True).decode().strip().split("\n")
    print("Espacio libre en disco:")
    for linea in resultado_espacio_disco:
        source, used, pcent = linea.split()
        print(f"{source}: {used} utilizado ({pcent})")
    
# Lista de hosts
hosts = [
    {
        "host": "example1.com",
        "username": "tu_usuario",
        "password": "tu_contraseña"
    },
    {
        "host": "example2.com",
        "username": "tu_usuario",
        "password": "tu_contraseña"
    },
    # Agrega más hosts según sea necesario
]

# Iterar sobre la lista de hosts y obtener información
for host_info in hosts:
    obtener_info(host_info["host"], host_info["username"], host_info["password"])