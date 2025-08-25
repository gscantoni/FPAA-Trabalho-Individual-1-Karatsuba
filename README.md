# Implementação do Algoritmo de Karatsuba (Python)

> **Trabalho Individual 1 — Fundamentos de Projeto e Análise de Algoritmos (Engenharia de Software).**  
> Este repositório contém a implementação do algoritmo de Karatsuba conforme solicitado no enunciado do professor.

---

## 🔍 Descrição do projeto

Este projeto implementa o algoritmo de **Karatsuba** para multiplicação eficiente de inteiros grandes.  
Diferente da multiplicação “escolar” (que utiliza 4 multiplicações recursivas ao dividir os operandos), Karatsuba reduz para **apenas 3 multiplicações recursivas**, obtendo uma complexidade menor:

T(n) ∈ O(n^{log2 3}) ≈ O(n^{1.585})

---

## ⚙️ Lógica do algoritmo (linha a linha do `karatsuba`)

```python
def karatsuba(x: int, y: int) -> int:
    sign = -1 if (x < 0) ^ (y < 0) else 1
    a, b = abs(x), abs(y)
    if a == 0 or b == 0:
        return 0
    if a < 10 and b < 10:
        return sign * (a * b)
    n = max(len(str(a)), len(str(b)))
    m = n // 2
    base = 10 ** m
    a_high, a_low = divmod(a, base)
    b_high, b_low = divmod(b, base)
    z2 = karatsuba(a_high, b_high)
    z0 = karatsuba(a_low, b_low)
    z1 = karatsuba(a_high + a_low, b_high + b_low) - z2 - z0
    result = (z2 * (10 ** (2 * m))) + (z1 * (10 ** m)) + z0
    return sign * result
```

### Explicação passo a passo
1. Sinal  
2. Casos-base  
3. Divisão  
4. Split  
5. Recursão (3 multiplicações)  
6. Combinação  

---

## ▶️ Como executar

```bash
python main.py 123456789 987654321
python main.py 123456789 987654321 --verify
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 📊 Relatório técnico

### Complexidade assintótica
- Relação: T(n) = 3T(n/2) + O(n)
- Tempo: Θ(n^{log2 3}) ≈ Θ(n^{1.585})
- Espaço: O(log n) recursão, O(n) para operações
- Casos: melhor O(1), pior/médio O(n^{1.585})

### Complexidade ciclomática
Decisões: 2  
M = decisões + 1 = 3  
Via grafo: N=10, E=11, P=1 → M=3

### Fluxo de controle (Mermaid)
```mermaid
flowchart TD
    A[Start] --> B{a==0 or b==0?}
    B -- sim --> C[return 0]
    B -- não --> D{a<10 and b<10?}
    D -- sim --> E[return sign*(a*b)]
    D -- não --> F[calcula n,m,base]
    F --> G[split partes]
    G --> H[z2,z0,z1 recursivos]
    H --> I[combina result]
    C --> J[End]
    E --> J
    I --> J
```

---

## 🧪 Validação

- `--verify` faz testes internos  
- `unittest` cobre números pequenos, aleatórios e grandes  

---

## 📁 Estrutura

```
.
├── main.py
├── README.md
└── tests/
    └── test_karatsuba.py
```

---

## 📎 Referências

- Karatsuba (1962)  
- Cormen et al., Introduction to Algorithms
