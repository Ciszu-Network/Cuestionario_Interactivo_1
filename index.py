import time
import random
import datetime
import os
import sys
import logs

os.makedirs("logs", exist_ok=True)
original_stdout = sys.stdout
log_name = f"logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{random.randint(1, 1000)}.txt"

logs.start_log(log_name)

print(f"Bienvenido a este cuestionario creado por Ciszuko Antony... Este cuestionario fue creado con Python. {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
time.sleep(2)

def pedir_dato_numeros(pregunta, minimo=2):
    while True:
        dato = input(pregunta).strip()
        if len(dato) < minimo:
            print(f"La respuesta debe tener al menos {minimo} números.")
            continue
        if dato.isdigit():
            return dato
        else:
            print("Por favor, ingresa solo números.")

def pedir_texto_general(pregunta, minimo=2):
    while True:
        dato = input(pregunta).strip()
        if len(dato) < minimo:
            print(f"La respuesta debe tener al menos {minimo} caracteres.")
            continue
        return dato

def pedir_dato_letras(pregunta, minimo=2):
    while True:
        dato = input(pregunta).strip()
        if len(dato) < minimo:
            print(f"La respuesta debe tener al menos {minimo} letras.")
            continue
        if dato.replace(" ", "").isalpha():
            return dato.capitalize()
        else:
            print("Por favor, ingresa solo letras.")

def pedir_texto_largo(pregunta, minimo=20):
    while True:
        dato = input(pregunta).strip()
        if len(dato) < minimo:
            print(f"La respuesta debe tener al menos {minimo} caracteres.")
            continue
        return dato

def pedir_dato_names(imput):
    while True:
        dato = input(f"Ingrese su {imput}.\n> ").strip()
        if len(dato) < 2:
            print(f"El {imput} debe tener al menos 2 letras.")
            continue
        if dato.lower() in NOMBRES_PROHIBIDOS:
            print(f"El {imput} ingresado está prohibido. Intenta con otro.")
            continue
        elif dato.isalpha():
            return dato.capitalize()
        else:
            print(f"El {imput} solo debe contener letras.")
            continue

NOMBRES_PROHIBIDOS = ["admin",
                      "root",
                      "test",
                      "usuario",
                      "hitler",
                      "gey",
                      "pene",
                      "puta",
                      "mierda",
                      "culo",
                      "tonto",
                      "bobo",
                      "estupido",
                      "burro",
                      "puto",
                      "pija",
                      "joto",
                      "idiota"]
        
name = pedir_dato_names("nombre")
last_name = pedir_dato_names("apellido")
complete_name = f"{name} {last_name}"
print(f"Hola, {complete_name}!", end=" ")
time.sleep(2)

EMOCIONES_POSITIVAS = ["bien",
                       "genial",
                       "excelente",
                       "feliz",
                       "contento"]

EMOCIONES_NEGATIVAS = ["mal",
                       "triste",
                       "deprimido",
                       "enojado"]

status = pedir_dato_letras("¿Cómo estás hoy?:\n> ").strip().lower()
if any(emocion in status and "no" not in status for emocion in EMOCIONES_POSITIVAS) or \
   any("no" in status and emocion in status for emocion in EMOCIONES_NEGATIVAS):
    print("¡Me alegra escuchar eso!")
elif any(emocion in status and "no" not in status for emocion in EMOCIONES_NEGATIVAS) or \
     any("no" in status and emocion in status for emocion in EMOCIONES_POSITIVAS):
    print("Lo siento. Espero que tu día mejore.")
else:
    print("No entendí tu respuesta, pero espero que tengas un buen día de todos modos.")
time.sleep(2)

while True:
    age = input("¿Cuántos años tienes?.\n> ").strip()
    if age.isdigit():
        age = int(age)
        if age >= 120:
            print("¡Esa edad no es posible! A menos que seas un viajero del tiempo, por favor, ingresa una edad real.")
        elif age <= 0:
            print("¡Esa edad no es posible! A menos que seas un recien nacido, por favor, ingresa una edad real.")
        else:
            break
    else:
        print("Por favor, ingresa solo números positivos y realistas para la edad.")

print(f"¡{age} años!", end=" ")
time.sleep(2)

if age >= 18:
    print("¡Eres mayor de edad!")
else:
    print("¡Eres menor de edad!")
time.sleep(2)

genere = input("¿Cuál es tu género? Ejemplo: (Masculino | Femenino | Otros generos).\n> ").strip()
if genere.lower() in ("masculino","masculina","hombre","chico","señor","caballero","niño","varón","varonil","macho","hombrecito","hombrezuelo"):
    print(f"¡Hola, señor {name}!")
elif genere.lower() in ("femenino","femina","mujer","chica","señora","señorita","niña","femenina","hembra","mujerona","mujeril","dama"):
    print(f"¡Hola, señora {name}!")
else:
    print(f"¡Hola, tu genero: {genere} queda bien, {name}!")
time.sleep(2)

profession = pedir_dato_letras("¿Cuál es tu profesión?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡Vaya! {profession.capitalize()} es una profesión interesante.")
time.sleep(2)

color = pedir_dato_letras("¿Cual es tu color favorito?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡{color.capitalize()} es un color bonito!")
time.sleep(2)

animal = pedir_dato_letras("¿Cual es tu animal favorito?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡{animal.capitalize()} es un animal fascinante!")
time.sleep(2)

food = pedir_dato_letras("¿Cual es tu comida favorita?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡{food.capitalize()} suena delicioso!")
time.sleep(2)

country = pedir_dato_letras("¿De qué país eres?: | Minimo 2 letras.\n> ", minimo=2).strip()
print(f"¡Ah, {country.capitalize()} es un país maravilloso!")
time.sleep(2)

movie = pedir_texto_general("¿Cuál es tu película favorita?: | Minimo 2 letras\n> ", minimo=2).strip().lower()
print(f"¡{movie.capitalize()} es una película genial!")
time.sleep(2)

serie = pedir_texto_general("¿Cuál es tu serie favorita?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡{serie.capitalize()} es una serie entretenida!")
time.sleep(2)

game = pedir_texto_general("¿Cuál es tu juego favorito?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡{game.capitalize()} es un juego divertido!")
time.sleep(2)

sport = pedir_texto_general("¿Cuál es tu deporte favorito?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡{sport.capitalize()} es un deporte interesante!")
time.sleep(2)

hobby = pedir_dato_letras("¿Cuál es tu pasión?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡{hobby.capitalize()} es una pasión increible!")
time.sleep(2)

music = pedir_texto_general("¿Cuál es tu banda favorita?: | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡{music.capitalize()} es una banda impresionante!")
time.sleep(2)

DNI = pedir_dato_numeros("¿Cuál es tu DNI?: (DNI REAL) | Minimo 7 digitos.\n> ", minimo=7).strip().lower()
print(f"¡Perfecto! Tu DNI estara oculto.")
time.sleep(2)

number_phone = pedir_dato_numeros("¿Cuál es tu número de teléfono?: (Cualquier formato) | Minimo 9 digitos.\n> ", minimo=9).strip().lower()
print(f"¡Genial! Tu número de teléfono es {number_phone}.")
time.sleep(2)

favorite_number = pedir_dato_numeros("¿Cuál es tu número favorito?: (Cualquier número).\n> ", minimo=1).strip().lower()
print(f"¡Interesante! Tu número favorito es {favorite_number}.")
time.sleep(2)

website = pedir_texto_general("¿Cuál es tu sitio web?: (Puedes poner http:// o https://) | Minimo 2 letras.\n> ", minimo=2).strip().lower()
print(f"¡Genial! Tu sitio web es {website}.")
time.sleep(2)

bio = pedir_texto_general("Escribe una breve biografía sobre ti: | Minimo 20 letras.\n> ", minimo=20).strip().lower()
print("¡Gracias por compartir tu biografía!")
time.sleep(2)

apariencia = pedir_texto_general("¿Cómo describirías tu apariencia física?: | Minimo 10 letras.\n> ", minimo=10).strip().lower()
print("¡Gracias por compartir sobre tu apariencia física!")
time.sleep(2)

print("¡Gracias por completar el cuestionario!")
time.sleep(2)

resumen = f"""
➡️ Resumen de tus respuestas:

- Nombre: {name},
- Apellido: {last_name},
- Nombre completo: {complete_name},
- Edad: {age} años,
- Género: {genere},

- Profesión: {profession},
- Color favorito: {color},
- Animal favorito: {animal},
- Comida favorita: {food},
- País: {country},
- Pelicula favorita: {movie},
- Serie favorita: {serie},
- Juego favorito: {game},
- Deporte favorito: {sport},
- Pasión: {hobby},
- Banda favorita: {music},
- DNI: Oculto,
- Número de teléfono: {number_phone},
- Número favorito: {favorite_number},
- Sitio web: {website},
- Biografía: {bio},
- Apariencia física: {apariencia}."""

print(resumen)
time.sleep(5)

resumen_name = f"cuestionarioresumen_{complete_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{random.randint(1, 1000)}.txt"
with open(f"logs/{resumen_name}", "w", encoding="utf-8") as archive:
    archive.write(resumen + "\n\nEste es un resumen de tus respuestas del cuestionario.")
resumen_path = os.path.abspath(f"logs/{resumen_name}")
print(f"Resumen guardado en el archivo: {resumen_path} de la carpeta actual. (Puedes abrirlo con cualquier editor de texto).")
time.sleep(3)

log_path = os.path.abspath(f"logs/{log_name}")
print(f"Log guardado en el archivo: {log_path} de la carpeta actual. (Puedes abrirlo con cualquier editor de texto).")
logs.stop_log()
time.sleep(1)

print(f"Gracias por usar este programa {complete_name}. ¡Adiós!")
time.sleep(2)