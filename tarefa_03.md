Desafio: Construção de um Algoritmo Genético Próprio
====================================================

O desafio é **construir um algoritmo genético** para resolver um problema específico:
👉 Encontrar o **menor caminho que leva um rato até um pedaço de queijo** dentro de uma sala mapeada.
O algoritmo deve permitir implementar todas as suas partes e operadores, além de exigir escolhas sobre os valores dos parâmetros livres.

* * *

🎯 Objetivo Principal do Algoritmo Genético
-------------------------------------------

*   Encontrar o **menor caminho do rato até o queijo** dentro da sala.
    
*   O algoritmo deve implementar todas as etapas do AG (população inicial, avaliação, seleção, cruzamento, mutação e elitismo).
    

* * *

🗺️ Cenário do Problema (Espaço de Busca)
-----------------------------------------

*   Sala inicialmente de **10x10 metros (100m²)**.
    
*   Pode ser expandida para **50x50 metros (2500m²)** para aumentar a complexidade.
    
*   O **rato** é colocado em qualquer linha da **primeira coluna** (lado esquerdo).
    
*   O **queijo** é colocado em qualquer linha da **última coluna** (lado direito).
    
*   O custo do caminho é contabilizado **metro a metro**.
    

* * *

🐭 Regras de Movimentação do Rato
---------------------------------

*   O rato **não anda na diagonal** e **não anda para trás**.
    
*   Sempre dá **1 metro para frente** antes de decidir o próximo movimento.
    
*   Pode se mover:
    *   para a esquerda,
        
    *   para a direita,
        
    *   ou continuar em linha reta.
        
*   Todas as rotas começam na posição inicial e terminam no queijo (não podem ser alteradas).
    

* * *

🧬 Codificação do Cromossomo
----------------------------

*   Cada cromossomo é um **vetor de inteiros**:
    *   **10 posições** para o caso **10x10**,
        
    *   **50 posições** para o caso **50x50**.
        
*   Estrutura:
    *   **posição 0** = linha inicial do rato,
        
    *   **última posição** = linha do queijo.
        
*   Genes variam entre:
    *   **0 a 9** no grid 10x10,
        
    *   **0 a 49** no grid 50x50.
        
*   População inicial deve garantir **valores válidos**.
    
*   As **colunas não precisam ser modeladas**, pois a posição no vetor já define a coluna.
    

* * *

📊 Função de Aptidão (Fitness Function)
---------------------------------------

*   O custo da rota depende apenas da distância percorrida.
    
*   **Não há obstáculos** na sala.
    
*   Fórmula do custo parcial entre duas linhas:
    
$$Custo(i,i+1)=1+∣Y(i+1)−Y(i)∣Custo(i, i+1) = 1 + |Y(i+1) - Y(i)|Custo(i,i+1)=1+∣Y(i+1)−Y(i)∣$$
*   O **custo total** é:
    
$$Custo=∑(1+∣Y(i+1)−Y(i)∣)Custo = \sum (1 + |Y(i+1) - Y(i)|)Custo=∑(1+∣Y(i+1)−Y(i)∣)$$
*   Exemplo: mover da **linha 4** para a **linha 7** → custo = 1 (frente) + 3 (diferença entre linhas) = **4 metros**.
    

* * *

⚙️ Operadores Genéticos
-----------------------

*   **Seleção:** método a escolher (roleta, torneio etc.).
    
*   **Cruzamento:** definir ponto(s) de corte.
    
*   **Mutação:** alterar valores aleatórios dentro do domínio permitido.
    
*   **Elitismo:** refletir se indivíduos de melhor desempenho devem ser preservados.
    

* * *

⏹️ Critério de Parada
---------------------

*   A **solução ótima é conhecida**: linha reta entre origem e destino.
    
*   Custos ótimos no caso **10x10**:
    *   Mesmo nível (mesma linha): **9 metros**.
        
    *   Diferentes linhas: **|destino - origem| + 9 metros**.
        
*   Recomenda-se:
    *   **valor ótimo da função**, ou
        
    *   **número fixo de gerações** como critério de parada.
        

* * *

🔧 Parâmetros Livres e Recomendações
------------------------------------

*   Tamanho da população: **500, 1000 ou até 5000 cromossomos**.
    
*   Taxa de cruzamento.
    
*   Taxa de mutação.
    
