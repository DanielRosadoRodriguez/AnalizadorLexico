# declaramos los elementos del lenguaje
reservadas = ["PROGRAMA", "FINPROG", "IMPRIME", "LEE"]
operadores = ["+", "-", "*", "/"]
asignacion = ["="]
comentario = ["#"]

# inicializamos una lista que contendra los elementos del archivo de texto
tokens = []

with open("input.txt", "r") as file:
    for line in file:
        # separamos cada linea en sus elementos y las agregamos a la lista de tokens
        tokens.append(line.split())
file.close()
for line in tokens:
    if line[0] in comentario:
        continue
    for element in line:
        if element in operadores:
            d_type = "operador"
        elif element in asignacion:
            d_type = "asignacion"
        elif element in reservadas:
            d_type = "reservada"
        else:
            d_type = "identificador"
        print(f"{d_type}: {element}")
