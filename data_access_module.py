def read_text():
    """
    funcion que lee el archivo de texto de entrada y
    regresa su contenido en una varialbe
    """
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
    return tokens


def write_file(text):
    """function that writes to a file"""
    with open("prueba.lex", "a") as out:
        for line in text:
            write_file(f"{line}\n")
    out.close()
