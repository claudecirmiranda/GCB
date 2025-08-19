**Título:** Research on the Performance of Supercritical H2 Cylindrical Seals Based on Multi-Objective Optimization Method of Spiral Groove Parameters

**Autores:** Xueliang Wang, Zegan Gao, Wei Zhang, Junjie Lu, Leibo Wu, e Min Jiang

**Publicação:**

• Postado: 4 de fevereiro de 2025

• Disponível em SSRN: https://ssrn.com/abstract=5123866

--------------------------------------------------------------------------------

a) Descrição do Problema, Variáveis/Restrições do Domínio e Modelagem da Função Objetivo

O problema central abordado neste trabalho é a **otimização da estrutura de vedações cilíndricas sem contato** para aumentar a eficiência e segurança em equipamentos de alta tecnologia, como as turbinas de hidrogênio. As turbinas a gás de hidrogênio são vitais para a energia limpa, mas enfrentam desafios técnicos consideráveis, especialmente no que tange à vedação sob condições operacionais severas, incluindo alta vibração, temperatura e pressão. As vedações cilíndricas são particularmente adequadas para essas condições devido à sua baixa taxa de vazamento, simplicidade estrutural e alta flexibilidade do sistema.

O cerne do problema de otimização reside no fato de que os parâmetros de desempenho das vedações cilíndricas — como capacidade de carga, taxa de vazamento e força de atrito — frequentemente se **restringem mutuamente**. Isso significa que otimizar uma métrica pode levar à deterioração de outra, caracterizando-o como um **típico problema de otimização multi-objetivo** que exige uma solução algorítmica. A pesquisa foca, portanto, na **análise da influência dos parâmetros das ranhuras espirais no desempenho da vedação** em um meio de hidrogênio e no projeto otimizado dessas ranhuras.

**Variáveis/Restrições do Domínio Consideradas:**

As variáveis independentes (ou de decisão) são os parâmetros geométricos das ranhuras espirais na vedação cilíndrica:

• **Profundidade da ranhura (x1):** Varia de 2 μm a 26 μm.

• **Comprimento da ranhura (x2):** Varia de 10 mm a 40 mm.

• **Número de ranhuras (x3):** Varia de 4 a 36.

• **Ângulo espiral (x4):** Varia de 15 a 75 graus, sendo a tangente do ângulo utilizada no modelo (0.2679 a 3.7320).

Além disso, o estudo considera duas condições operacionais distintas:

• **Condição Baixa:** Pressão de .4 MPa e Temperatura de 350 K.

• **Condição Alta:** Pressão de .8 MPa e Temperatura de 650 K. Outros parâmetros operacionais e estruturais fixos incluem: velocidade de rotação de 20.000 r/min, excentricidade de 0.6 e espessura média do filme de gás de 10 μm.

**Modelagem da Função Objetivo:**

As variáveis dependentes, que representam o desempenho da vedação, são:

• **Capacidade de carga do filme de gás (y1)**

• **Força de atrito (y2)**

• **Taxa de vazamento (y3)**

Para modelar a relação entre os parâmetros das ranhuras e o desempenho da vedação, foi estabelecido um **modelo de regressão não-linear multivariada**. Este modelo (Equação 5) expressa a relação entre as quatro variáveis de decisão (x1, x2, x3, x4) e as três variáveis de desempenho (y1, y2, y3). As equações de previsão de regressão foram ajustadas para ambas as condições de operação (baixa e alta), mostrando coeficientes de determinação (R²) e coeficientes de correlação ajustados (adjust_R²) muito próximos de 1, indicando boa precisão e credibilidade do modelo.

A função objetivo final do problema de otimização multi-objetivo visa:

• **Minimizar o vazamento (Q)**

• **Minimizar a força de atrito (f)**

• **Maximizar a capacidade de carga (F)**

Matematicamente, isso é expresso como **M-minG(x)=(-F(x),f(x),Q(x))**, onde -F(x) é usado para transformar a maximização da capacidade de carga em uma minimização para compatibilidade com o algoritmo.

