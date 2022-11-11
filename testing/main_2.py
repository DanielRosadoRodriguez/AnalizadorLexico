from data_access_module import read_text, print_archivo, print_2ndo_archivo
from print_error import print_error_message
# declaramos los elementos del lenguaje
reservadas = ["PROGRAMA", "FINPROG", "IMPRIME", "LEE"]
operadores = ["+", "-", "*", "/"]
asignacion = ["="]
comentario = ["#"]

tokens = read_text()
file1_elements = []
file2_elements = []

for n_line, line in enumerate(tokens):
    if line[0] == "#":
        continue
    else:
        for n_element, element in enumerate(line):
            print(element[:2])
            if element in reservadas or element in operadores or element in asignacion:
                print(element)
                continue
            elif element[:1] == "0x":
                print(f"{n_element} {element}")