*   Operadores de seleção, cruzamento e mutação.
    
*   Possibilidade de **mudar posições do rato e do queijo**.
    
*   Exibir:
    *   melhor cromossomo,
        
    *   geração em que o algoritmo parou.
        
*   Executar múltiplas vezes para analisar variação.
    
*   Opcional: visualizar **top 5 melhores cromossomos**.
    

* * *

📈 Análise e Consolidação do Conhecimento
-----------------------------------------

*   Observar a melhor solução encontrada e outras boas soluções.
    
*   Comparar similaridades entre cromossomos de alta performance.
    
*   Avaliar proximidade entre valores da função objetivo.
    
*   Fazer análise crítica considerando a teoria de AGs.
    
*   Refletir sobre o impacto da **aleatoriedade inicial** no tempo até a solução.
    

* * *

✅ Resumo
--------

O desafio é implementar **um algoritmo genético completo** que encontre o **menor caminho em um grid**.  
Será necessário aplicar conceitos de **codificação, função de aptidão e operadores genéticos**, além de realizar **análises críticas** dos resultados e da convergência da solução.

## Ga – Menor Caminho Do Rato Até O Queijo (10x10 Ou 50x50) – Código Python

```PYTHON
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algoritmo Genético para encontrar o menor caminho (em custo) que leva um rato
até um queijo em um grid N x N (N=10 ou 50, mas funciona para qualquer N>=2).

Modelagem (conforme enunciado):
- Cada cromossomo é um vetor de tamanho N, onde o índice i representa a coluna i.
- O valor do gene Y[i] é a linha (0..N-1) ocupada quando o rato está na coluna i.
- Y[0] (posição inicial) e Y[N-1] (posição do queijo) são fixos.
- O custo entre colunas consecutivas i -> i+1 é: 1 (frente) + |Y[i+1] - Y[i]| (deslocamento lateral).
- Custo total da rota: sum_{i=0..N-2} (1 + |Y[i+1] - Y[i]|).
- Ótimo teórico: (N-1) + |Y[N-1] - Y[0]|.

Recursos implementados:
- Geração de população inicial factível.
- 3 métodos de seleção: tournament, roulette, rank.
- 3 métodos de cruzamento: one_point, two_point, uniform (respeitando Y[0] e Y[-1] fixos).
- 2 mutações: reset (atribui novo valor aleatório) e creep (variação incremental ±step com clamp).
- Elitismo configurável.
- Critérios de parada: atingir o custo ótimo OU alcançar o máximo de gerações.
- Execução múltipla (para análise de variabilidade), registro do melhor por geração, e exportação opcional.
- Visualização opcional do melhor caminho via matplotlib.

Uso rápido:
    python ga_rato_queijo.py --N 10 --start 4 --goal 7 \
        --pop 1000 --cx 0.9 --mut 0.15 --sel tournament --cxop one_point \
        --mutop creep --elit 0.05 --max_gens 500 --seed 42 --plot best.png

Múltiplas execuções (p/ estatística):
    python ga_rato_queijo.py --runs 10 --N 50 --start 3 --goal 18

Saídas principais no console:
- Melhor cromossomo, custo, geração de parada, se atingiu o ótimo, top-K caminhos.

Autor: Claudecir Miranda
"""
from __future__ import annotations
from dataclasses import dataclass
import argparse
import math
import random
from typing import Callable, List, Tuple, Optional, Sequence

try:
    import numpy as np
except ImportError:  # numpy é opcional; o código não depende dela.
    np = None  # type: ignore

# ===============================
# Utilitários do problema
# ===============================

def path_cost(path: Sequence[int]) -> int:
    """Calcula o custo total da rota: Σ (1 + |Y[i+1]-Y[i]|).
    Assume len(path) >= 2.
    """
    total = 0
    for i in range(len(path) - 1):
        total += 1 + abs(path[i + 1] - path[i])
    return total


def optimal_cost(path: Sequence[int]) -> int:
    """Custo ótimo teórico: (N-1) + |dest - origem|.
    Usa apenas os extremos de `path` para calcular.
    """
    N = len(path)
    return (N - 1) + abs(path[-1] - path[0])


# ===============================
# Parâmetros do GA
# ===============================

@dataclass
class GAParams:
    N: int = 10  # grid N x N
    start: Optional[int] = None  # linha inicial (0..N-1)
    goal: Optional[int] = None   # linha final (0..N-1)
    pop_size: int = 1000
    crossover_rate: float = 0.9
    mutation_rate: float = 0.15  # probabilidade de mutação por gene (entre colunas 1..N-2)
    selection: str = "tournament"  # "tournament" | "roulette" | "rank"
    tournament_k: int = 3
    crossover_op: str = "one_point"  # "one_point" | "two_point" | "uniform"
    mutation_op: str = "creep"  # "reset" | "creep"
    creep_step: int = 1  # tamanho do passo do creep (±step)
    elitism_rate: float = 0.05  # fração de elite preservada (0..0.2 recomendado)
    max_generations: int = 1000
    seed: Optional[int] = None
    top_k: int = 5  # quantos melhores exibir ao final

    # Critério extra (opcional): parar se não houver melhora por tantas gerações (0 = desabilitado)
    stall_generations: int = 0


# ===============================
# Núcleo do GA
# ===============================

class GeneticMouseCheese:
    def __init__(self, params: GAParams):
        assert params.N >= 2
        self.p = params
        if self.p.seed is not None:
            random.seed(self.p.seed)
            if np is not None:
                np.random.seed(self.p.seed)
        # Trata start/goal
        self.start = self.p.start if self.p.start is not None else random.randrange(self.p.N)
        self.goal = self.p.goal if self.p.goal is not None else random.randrange(self.p.N)
        # Tamanhos derivados
        self.N = self.p.N
        self.valid_rows = range(self.N)
        # Ajusta elite absoluto
        self.elite_size = max(1, int(round(self.p.elitism_rate * self.p.pop_size)))
        # Índices mutáveis (entre colunas 1..N-2)
        self.mutable_idx = list(range(1, self.N - 1))

    # ---------- População inicial ----------
    def _random_chromosome(self) -> List[int]:
        chrom = [0] * self.N
        chrom[0] = self.start
        chrom[-1] = self.goal
        for i in self.mutable_idx:
            chrom[i] = random.randrange(self.N)
        return chrom

    def _init_population(self) -> List[List[int]]:
        return [self._random_chromosome() for _ in range(self.p.pop_size)]

    # ---------- Avaliação ----------
    def evaluate(self, population: List[List[int]]) -> List[int]:
        return [path_cost(ch) for ch in population]

    # ---------- Seleção ----------
    def _select(self, population: List[List[int]], costs: List[int]) -> List[int]:
        sel = self.p.selection
        if sel == "tournament":
            return self._tournament_select(costs)
        elif sel == "roulette":
            return self._roulette_select(costs)
        elif sel == "rank":
            return self._rank_select(costs)
        else:
            raise ValueError(f"Seleção desconhecida: {sel}")

    def _tournament_select(self, costs: List[int]) -> List[int]:
        idx = list(range(len(costs)))
        parents = []
        for _ in range(len(costs)):
            contenders = random.sample(idx, k=min(self.p.tournament_k, len(idx)))
            # minimização: menor custo vence
            winner = min(contenders, key=lambda i: costs[i])
            parents.append(winner)
        return parents

    def _roulette_select(self, costs: List[int]) -> List[int]:
        # Minimização: converte custo em aptidão maior-melhor.
        # Usamos score = 1/(1+cost). Evita negativos e divisão por zero.
        scores = [1.0 / (1.0 + c) for c in costs]
        ssum = sum(scores)
        if ssum == 0:
            probs = [1.0 / len(scores)] * len(scores)
        else:
            probs = [s / ssum for s in scores]
        # Gera |pop| pais por amostragem com reposição
        cum = []
        acc = 0.0
        for p in probs:
            acc += p
            cum.append(acc)
        rands = [random.random() for _ in range(len(costs))]
        parents = []
        for r in rands:
            # busca linear (populações grandes: trocar por bisect)
            j = 0
            while j < len(cum) and r > cum[j]:
                j += 1
            parents.append(min(j, len(costs) - 1))
        return parents

    def _rank_select(self, costs: List[int]) -> List[int]:
        # Rank: classifica por custo crescente e atribui probabilidade linear ao rank
        sorted_idx = sorted(range(len(costs)), key=lambda i: costs[i])
        ranks = [0] * len(costs)
        for r, i in enumerate(sorted_idx):
            ranks[i] = r + 1  # 1..n
        ssum = len(costs) * (len(costs) + 1) / 2
        probs = [rank / ssum for rank in ranks]  # melhor (rank alto) maior prob.
        # amostragem
        cum = []
        acc = 0.0
        for p in probs:
            acc += p
            cum.append(acc)
        parents = []
        for _ in range(len(costs)):
            r = random.random()
            j = 0
            while j < len(cum) and r > cum[j]:
                j += 1
            parents.append(min(j, len(costs) - 1))
        return parents

    # ---------- Cruzamento ----------
    def _crossover_pair(self, p1: List[int], p2: List[int]) -> Tuple[List[int], List[int]]:
        if random.random() > self.p.crossover_rate or len(self.mutable_idx) == 0:
            return p1[:], p2[:]
        op = self.p.crossover_op
        if op == "one_point":
            cut = random.choice(self.mutable_idx)
            c1 = p1[:cut] + p2[cut:]
            c2 = p2[:cut] + p1[cut:]
        elif op == "two_point":
            a, b = sorted(random.sample(self.mutable_idx, k=min(2, len(self.mutable_idx))))
            c1 = p1[:a] + p2[a:b] + p1[b:]
            c2 = p2[:a] + p1[a:b] + p2[b:]
        elif op == "uniform":
            c1, c2 = p1[:], p2[:]
            for i in self.mutable_idx:
                if random.random() < 0.5:
                    c1[i], c2[i] = c2[i], c1[i]
        else:
            raise ValueError(f"Cruzamento desconhecido: {op}")
        # Garantir extremos
        c1[0], c1[-1] = self.start, self.goal
        c2[0], c2[-1] = self.start, self.goal
        return c1, c2

    # ---------- Mutação ----------
    def _mutate(self, chrom: List[int]) -> None:
        if self.p.mutation_rate <= 0 or len(self.mutable_idx) == 0:
            return
        if self.p.mutation_op == "reset":
            for i in self.mutable_idx:
                if random.random() < self.p.mutation_rate:
                    chrom[i] = random.randrange(self.N)
        elif self.p.mutation_op == "creep":
            step = max(1, int(self.p.creep_step))
            for i in self.mutable_idx:
                if random.random() < self.p.mutation_rate:
                    delta = random.randint(-step, step)
                    chrom[i] = max(0, min(self.N - 1, chrom[i] + delta))
        else:
            raise ValueError(f"Mutação desconhecida: {self.p.mutation_op}")
        # extremos permanecem fixos
        chrom[0], chrom[-1] = self.start, self.goal

    # ---------- Loop evolutivo ----------
    def run(self) -> dict:
        population = self._init_population()
        costs = self.evaluate(population)
        best_idx = min(range(len(costs)), key=lambda i: costs[i])
        best = population[best_idx][:]
        best_cost = costs[best_idx]
        best_hist = [best_cost]
        opt = optimal_cost(best)
        stall_left = self.p.stall_generations if self.p.stall_generations > 0 else None

        gen = 0
        while gen < self.p.max_generations and best_cost > opt:
            gen += 1
            # Seleção
            parent_idx = self._select(population, costs)
            parents = [population[i] for i in parent_idx]
            # Cruzamento (em pares)
            next_pop: List[List[int]] = []
            for i in range(0, len(parents), 2):
                p1 = parents[i]
                p2 = parents[i + 1] if i + 1 < len(parents) else parents[0]
                c1, c2 = self._crossover_pair(p1, p2)
                next_pop.append(c1)
                if len(next_pop) < self.p.pop_size:
                    next_pop.append(c2)
            # Mutação
            for indiv in next_pop:
                self._mutate(indiv)
            # Elitismo: injeta melhores anteriores
            elite_idx = sorted(range(len(costs)), key=lambda i: costs[i])[: self.elite_size]
            elites = [population[i][:] for i in elite_idx]
            # Avalia nova população
            population = next_pop
            costs = self.evaluate(population)
            # Substitui piores por elites (garante preservação)
            worst_idx = sorted(range(len(costs)), key=lambda i: costs[i], reverse=True)[: self.elite_size]
            for e, w in zip(elites, worst_idx):
                population[w] = e
                costs[w] = path_cost(e)
            # Atualiza best
            cur_idx = min(range(len(costs)), key=lambda i: costs[i])
            cur_best = population[cur_idx]
            cur_cost = costs[cur_idx]
            if cur_cost < best_cost:
                best, best_cost = cur_best[:], cur_cost
                # reset stall
                if stall_left is not None:
                    stall_left = self.p.stall_generations
            else:
                if stall_left is not None:
                    stall_left -= 1
            best_hist.append(best_cost)
            if stall_left is not None and stall_left <= 0:
                break
        # Coleta top-K
        sorted_idx = sorted(range(len(costs)), key=lambda i: costs[i])
        top_k = [(population[i][:], costs[i]) for i in sorted_idx[: self.p.top_k]]
        return {
            "best_path": best,
            "best_cost": best_cost,
            "optimal_cost": opt,
            "reached_optimum": best_cost == opt,
            "generations": gen,
            "history": best_hist,
            "top_k": top_k,
            "start": self.start,
            "goal": self.goal,
            "N": self.N,
            "params": self.p,
        }

    # ---------- Visualização ----------
    def plot_path(self, path: Sequence[int], save: Optional[str] = None):
        try:
            import matplotlib.pyplot as plt
        except Exception as e:
            print("matplotlib não disponível para plotar:", e)
            return
        N = len(path)
        xs = list(range(N))
        ys = list(path)
        plt.figure()
        plt.plot(xs, ys, marker='o')  # não define cores explicitamente
        plt.title(f"Melhor caminho – custo={path_cost(path)} | ótimo={optimal_cost(path)}")
        plt.xlabel("Coluna (frente)")
        plt.ylabel("Linha")
        plt.grid(True)
        plt.gca().invert_yaxis()  # opcional: linha 0 no topo
        if save:
            plt.savefig(save, bbox_inches='tight')
        else:
            plt.show()


# ===============================
# Execução múltipla para análise
# ===============================

def run_multiple(params: GAParams, runs: int = 10, verbose: bool = True) -> dict:
    best_costs = []
    reached = 0
    gens = []
    best_of_all: Optional[Tuple[List[int], int]] = None
    for r in range(runs):
        # Variar seed se desejado mantendo base
        p = GAParams(**{**params.__dict__})
        if params.seed is not None:
            p.seed = params.seed + r
        ga = GeneticMouseCheese(p)
        res = ga.run()
        best_costs.append(res["best_cost"])
        gens.append(res["generations"])
        reached += 1 if res["reached_optimum"] else 0
        if best_of_all is None or res["best_cost"] < best_of_all[1]:
            best_of_all = (res["best_path"], res["best_cost"])  # type: ignore
        if verbose:
            print(f"Run {r+1}/{runs}: best_cost={res['best_cost']} | gens={res['generations']} | optimum={res['optimal_cost']} | reached={res['reached_optimum']}")
    stats = {
        "runs": runs,
        "avg_best_cost": sum(best_costs) / len(best_costs),
        "min_best_cost": min(best_costs),
        "max_best_cost": max(best_costs),
        "hit_rate": reached / runs,
        "avg_generations": sum(gens) / len(gens),
        "best_overall_path": best_of_all[0] if best_of_all else None,
        "best_overall_cost": best_of_all[1] if best_of_all else None,
    }
    return stats


# ===============================
# CLI
# ===============================

def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Algoritmo Genético – Rato e Queijo em grid N x N")
    ap.add_argument("--N", type=int, default=10, help="Tamanho do grid (N x N). Ex: 10 ou 50")
    ap.add_argument("--start", type=int, default=None, help="Linha inicial (0..N-1). Default: aleatório")
    ap.add_argument("--goal", type=int, default=None, help="Linha final (0..N-1). Default: aleatório")

    ap.add_argument("--pop", type=int, default=1000, help="Tamanho da população")
    ap.add_argument("--cx", type=float, default=0.9, help="Taxa de cruzamento (0..1)")
    ap.add_argument("--mut", type=float, default=0.15, help="Taxa de mutação por gene (0..1)")
    ap.add_argument("--sel", type=str, default="tournament", choices=["tournament", "roulette", "rank"], help="Operador de seleção")
    ap.add_argument("--tk", type=int, default=3, help="k do tournament (>=2)")
    ap.add_argument("--cxop", type=str, default="one_point", choices=["one_point", "two_point", "uniform"], help="Operador de cruzamento")
    ap.add_argument("--mutop", type=str, default="creep", choices=["reset", "creep"], help="Operador de mutação")
    ap.add_argument("--step", type=int, default=1, help="Passo do creep (±step)")
    ap.add_argument("--elit", type=float, default=0.05, help="Taxa de elitismo (fração 0..0.2)")
    ap.add_argument("--max_gens", type=int, default=1000, help="Máximo de gerações")
    ap.add_argument("--stall", type=int, default=0, help="Parar após X gerações sem melhora (0=desabilitado)")
    ap.add_argument("--seed", type=int, default=None, help="Seed de aleatoriedade")
    ap.add_argument("--runs", type=int, default=1, help="Número de execuções independentes")
    ap.add_argument("--topk", type=int, default=5, help="Mostrar top-K soluções ao final")
    ap.add_argument("--plot", type=str, default=None, help="Salvar imagem do melhor caminho (arquivo .png)")
    return ap.parse_args()


def main():
    args = parse_args()
    params = GAParams(
        N=args.N,
        start=args.start,
        goal=args.goal,
        pop_size=args.pop,
        crossover_rate=args.cx,
        mutation_rate=args.mut,
        selection=args.sel,
        tournament_k=args.tk,
        crossover_op=args.cxop,
        mutation_op=args.mutop,
        creep_step=args.step,
        elitism_rate=args.elit,
        max_generations=args.max_gens,
        seed=args.seed,
        top_k=args.topk,
        stall_generations=args.stall,
    )

    if args.runs > 1:
        stats = run_multiple(params, runs=args.runs, verbose=True)
        print("\nResumo múltiplas execuções:")
        for k, v in stats.items():
            print(f"  {k}: {v}")
        if args.plot and stats.get("best_overall_path") is not None:
            ga = GeneticMouseCheese(params)
            ga.plot_path(stats["best_overall_path"], save=args.plot)
    else:
        ga = GeneticMouseCheese(params)
        res = ga.run()
        print("Parâmetros:")
        print(f"  N={res['N']} | start={res['start']} | goal={res['goal']} | pop={params.pop_size}")
        print(f"  seleção={params.selection} | cruzamento={params.crossover_op} | mutação={params.mutation_op}")
        print(f"  cx={params.crossover_rate} | mut={params.mutation_rate} | elit={params.elitism_rate}")
        print("\nResultado:")
        print(f"  Ótimo teórico: {res['optimal_cost']}")
        print(f"  Melhor custo:   {res['best_cost']} (atingiu_ótimo={res['reached_optimum']})")
        print(f"  Gerações:       {res['generations']}")
        print(f"  Melhor caminho: {res['best_path']}")
        print("\nTop-K soluções:")
        for i, (path, cost) in enumerate(res["top_k"], 1):
            print(f"  {i:>2}. custo={cost:>4} | caminho={path}")
        if args.plot:
            ga.plot_path(res["best_path"], save=args.plot)
            print(f"Figura salva em: {args.plot}")


if __name__ == "__main__":
    main()

```