--------------------------------------------------------------------------------

b) Identificação da Técnica Evolucionária Utilizada e Descrição dos Resultados Obtidos

**Técnica Evolucionária Utilizada:**

A técnica evolucionária empregada para a otimização multi-objetivo foi o **algoritmo NSGA-II (Non-dominated Sorting Genetic Algorithm II)**. Este algoritmo foi implementado na plataforma **PlatEMO**, um ambiente de software para otimização evolucionária multi-objetivo. Os parâmetros de execução do NSGA-II foram definidos como um **tamanho de população de 100 indivíduos e 200 iterações**, resultando na geração de um conjunto de soluções de Pareto.

Para a seleção da "melhor" solução a partir do conjunto de Pareto (que contém 100 conjuntos de populações), foram utilizados dois métodos de tomada de decisão, que auxiliam a lidar com a natureza conflitante dos múltiplos objetivos:

. **Método TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) Subjetivo:** Avalia as opções calculando a distância para as soluções ideais e não ideais, com coeficientes de peso definidos subjetivamente (proporções 3:6:1 e 4:4:2 para capacidade de carga:vazamento:atrito).

2. **Método TOPSIS com Peso de Entropia (Objetivo):** Este método determina os pesos de cada indicador de desempenho com base na dispersão dos dados, o que o torna um método objetivo, não dependente de intenções subjetivas humanas.

**Resultados Obtidos:**

Os principais resultados da otimização foram os seguintes:

• **Impacto dos Parâmetros:** As simulações numéricas e a otimização revelaram que a **profundidade da ranhura tem o impacto mais significativo no desempenho de vedação**, seguida pelo comprimento da ranhura. Os efeitos do ângulo espiral e do número de ranhuras são relativamente menores.

• **Modelo de Regressão:** O modelo de regressão não-linear estabelecido demonstrou uma **excelente capacidade preditiva** (R² e adjust_R² próximos de 1), o que permite substituir simulações numéricas complexas e demoradas.

• **Desempenho Geral Otimizado:** A otimização com o algoritmo NSGA-II, combinada com os métodos TOPSIS, resultou em um **melhor desempenho geral da vedação**.

• **Parâmetros Ótimos da Ranhura Espiral:**

    ◦ Para **condições de baixa operação**, os resultados de otimização foram consistentes em todos os esquemas de peso (TOPSIS subjetivo e TOPSIS com peso de entropia), indicando **profundidade da ranhura de 2 μm e comprimento da ranhura de 10 mm** como os parâmetros ideais. Sob essas condições, houve melhorias na capacidade de carga e no desempenho de vazamento, com uma pequena diminuição no desempenho de atrito.    ◦ Para **condições de alta operação**, os resultados ótimos **diferem dependendo do método de seleção**.        ▪ Os métodos TOPSIS subjetivos (pesos 3:6:1 e 4:4:2) geralmente mantiveram a profundidade da ranhura em 2 μm e o comprimento da ranhura em aproximadamente 10 mm. Nesses casos, tanto a capacidade de carga quanto a taxa de vazamento melhoraram, enquanto o atrito diminuiu ligeiramente.        ▪ O método TOPSIS com peso de entropia, que atribui um peso maior ao atrito (38.93%) sob condições de alta operação, resultou em parâmetros ótimos de **26 μm para a profundidade da ranhura e 10 mm para o comprimento da ranhura**. Embora tenha havido uma melhora significativa no desempenho do atrito, a capacidade de carga diminuiu acentuadamente e a taxa de vazamento aumentou ligeiramente.

• **Percepção da Influência dos Parâmetros e Métodos:** A consistência da profundidade (2 μm) e do comprimento (10 mm) nos resultados ótimos reforça o seu impacto significativo no desempenho geral da vedação. A variação dos resultados sob condições de alta operação, dependendo do método de ponderação, sugere que a seleção final da estratégia de otimização deve considerar as **prioridades práticas da aplicação**. O estudo conclui que não há um método de seleção de solução superior ou inferior absoluto, e que a combinação de ambos é mais benéfica para o julgamento dos resultados.

