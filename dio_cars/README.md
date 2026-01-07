DIO Cars — Exemplo MVC em Flask

Descrição
- Projeto de exemplo que mostra uma tabela chamada "DIO Cars" com 5 carros fixos.
- Cada linha mostra valor, ano e marca. A última coluna tem um botão que exibe uma mensagem: "voce selecionou o carro (NOME_DO_CARRO)".

Tecnologias
- Python 3.14+ (testado aqui)
- Flask 2.2.5

Como executar (PowerShell):

```powershell
python -m pip install -r dio_cars/requirements.txt
python dio_cars/app.py
```

Abra no navegador: http://127.0.0.1:5000

Observações
- Caso veja um aviso sobre `flask.exe` não estar no PATH, pode executar com `python dio_cars/app.py` sem problemas.
- Foi adicionado um pequeno "shim" em `dio_cars/app.py` para compatibilidade com mudanças em `pkgutil` no Python 3.14; para uma solução mais limpa, use Python 3.11.

Arquivos principais
- [dio_cars/app.py](dio_cars/app.py)
- [dio_cars/models.py](dio_cars/models.py)
- [dio_cars/templates/index.html](dio_cars/templates/index.html)

Prompt usado para gerar a página

> "vamos criar um projeto python simples que exiba no \"localhost/\" uma tabela chamada \"DIO Cars\" com colunas o valor, ano e marca de 5 carros (pode escolher e deixar fixo no código) sendo a ultima coluna com um botão que ao ser clicado exiba uma mensagem \"voce selecionou o carro (carro selecionaro) \" utilizando MVC"
