# Computação Distribuída — Exercícios 1.1 e 1.2

Atividade da disciplina de **Computação Distribuída** da Universidade de Fortaleza (UNIFOR).

## Exercício 1.1 — Disponibilidade de Serviço Replicado

O objetivo é calcular a disponibilidade de um serviço replicado em múltiplos servidores.

São considerados os seguintes parâmetros:

- `n`: número total de servidores;
- `k`: número mínimo de servidores disponíveis necessário para o serviço operar;
- `p`: probabilidade de cada servidor estar disponível.

Considerando que os servidores possuem disponibilidades independentes, a disponibilidade do serviço é calculada pela distribuição binomial:

A(n,k,p) = Σ C(n,i) × p^i × (1-p)^(n-i), para i = k até n.

### Casos específicos

Quando apenas um servidor precisa estar disponível (`k = 1`):

A(n,1,p) = 1 - (1-p)^n

Quando todos os servidores precisam estar disponíveis (`k = n`):

A(n,n,p) = p^n

A implementação está disponível em:

`exercicio_1_1.py`

## Exercício 1.2 — Cálculo Analítico e Simulação Estocástica

O exercício compara a disponibilidade calculada matematicamente com os resultados obtidos através de uma simulação estocástica.

Para cada combinação de `n`, `k` e `p`, são realizadas várias rodadas de simulação.

Em cada rodada:

1. É determinada aleatoriamente a disponibilidade de cada servidor;
2. É contado o número de servidores disponíveis;
3. O serviço é considerado operacional quando pelo menos `k` servidores estão disponíveis;
4. A disponibilidade experimental é calculada pela proporção de rodadas bem-sucedidas.

São comparados os casos:

- `k = 1`;
- `k = n/2`;
- `k = n`.

Os resultados analíticos e experimentais são apresentados lado a lado e visualizados através de gráficos 2D.

A implementação está disponível em:

`exercicio_1_2.py`

## Tecnologias utilizadas

- Python 3
- Matplotlib
- Biblioteca `math`
- Biblioteca `random`

## Como executar

Clone o repositório:

```bash
git clone https://github.com/gisele-siqueira/computacao-distribuida-exercicio1.git
