LIMITE = 5  # LIMITE = 3 + D; D = 2


def pode_emprestar(quantidade):
    if type(quantidade) is not int:
        return False
    if quantidade < 1:
        return False
    return quantidade <= LIMITE
