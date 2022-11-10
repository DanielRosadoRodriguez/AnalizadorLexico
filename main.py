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

theres_an_error = False
hint_message = ""

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
                theres_an_error = True
                hint_message = 'Es posible que te haya hecho falta cerrar comillas ["]'
        elif element.isnumeric():
            d_type = "[valorn]"
            nombre = f"{element}"
            value = f"{element}"
        elif element[:1] == "0x":
            try:
                deicmal_value = int(element[2:], 16)
                d_type = "[valorn]"
                nombre = f"{element}"
                value = f"{deicmal_value}"
            except ValueError:
                theres_an_error = True
                hint_message = "valor hexadecimal inválido"
        elif element[0].isnumeric() and not element.isnumeric():
            theres_an_error = True
            hint_message = 'valor no reconocido, inicia por un numero pero no es un valor numerico'
        elif not element.isalnum():
            theres_an_error = True
            hint_message = 'caracter no reconocido'
        elif element.isalpha():
            if len(element) <= 16:
                cont_ids += 1
                d_type = "[ids]"
                nombre = f"{element}"
                cont = f"{cont_ids}"
            else:
                theres_an_error = True
                hint_message = 'el elemento excede el número de caracteres permitidos'
        if theres_an_error:
            print_error_message(error_index=element_number, line_number=line_number, line=line, hint=hint_message)
            break
        else:
            try:
                file1_elements.append(d_type)
                if d_type == "[valorn]":
                    new_element = {
                        "d_type": d_type,
                        "values": {
                            "nombre": nombre,
                            "value": value
                        }
                    }
                else:
                    new_element = {
                        "d_type": d_type,
                        "values": {
                            "nombre": nombre,
                            "cont": cont
                        }
                    }
                file2_elements.append(new_element)
            except NameError:
                print("the d_type parameter is none")
    if theres_an_error:
        break

