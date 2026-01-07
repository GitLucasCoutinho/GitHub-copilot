from typing import List, Tuple, Dict

Question = Dict[str, object]

OPTION_COUNT = 4

QUESTOES: List[Question] = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Paris", "Lyon", "Marselha", "Nice"],
        "resposta_correta": 0,
        "valor": 1,
    },
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
        "resposta_correta": 0,
        "valor": 1,
    },
    {
        "pergunta": "Qual é a capital da Austrália?",
        "opcoes": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "resposta_correta": 2,
        "valor": 1,
    },
    {
        "pergunta": "Qual é a capital do Canadá?",
        "opcoes": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
        "resposta_correta": 2,
        "valor": 1,
    },
    {
        "pergunta": "Qual é a capital do Japão?",
        "opcoes": ["Osaka", "Quioto", "Hiroshima", "Tóquio"],
        "resposta_correta": 3,
        "valor": 1,
    },
]


def calcular_pontuacao(respostas_usuario: List[int]) -> Tuple[int, List[Dict[str, object]]]:
    """
    Compara as respostas do usuário com as respostas corretas e retorna
    a pontuação total e detalhes por questão.
    """
    pontuacao = 0
    detalhes: List[Dict[str, object]] = []

    for indice, questao in enumerate(QUESTOES):
        try:
            resposta_usuario = respostas_usuario[indice]
        except IndexError:
            resposta_usuario = -1

        resposta_correta = questao["resposta_correta"]
        acertou = resposta_usuario == resposta_correta

        if acertou:
            pontuacao += int(questao.get("valor", 1))

        detalhes.append(
            {
                "questao": indice + 1,
                "resposta_usuario": (
                    questao["opcoes"][resposta_usuario]
                    if 0 <= resposta_usuario < len(questao["opcoes"]) else "Inválida"
                ),
                "resposta_correta": questao["opcoes"][resposta_correta],
                "acertou": acertou,
            }
        )

    return pontuacao, detalhes


def imprimir_questoes() -> None:
    """Imprime todas as questões com suas opções."""
    for i, q in enumerate(QUESTOES, start=1):
        print(f"{i}. {q['pergunta']}")
        for idx, op in enumerate(q["opcoes"], start=1):
            print(f"   {idx}) {op}")
        print()


def coletar_respostas() -> List[int]:
    """
    Lê as respostas do usuário via input() e retorna uma lista de índices (0-based).
    """
    respostas: List[int] = []
    for i, q in enumerate(QUESTOES):
        max_opcoes = len(q["opcoes"])
        prompt = f"Digite o número da resposta para a questão {i+1} (1-{max_opcoes}): "
        while True:
            try:
                entrada = input(prompt).strip()
                resposta = int(entrada) - 1
                if 0 <= resposta < max_opcoes:
                    respostas.append(resposta)
                    break
                print(f"Por favor, digite um número entre 1 e {max_opcoes}.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
            except (KeyboardInterrupt, EOFError):
                print("\nEntrada interrompida. Encerrando quiz.")
                raise
    return respostas


def imprimir_resultado(pontuacao: int, detalhes: List[Dict[str, object]]) -> None:
    separador = "=" * 50
    print(f"\n{separador}")
    print(f"Pontuação Final: {pontuacao}/{len(QUESTOES)}")
    print(f"{separador}\n")

    for detalhe in detalhes:
        status = "✓ CORRETO" if detalhe["acertou"] else "✗ INCORRETO"
        print(f"Questão {detalhe['questao']}: {status}")
        print(f"  Sua resposta: {detalhe['resposta_usuario']}")
        print(f"  Resposta correta: {detalhe['resposta_correta']}\n")


def main() -> None:
    imprimir_questoes()
    try:
        respostas = coletar_respostas()
    except (KeyboardInterrupt, EOFError):
        return

    pontuacao, detalhes = calcular_pontuacao(respostas)
    imprimir_resultado(pontuacao, detalhes)


if __name__ == "__main__":
    main()
