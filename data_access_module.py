def read_text(path="prueba.mio"):

    tokens = []
    with open(path, "r") as file:
        for line in file:
            tokens.append(line.split())
    file.close()
    return tokens


def print_archivo(elements, path="salida.txt"):
    with open(path, "a") as out:
        for element in elements:
            out.write(f"{element}\n")
    out.close()
