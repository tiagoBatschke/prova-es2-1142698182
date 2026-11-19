LIMITE = 5  # LIMITE = 3 + D; D = 2


def pode_emprestar(quantidade):
    if quantidade < 1:
        return False
    return quantidade <= LIMITE