## Execução do código

```bash
python ga_rato_queijo.py --N 10 --start 4 --goal 7 --pop 1000 --cx 0.9 --mut 0.15 --sel tournament --cxop one_point --mutop creep --elit 0.05 --max_gens 500 --seed 42 --plot best.png

Parâmetros:
  N=10 | start=4 | goal=7 | pop=1000
  seleção=tournament | cruzamento=one_point | mutação=creep
  cx=0.9 | mut=0.15 | elit=0.05

Resultado:
  Ótimo teórico: 12
  Melhor custo:   12 (atingiu_ótimo=True)
  Gerações:       3
  Melhor caminho: [4, 4, 4, 4, 5, 6, 6, 6, 6, 7]

Top-K soluções:
   1. custo=  12 | caminho=[4, 4, 4, 4, 5, 6, 6, 6, 6, 7]
   2. custo=  12 | caminho=[4, 4, 6, 6, 6, 6, 6, 6, 6, 7]
   3. custo=  14 | caminho=[4, 4, 4, 4, 4, 5, 4, 4, 6, 7]
   4. custo=  14 | caminho=[4, 4, 5, 6, 5, 6, 6, 7, 7, 7]
   5. custo=  14 | caminho=[4, 4, 5, 4, 6, 6, 6, 6, 6, 7]
Figura salva em: best.png
```

