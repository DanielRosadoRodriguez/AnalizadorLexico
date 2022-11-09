from data_access_function import read_text, write_file

# declaramos los elementos del lenguaje
reservadas = ["PROGRAMA", "FINPROG", "IMPRIME", "LEE"]
operadores = ["+", "-", "*", "/"]
asignacion = ["="]
comentario = ["#"]

elements_file2 = []
tokens = read_text()

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
            d_type = "[valorn]"
        except ValueError:
            if element in operadores:
                d_type = f"{element}"
            elif element in asignacion:
                d_type = "="
            elif element in reservadas:
                d_type = f"{element}"
            else:
                try:
                    element = int(element, 16)
                    d_type = "[HEX]"
                except ValueError:
                    d_type = "[id]"
