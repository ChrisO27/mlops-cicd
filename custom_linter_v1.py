import os #para trabajar con los archivos
import argparse  #manejar los argumentos de la línea de comandos
import re #para trabajar con expresiones regulares
import sys #para interactuar con el sistema operativo


def check_black(file_path):
    """
    verificar las líneas en blanco antes de una definición de bloque (clase, función, if, while, for)"""

    # conteo de errores
    errors = 0

    # recorrer el archivo línea por línea 
    # 'r' para leer el archivo
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # desde la linea 2 hasta el final del archivo, verificar si hay una definición de bloque
        for i in range(2, len(lines)):
            # verificar si la línea actual es una definición de bloque
            if re.match(r'^\s*(class|def|if|while|for)', lines[i]):
                # verificar si las dos líneas anteriores están en blanco    
                if not re.match(r'^\s*', lines[i-1]) or not re.match(r'^\s*', lines[i-2]):
                    # si no hay dos líneas en blanco antes de la definición del bloque, imprimir un mensaje de error
                    print(f"{file_path}:{i+1}: Expected 2 blank lines before block definition")
                    # incrementar el contador de errores
                    errors += 1
                # verificar si hay más de dos líneas en blanco antes de la definición del bloque
                elif re.match(r'^\s*', lines[i-3]):
                    # si hay más de dos líneas en blanco antes de la definición del bloque, imprimir un mensaje de error
                    print(f"{file_path}:{i+1}: Too many lines before block definition")
                    errors += 1

    return errors

def lint_directory(directory):
    """
    Recorrer el directorio y verificar cada archivo .py
    """
    total_errors = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                total_errors += check_black(file_path)
    return total_errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom linter")
    parser.add_argument("directories", nargs='+', help="Directories to lint")

    args = parser.parse_args()

    total_errors = 0

    for directory in args.directories:
        total_errors += lint_directory(directory)

    if total_errors > 0:
        print(f"Total errors found: {total_errors}")
        sys.exit(1)
    else:
        print("No errors found.")
        sys.exit(0)