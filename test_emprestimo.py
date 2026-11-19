from emprestimo import pode_emprestar


def test_limite_inclusivo_e_aceito():
    # Preparar
    quantidade = 5
    # Agir
    resultado = pode_emprestar(quantidade)
    # Verificar
    assert resultado is True


def test_acima_do_limite_e_rejeitado():
    # Preparar
    quantidade = 6
    # Agir
    resultado = pode_emprestar(quantidade)
    # Verificar
    assert resultado is False


def test_zero_e_rejeitado():
    # Preparar
    quantidade = 0
    # Agir
    resultado = pode_emprestar(quantidade)
    # Verificar
    assert resultado is False


def test_quantidade_nao_inteira_e_rejeitada():
    # Preparar
    quantidade = 4.5
    # Agir
    resultado = pode_emprestar(quantidade)
    # Verificar
    assert resultado is False