<img width="567" height="455" alt="best" src="https://github.com/user-attachments/assets/4cc81249-4dc3-4a50-bcec-c1e49df5664c" />

## Análise dos Resultados

Obteve-se um excelente resultado, atingindo o **ótimo teórico** (12) em apenas **3 gerações**, o que mostra que os parâmetros escolhidos (população grande, alta taxa de cruzamento, mutação moderada e elitismo) favoreceram convergência rápida.  

Segue a análise consolidada:

* * *

🔎 Observação da melhor e boas soluções
---------------------------------------

*   **Melhor solução**: `[4, 4, 4, 4, 5, 6, 6, 6, 6, 7]`  
    Representa um caminho suave, com degraus bem distribuídos até chegar na linha 7.
    
*   **Outra ótima (mesmo custo)**: `[4, 4, 6, 6, 6, 6, 6, 6, 6, 7]`  
    Também chega no custo 12, mas dá um salto maior no início e depois segue reto.
    
*   **Boas soluções próximas**: custos 14, com variações que criam “zig-zags” desnecessários (ex.: subir e descer entre 5–6, ou manter linha 4 e só no final ajustar).
    

* * *

🧬 Comparação dos cromossomos
-----------------------------

*   As **duas soluções ótimas** (custo=12) têm **estrutura semelhante**:
    *   início fixo em 4,
        
    *   fim fixo em 7,
        
    *   transição suave de 4→7 ao longo das colunas,
        
    *   diferença principal está em **onde ocorre a subida** (distribuída ou concentrada).
        
