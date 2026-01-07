# dio_quis

Quiz simples sobre capitais do mundo — código em Python.

**Resumo**
- Módulo principal: `dio_quis.is_quis_` (contém `main()` para executar o quiz interativo).
- Testes: `dio_quis.test_is_quis_` (pytest).

**Requisitos**
- Python 3.10+ (recomendado 3.11+; teste aqui em 3.14).

**Instalação (recomendado: virtualenv)**

1. Criar e ativar virtualenv (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Atualizar pip e instalar dependências para testes:

```powershell
python -m pip install --upgrade pip
pip install pytest
```

> Observação: se ao instalar pip emitir aviso sobre scripts em uma pasta que não está no `PATH`, prefira sempre executar o pytest via `python -m pytest`.

**Executar testes**

- Rodar todos os testes:

```powershell
python -m pytest -q
```

- Rodar apenas o pacote `dio_quis` tests:

```powershell
python -m pytest dio_quis -q
```

**Executar o quiz (programa)**

- Executar diretamente o módulo (recomendado):

```powershell
python -m dio_quis.is_quis_
```

- Ou executar o arquivo:

```powershell
python dio_quis\is_quis_.py
```

**Notas de boas práticas**
- Mantenha o ambiente virtual ativo ao trabalhar no projeto.
- Use `python -m pytest` para evitar problemas com PATH.
- Para desenvolvimento iterativo, execute `pytest -q` com `-k` para filtrar testes.

**Problemas comuns**
- Aviso: "scripts are installed in '...\AppData\Roaming\Python\...' which is not on PATH" — não é erro. Use `python -m pytest` ou adicione a pasta ao `PATH` se preferir rodar `pytest` diretamente.

**Licença**
- Uso livre para fins educativos e demonstração.
