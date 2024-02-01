import random

# Menu principal
print("Bienvenido al juego Piedra, Papel, Tijeras")

# Obtener la elección del usuario
usuario = input("Escribe con qué quieres atacar, Piedra, Papel o Tijeras: ").lower()

# Declarar listas de armas
Lista_Armas = ["piedra", "papel", "tijeras"]

# Obtener la elección de la CPU
cpu = random.choice(Lista_Armas)

# Declaramos las condiciones para determinar al ganador según el arma elegida
resultado = ""
if usuario == cpu:
    resultado = "Empatado"
elif (usuario == "papel" and cpu == "piedra") or (usuario == "piedra" and cpu == "tijeras") or (usuario == "tijeras" and cpu == "papel"):
    resultado = "Ganado"
else:
    resultado = "Perdido"
# Imprimir el resultado
print(f"Tu has elegido {usuario} y el ordenador ha elegido {cpu}. Has" + " ",resultado + " ""la partida")

