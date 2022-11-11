# test for the string classification and string error
from data_access_module import read_text, print_archivo
from elementos_del_lenguaje import comentario, elementos_lenguaje
import comparisons as c
from print_error import print_error_message

tokens = read_text(path="input.txt")

cont_textos = 0
cont_variables = 0
lista_texto_1 = []
there_is_an_error = False

for line_number, line in enumerate(tokens):
    if line[0] in comentario:
        continue
    else:
        for element_number, element in enumerate(line):
            if c.is_reservada(element=element, reservadas=elementos_lenguaje):
                print(element)
                lista_texto_1.append(element)
                continue
            elif c.is_text(first_char=element[0], last_char=line[-1][-1]):
                print("[litalfnum]")
                cont_textos += 1
                d_type = "TXT"
                nombre = element
                cont = cont_textos
                lista_texto_1.append("[litalfnum]")
                continue
            elif element.isnumeric():
                print("[valorn]")
                d_type = "VAL"
                nombre = element
                valor = int(element)
                lista_texto_1.append("[valorn]")
                continue
            elif c.is_hexadecimal(element):
                print("[valorn]")
                d_type = "VAL"
                nombre = element
                valor = int(element, 16)
                lista_texto_1.append("[valorn]")
                continue
            elif c.is_id(element):
                cont_variables += 1
                print("[id]")
                d_type = "IDS"
                nombre = element
                cont = cont_variables
                lista_texto_1.append("[id]")
                continue

if not there_is_an_error:
    print_archivo(elements=lista_texto_1, path="texto_1.txt")