*   As soluções **quase ótimas (custo=14)** são muito parecidas, mas incluem pequenos desvios (subidas/descidas extras), o que penaliza a função objetivo.
    
*   Isso mostra que o **espaço de busca contém múltiplos cromossomos equivalentes** em custo ótimo — há várias formas diferentes de obter a mesma distância mínima.
    

* * *

📊 Semelhança na função objetivo
--------------------------------

*   Diferença entre ótimas (12) e próximas (14) é **pequena**, mas suficiente para destacar como mutações ou cruzamentos ligeiramente mal posicionados podem gerar custo extra.
    
*   O GA conseguiu **discriminar rapidamente** entre custo ótimo e quase ótimo, convergindo em poucas gerações.
    

* * *

🧠 Análise crítica do GA
------------------------

1.  **Aleatoriedade inicial**:
    *   O fato de ter encontrado o ótimo em **3 gerações** mostra que já na população inicial apareceram cromossomos bem próximos do ótimo.
        
    *   Se a aleatoriedade inicial tivesse favorecido mais soluções ruins, o GA precisaria de mais gerações para “lapidar”.
        
2.  **Seleção por torneio**:
    *   Favorece soluções boas rapidamente, acelerando convergência.
        
    *   Mas em casos mais complexos (N=50, obstáculos), pode gerar **convergência prematura** se a diversidade não for mantida.
        
