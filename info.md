# Documentación del Proyecto Cuestionario Interactivo creado por Ciszuko Antony

## Descripción

Este proyecto es un simple cuestionario de consola implementado en Python. Hace una serie de preguntas al usuario, recopila las respuestas y luego guarda un resumen de las respuestas en un archivo de texto. También crea un archivo de registro que captura la salida de la consola durante la ejecución del programa.

## Cómo ejecutar el proyecto

Para ejecutar el cuestionario, simplemente ejecute el archivo `run.bat`. Esto iniciará el script de Python en una nueva ventana de terminal.

Alternativamente, puede ejecutar el script de Python directamente desde la línea de comandos:

```bash
python index.py
```

## Estructura del proyecto

El proyecto tiene la siguiente estructura de archivos:

- `index.py`: El script principal de Python que contiene la lógica del cuestionario.
- `logs.py`: Un módulo de Python que maneja el registro de la salida de la consola.
- `run.bat`: Un archivo de script de Windows para ejecutar el cuestionario.
- `logs/`: Un directorio donde se guardan los archivos de resumen y registro del cuestionario.
- `info.md`: Documentación del proyecto en formato Markdown.
- `info.txt`: Documentación del proyecto en formato de texto sin formato.
- `README.md`: La documentación principal del proyecto para los usuarios de GitHub.
- `.gitignore`: Un archivo que especifica los archivos que Git debe ignorar.
- `LICENSE`: La licencia del proyecto.

## Descripción de los archivos

### `index.py`

Este es el archivo principal del proyecto. Contiene el código para:

- Hacer preguntas al usuario.
- Validar las respuestas del usuario.
- Guardar un resumen de las respuestas en un archivo de texto en el directorio `logs/`.
- Registrar la salida de la consola en un archivo de texto en el directorio `logs/`.

### `logs.py`

Este módulo proporciona funciones para iniciar y detener el registro de la salida de la consola en un archivo.

### `run.bat`

Este es un simple archivo de script de Windows que ejecuta el script `index.py` en una nueva ventana de terminal.

### `logs/`

Este directorio es creado por `index.py` si no existe. Contiene dos tipos de archivos:

- `cuestionarioresumen_*.txt`: Archivos que contienen el resumen de las respuestas del usuario al cuestionario.
- `log_*.txt`: Archivos que contienen la salida de la consola registrada durante la ejecución del cuestionario.
