from data_access_module import read_text
from print_error import print_error_message
# declaramos los elementos del lenguaje
reservadas = ["PROGRAMA", "FINPROG", "IMPRIME", "LEE"]
operadores = ["+", "-", "*", "/"]
asignacion = ["="]
comentario = ["#"]

tokens = read_text()
print(tokens)
file1_elements = []
file2_elements = []

cont_ids = 0
cont_italfanum = 0
cont_valrn = 0

for line_number, line in enumerate(tokens):
    if line[0] in comentario:
        # si un elemento es un comentario, lo ignoramos
        continue
    for element_number, element in enumerate(line):
        if element in reservadas or operadores or asignacion:
            file1_elements.append(element)
        elif element[0] == '"':
            if element[-1] == '"':
                cont_italfanum += 1
                d_type = "[litalfnum]"
                cont = f"txt{cont_italfanum}"
                nombre = element
            else:
                hint_message = 'Es posible que te haya hecho falta cerrar comillas ["]'
                print_error_message(error_index=element_number, line_number=line_number, line=line, hint=hint_message)



