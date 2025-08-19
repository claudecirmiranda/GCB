```
=== Run information ===

Scheme:       weka.associations.Apriori -N 10 -T 0 -C 0.9 -D 0.05 -U 1.0 -M 0.1 -S -1.0 -c -1
Relation:     veiculos
Instances:    47
Attributes:   3
              idade
              renda
              carro
=== Associator model (full training set) ===


Apriori
=======

Minimum support: 0.1 (5 instances)
Minimum metric <confidence>: 0.9
Number of cycles performed: 18

Generated sets of large itemsets:

Size of set of large itemsets L(1): 6

Size of set of large itemsets L(2): 11

Size of set of large itemsets L(3): 4

Best rules found:

 1. idade=18-40 renda=0-8k 18 ==> carro=NACIONAL 18    <conf:(1)> lift:(1.68) lev:(0.15) [7] conv:(7.28)
 2. idade=18-40 carro=IMPORTADO 8 ==> renda=>8k 8    <conf:(1)> lift:(2.04) lev:(0.09) [4] conv:(4.09)
 3. renda=0-8k carro=NACIONAL 20 ==> idade=18-40 18    <conf:(0.9)> lift:(1.36) lev:(0.1) [4] conv:(2.27)


```

Resultado resumido
---------------------

*   **Dataset**: `veiculos`
    
*   **Instâncias**: 47
    
*   **Atributos**: `idade`, `renda`, `carro`
    
*   **Configuração**:
    *   Suporte mínimo: **0.1** (ou seja, pelo menos 10% dos registros, ~5 instâncias).
        
    *   Confiança mínima: **0.9** (90%).
        
    *   Máximo de regras: 10.
        

* * *

Regras Geradas
-----------------

### Regra 1

`idade=18-40 renda=0-8k 18 ==> carro=NACIONAL 18     conf:(1) lift:(1.68) lev:(0.15) [7] conv:(7.28)`

**Interpretação:**
*   Sempre que a pessoa tem **idade entre 18–40** e **renda de até 8k**, ela possui **carro nacional**.
    
*   **Confiança 1 (100%)**: não houve nenhuma exceção no dataset.
    
*   **Suporte 18/47 ≈ 38%**: aparece em 18 instâncias.
    
*   **Lift 1.68**: a chance de alguém ter carro nacional aumenta **68%** se a pessoa tiver idade 18–40 e renda até 8k.
    

* * *

### Regra 2

`idade=18-40 carro=IMPORTADO 8 ==> renda=>8k 8     conf:(1) lift:(2.04) lev:(0.09) [4] conv:(4.09)`

**Interpretação:**
*   Pessoas de **18–40 anos com carro importado** sempre têm **renda maior que 8k**.
    
*   **Confiança 1 (100%)**.
    
*   **Suporte 8/47 ≈ 17%**.
    
*   **Lift 2.04**: probabilidade de renda > 8k dobra quando a pessoa tem carro importado.
    

* * *

### Regra 3

`renda=0-8k carro=NACIONAL 20 ==> idade=18-40 18     conf:(0.9) lift:(1.36) lev:(0.1) [4] conv:(2.27)`

**Interpretação:**
*   Pessoas com **renda até 8k e carro nacional** são **90% das vezes jovens (18–40 anos)**.
    
*   **Suporte 20/47 ≈ 42%** (20 instâncias).
    
*   **Confiança 0.9 (90%)**: há algumas exceções (2 instâncias).
    
*   **Lift 1.36**: aumenta em 36% a chance de ser jovem nesse grupo.
    

* * *

Como usar essas regras
-------------------------

Essas regras de associação ajudam a entender **padrões de perfil**:
*   Pessoas jovens com baixa renda → **carros nacionais**.
    
*   Jovens com carro importado → **renda alta**.
    
*   Renda baixa + carro nacional → geralmente jovens.
    
Isso pode ser aplicado em:
*   **Segmentação de clientes** (marketing automotivo).
    
*   **Modelagem de crédito** (perfil de risco de financiamento).
    
*   **Estudos de mercado** (estratégias de venda por faixa etária e renda).
