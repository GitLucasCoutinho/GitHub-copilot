import pytest

from dio_quis.is_quis_ import (
    calcular_pontuacao,
    imprimir_questoes,
    coletar_respostas,
    imprimir_resultado,
    QUESTOES,
    OPTION_COUNT,
)


def test_option_count():
    assert OPTION_COUNT == 4


def test_questoes_structure():
    assert len(QUESTOES) == 5
    for q in QUESTOES:
        assert "pergunta" in q
        assert "opcoes" in q
        assert "resposta_correta" in q
        assert "valor" in q
        assert len(q["opcoes"]) == 4


def test_calcular_pontuacao_all_correct():
    respostas = [0, 0, 2, 2, 3]
    pontuacao, detalhes = calcular_pontuacao(respostas)
    assert pontuacao == 5
    assert len(detalhes) == 5
    assert all(d["acertou"] for d in detalhes)


def test_calcular_pontuacao_all_incorrect():
    respostas = [1, 1, 1, 1, 1]
    pontuacao, detalhes = calcular_pontuacao(respostas)
    assert pontuacao == 0
    assert not any(d["acertou"] for d in detalhes)


def test_calcular_pontuacao_partial_correct():
    respostas = [0, 1, 2, 2, 3]
    pontuacao, detalhes = calcular_pontuacao(respostas)
    assert pontuacao == 4


def test_calcular_pontuacao_incomplete_respostas():
    respostas = [0, 0]
    pontuacao, detalhes = calcular_pontuacao(respostas)
    assert len(detalhes) == 5
    assert detalhes[2]["resposta_usuario"] == "Inválida"


def test_calcular_pontuacao_invalid_index():
    respostas = [0, 0, 2, 2, 99]
    pontuacao, detalhes = calcular_pontuacao(respostas)
    assert detalhes[4]["resposta_usuario"] == "Inválida"


def test_imprimir_questoes(capsys):
    imprimir_questoes()
    captured = capsys.readouterr()
    assert "Qual é a capital da França?" in captured.out
    assert "Paris" in captured.out
