# test for the string classification and string error
from data_access_module import read_text, print_archivo
from elementos_del_lenguaje import comentario, elementos_lenguaje
import comparisons as c
from process_data import to_dictionary, parse_dictionary
from print_error import print_error_message

tokens = read_text(path="input.txt")

cont_textos = 0
cont_variables = 0
lista_texto_1 = []
lista_texto_2 = []
there_is_an_error = False

for line_number, line in enumerate(tokens):
    if line[0] in comentario:
        continue
    else:
        for element_number, element in enumerate(line):
            if c.is_reservada(element=element, reservadas=elementos_lenguaje):
                lista_texto_1.append(element)
                continue
            elif c.is_text(first_char=element[0], last_char=line[-1][-1]):
                cont_textos += 1
                d_type = "TXT"
                nombre = element
                valor = f"txt{cont_textos}"
                lista_texto_1.append("[litalfnum]")
            elif element.isnumeric():
                d_type = "VAL"
                nombre = element
                valor = int(element)
                lista_texto_1.append("[valorn]")
            elif c.is_hexadecimal(element):
                d_type = "VAL"
                nombre = element
                valor = int(element, 16)
                lista_texto_1.append("[valorn]")
            elif c.is_id(element):
                cont_variables += 1
                d_type = "IDS"
                nombre = element
                valor = f"id{cont_variables}"
                lista_texto_1.append("[id]")
            else:
                there_is_an_error = True
                print(f"Danger! Error en la linea {line_number}. Elemento que genera el error: {element}")
                break
            if not there_is_an_error:
                element_info = to_dictionary(d_type=d_type, name=nombre, value=valor)
                lista_texto_2.append(element_info)
    if there_is_an_error:
        break

if not there_is_an_error:
    print_archivo(elements=lista_texto_1, path="texto_1.txt")
if not there_is_an_error:
    lista_texto_2 = parse_dictionary(lista_texto_2)
    print_archivo(elements=lista_texto_2, path="texto_2.txt")