--------------------------------------------------------------------------------

c) Percepções sobre o Problema, a Solução Proposta e os Resultados Obtidos

**Percepções sobre o Problema:**

O problema de otimizar vedações para turbinas a gás de hidrogênio é **altamente relevante e de grande importância prática**. A transição para combustíveis mais limpos como o hidrogênio é crucial para a sustentabilidade energética, e a vedação eficaz é um gargalo tecnológico que afeta diretamente a segurança e a eficiência desses sistemas. A natureza multi-objetivo do problema, onde as métricas de desempenho são frequentemente conflitantes, é uma **característica inerente e desafiadora**. Não é possível simplesmente maximizar tudo; é preciso encontrar um equilíbrio ou _trade-off_ que atenda aos requisitos práticos. A falta de pesquisas teóricas sobre vedações de hidrogênio especificamente ressalta a **originalidade e a necessidade urgente** de estudos como este2.

**Percepções sobre a Solução Proposta:**

A abordagem metodológica empregada é **robusta, lógica e bem estruturada**.

• A combinação de **simulações numéricas detalhadas** com a construção de um **modelo de regressão não-linear** é uma estratégia inteligente. O modelo de regressão, com sua alta precisão, age como um "gêmeo digital" simplificado, permitindo avaliações de desempenho rápidas e substituindo cálculos numéricos que seriam onerosos. Isso melhora significativamente a eficiência do processo de otimização.

• A escolha do **algoritmo NSGA-II** é **apropriada e eficaz** para problemas multi-objetivo. Ele permite a exploração de um conjunto diversificado de soluções de Pareto, oferecendo aos engenheiros uma visão clara dos _trade-offs_ entre os diferentes objetivos.

• A aplicação dos métodos **TOPSIS, tanto subjetivo quanto objetivo (peso de entropia)**, para a seleção da solução ótima a partir do conjunto de Pareto é um ponto forte da solução. Isso demonstra a compreensão de que a "melhor" solução em um cenário multi-objetivo não é única e pode depender das prioridades do usuário ou das condições da aplicação. A capacidade de aplicar diferentes conjuntos de pesos e ver o impacto nos resultados é crucial para a tomada de decisão em engenharia.

**Percepções sobre os Resultados Obtidos:**

Os resultados são **perspicazes e fornecem diretrizes práticas valiosas**:

• A identificação da **profundidade da ranhura como o fator mais influente** é uma descoberta chave para os engenheiros, direcionando os esforços de design e fabricação. Saber quais parâmetros têm maior impacto permite otimizar recursos e focar nas variáveis mais críticas.

• A determinação de **parâmetros ótimos específicos (2 μm de profundidade e 10 mm de comprimento)** fornece uma linha de base concreta para o design. No entanto, a variação desses ótimos com as condições de operação (baixa vs. alta) e os métodos de ponderação ressalta a necessidade de **customização e consideração do contexto de aplicação**.

• A divergência entre os resultados dos métodos TOPSIS subjetivo e objetivo sob **condições de alta operação** é uma percepção crucial. Isso demonstra que não há uma solução "tamanho único" para a otimização multi-objetivo. A melhor solução é um balanço de objetivos baseado em **prioridades práticas**. Se a redução do atrito for crítica, o método de entropia pode ser preferível; se a capacidade de carga e o vazamento forem mais importantes, a abordagem subjetiva pode ser mais adequada. Essa flexibilidade na seleção da solução é um grande benefício do estudo.

• Em suma, o trabalho não apenas resolve um problema complexo com uma metodologia sofisticada, mas também oferece **insights práticos valiosos** que servem como uma base teórica sólida para o design e aplicação de vedações cilíndricas em turbinas a gás de hidrogênio.
