
def EstablecerPass(contra):
    if len(contra) > 3 or len(contra) <= 0:
        raise Exception("Codificación inválida, fuera de rango [0,3]")
    Passw = []
    i = 0
    for n in contra:
        Passw.append(int(n))
        i += 1
    return Passw