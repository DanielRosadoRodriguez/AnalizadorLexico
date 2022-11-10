# test for the string classification and string error
from data_access_module import read_text
from elementos_del_lenguaje import comentario
from print_error import print_error_message

tokens = read_text(path="input_tests/test1.txt")

for line_number, line in enumerate(tokens):
    if line[0] in comentario:
        print("es un comentario")
        continue
    else:
        for element_number, element in enumerate(line):
            if element[0] == '"' and line[-1][-1] == '"':
                print("es un texto")
                break
            else:
                hint_message = "Es posible que te haya faltado cerrar comillas"
                print_error_message(line=line, line_number=line_number, error_index=element_number, hint=hint_message)
                break