3.  **Mutação creep**:
    *   Boa escolha, pois permite ajustes suaves e evita oscilações bruscas (importante para caminhos mínimos).
        
4.  **Elitismo (5%)**:
    *   Garantiu preservação das melhores soluções, permitindo que não se perdesse o ótimo quando surgisse.
        
5.  **Multiplicidade de ótimos**:
    *   O problema tem várias soluções equivalentes (mesmo custo, caminhos diferentes).
        
    *   O GA explorou esse espaço, como mostra a existência de dois ótimos distintos no Top-K.
        

* * *

🌱 Reflexão sobre aleatoriedade e convergência
----------------------------------------------

*   **Com boa população inicial** → convergência rápida (como neste caso).
    
*   **Com população ruim** → pode levar dezenas de gerações, mas ainda assim o GA tende a encontrar o ótimo pela combinação de cruzamento + mutação.
    
*   Isso confirma uma característica dos algoritmos genéticos: **robustez frente a múltiplos pontos de partida**, ao custo de alguma variabilidade no tempo para convergir.
    

* * *

✅ **Conclusão**: O GA funcionou de forma eficiente, encontrou o ótimo em poucas gerações e mostrou que as melhores soluções têm cromossomos muito parecidos (transições suaves de 4→7). A aleatoriedade inicial impacta fortemente a velocidade, mas não impede a convergência.
