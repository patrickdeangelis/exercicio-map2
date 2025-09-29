# Refatoração: Classe Funcionario

Este projeto contém um código Python que precisa ser refatorado. A classe `Funcionario` atualmente viola o princípio da responsabilidade única.

## Estrutura do Projeto

```
src/
  funcionario.py      # Código original com problemas de design
  test_funcionario.py # Testes para validar o comportamento
```

## Como Executar

**Importante:** Todos os comandos devem ser executados a partir do diretório raiz do projeto (onde está o arquivo `README.md`).

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o código principal
```bash
python src/funcionario.py
```

### 3. Executar os testes
```bash
python -m pytest src/test_funcionario.py
```

### 4. Executar testes com cobertura
```bash
python -m pytest src/test_funcionario.py -v
```

## Objetivo

O objetivo é refatorar o código seguindo os princípios SOLID, especialmente o **Princípio da Responsabilidade Única (SRP)**.

A classe `Funcionario` atualmente tem múltiplas responsabilidades que devem ser separadas em classes diferentes.
