# Otimização de Shows com Busca Tabu

Atividade da disciplina de **Computação Evolucionária** - Otimização usando algoritmo de Busca Tabu para resolver o problema de seleção de shows da Maria.

## Problema

Maria ganhou milhas grátis para passagens em 2026 e decidiu investir indo ao máximo de shows que conseguir. No entanto, ela tem apenas R$ 3.000 para gastar com ingressos. O objetivo é maximizar o número de shows considerando seu gosto pessoal.

## Estrutura do Projeto

```
Tabu/
├── problemaA.py          # Resolve questão (a) - problema original vs. com restrição
├── problemaB.py          # Resolve questão (b) - teste de diferentes parâmetros
├── TS/                   # Implementação da Busca Tabu
│   ├── TS.py            # Algoritmo principal
│   └── stoch_optim_utilities.py  # Funções auxiliares
├── requirements.txt      # Dependências
└── README.md            # Este arquivo
```

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução

### Problema A - Comparação com/sem restrição
```bash
python3 problemaA.py
```

### Problema B - Teste de parâmetros
```bash
python3 problemaB.py
```

## Dados do Problema

- **Orçamento:** R$ 3.000
- **16 artistas** com preços e valores de gosto diferentes
- **Objetivo:** Maximizar número de shows + valor de gosto

## Algoritmo

Utiliza **Busca Tabu** (Tabu Search) para resolver o problema de otimização combinatória, tratando-o como um problema da mochila onde queremos maximizar tanto a quantidade quanto a qualidade dos shows selecionados.

## Resultados

O algoritmo encontra soluções que maximizam o número de shows respeitando o orçamento, priorizando artistas com melhor relação custo-benefício.