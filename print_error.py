def print_error_message(line, line_number, error_index, hint=""):
    """funcion que imprime un mensaje de error"""

    error_line_message = f""
    line_str = f""

    for index, element in enumerate(line):
        line_str += f"{element} "
        if index == error_index:
            error_line_message += len(element) * "*"
        else:
            error_line_message += len(element) * " "
        error_line_message += " "

    print(f"- Danger! Error en la linea {line_number}:")
    if line_number < 2:
        print(f"            |")
    else:
        print(f"          {line_number - 1} | ")
    print(f"          {line_number} | {line_str}")
    print(f"          {line_number+1} | {error_line_message}")

    if hint != "":
        print(f"              {hint}")
