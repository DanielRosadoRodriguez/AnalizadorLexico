# test for the string classification and string error
from data_access_module import read_text
from elementos_del_lenguaje import comentario, elementos_lenguaje
import comparisons as c
from print_error import print_error_message

tokens = read_text(path="input.txt")

for line_number, line in enumerate(tokens):
    if line[0] in comentario:
        continue
    else:
        for element_number, element in enumerate(line):
            if c.is_reservada(element=element, reservadas=elementos_lenguaje):
                print(element)
            elif c.is_text(first_char=element[0], last_char=line[-1][-1]):
                print("[litalfnum]")
            elif element.isnumeric():
                print("[valorn]")
            elif c.is_hexadecimal(element):
                print("[valorn]")
            elif c.is_id(element):
                print("[id]")
