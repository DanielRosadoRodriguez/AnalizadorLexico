# declaramos los elementos del lenguaje
reservadas = ["PROGRAMA", "FINPROG", "IMPRIME", "LEE"]
operadores = ["+", "-", "*", "/"]
asignacion = ["="]
comentario = ["#"]

# inicializamos una lista que contendra los elementos del archivo de texto
tokens = []

# leemos el documento con el input
with open("input.txt", "r") as file:
    # recorremos cada linea del archivo de texto
    for line in file:
        # separamos cada linea en sus elementos y las agregamos a la lista de tokens
        tokens.append(line.split())
# una vez terminado de guardar los elementos del archivo, cerramos el archivo de texto
file.close()

# recorremos el arreglo generado de tokens
for line in tokens:
    # si la linea inicia por #, es un comentario, pasamos a la siguiente linea
    if line[0] in comentario:
        continue
    # recorremos cada elemento en el arreglo
    for element in line:
        # clasificamos el elemento
        try:
            element = int(element)
            d_type = "constante"
        except ValueError:
            if element in operadores:
                d_type = "operador"
            elif element in asignacion:
                d_type = "asignacion"
            elif element in reservadas:
                d_type = "reservada"
            else:
                d_type = "identificador"

        print(f"{d_type}: {element}")
        with open("output.txt", "a") as out:
            out.write(f"{d_type}\n")
