Blueprint Tecnológico GCB - Análise Buy vs Make por Camadas
===========================================================
_Recomendações baseadas na Tabela de Lista de Projetos_

EXECUTIVE SUMMARY - RECOMENDAÇÕES ESTRATÉGICAS
----------------------------------------------

### 🟢 PRIORIDADE ALTA - BUY (COTS) - 70% das aplicações

**Benefícios**: Redução de 40-60% do TCO, time-to-market acelerado, manutenção terceirizada **Sistemas Core**: OMS, WMS, PIM, CRM, TMS, Gateway Pagamentos, Pricing

### 🟡 PRIORIDADE MÉDIA - HYBRID (Buy + Customize) - 20% das aplicações

**Benefícios**: Balance entre velocidade e diferenciação competitiva **Diferenciadores**: E-commerce, CDC, Analytics Avançados, Experiência Cliente

### 🔴 PRIORIDADE BAIXA - MAKE (Custom) - 10% das aplicações

**Justificativa**: Apenas para diferenciadores únicos do negócio GCB **Aplicações**: Integrações específicas, Configurações regionais/bandeiras

* * *

CAMADA 1: EXPERIÊNCIA DO CLIENTE (Frontend/UI)
----------------------------------------------

### 🟢 **RECOMENDAÇÃO BUY - COTS**

| Aplicação | Solução COTS Sugerida | Fornecedor | Justificativa | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- | --- |
| **Portal E-commerce** | Commerce Cloud / Magento Commerce | Salesforce / Adobe | Plataforma madura, extensibilidade, marketplace nativo | I03 |  A3.4, A3.6, A3.7, A3.8, A3.12  |  A busca inteligente, como **Algolia** ou **Elasticsearch**, é um "Quick Win" estratégico que visa melhorar a conversão do e-commerce |
| **Portal B2B** | B2B Commerce Cloud | Salesforce / SAP | Funcionalidades B2B específicas, catálogos diferenciados | I12 | A12.1, A12.2, A12.4 | |
| **PDV Multiskill** | Store Commerce / NCR Counterpoint | Microsoft / NCR | Omnichannel nativo, mobile-first |I02 | A2.1, A2.8, A2.11, A2.12 | |
| **Portal Atendimento** | Service Cloud | Salesforce | Integração nativa com CRM, AI-powered | I08 | A8.1 | |
| **CMS Sellers** | Experience Manager | Adobe | Gestão de conteúdo empresarial, workflows | I03 | A3.9, A3.10 | |

### 🟡 **RECOMENDAÇÃO HYBRID**

| Sistema | Abordagem | Justificativa | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- |
|**App Mobile Rastreamento**|PWA baseada em APIs COTS | | I01 | A1.10 | |
|**PDV Customizado**|Extensões sobre PDV base | | |  | |

* * *

CAMADA 2: SISTEMAS CORE DE NEGÓCIO (Backend/Business Logic)
-----------------------------------------------------------

### 🟢 **RECOMENDAÇÃO BUY - COTS (ALTA PRIORIDADE)**

| Sistema | Solução COTS | Fornecedor | ROI Estimado | Prazo Impl. | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **OMS (Order Management)** | IBM Sterling OMS / Fluent Commerce | IBM / Fluent | 60% redução custos ops | 6-9 meses | I01<br> I03<br> I02<br> I08<br> I06 | A1.2, A1.4<br> A3.6<br> A2.7<br> A8.6<br> A6.7 | |
| **WMS (Manhattan)** | Manhattan Active WM | Manhattan | 40% eficiência logística | 8-12 meses | I01<br> I06<br> I02 |  A1.9 <br> A6.3, A6.5<br> A2.10 | |
| **PIM** | Akeneo PIM / Salsify | Akeneo / Salsify | 50% redução time-to-market | 4-6 meses | I03 | A3.2 | O **PIM Akeneo** é listado como um "Quick Win" estratégico para o Catálogo Unificado (E01), visando ter o catálogo pronto em 1/3 do tempo atual |
| **CRM** | Sales/Service Cloud | Salesforce | 35% aumento conversão | 6-8 meses |I01<br> I02<br> I04<br> I05<br> I07<br> I08 | A1.1<br> A2.13<br> A4.8<br> A5.5<br> A7.3<br> A8.3, A8.7 | O **Salesforce CRM** é um "Quick Win" para a Visão Cliente (E04), visando aumentar a eficiência dos vendedores |
| **TMS** | Manhattan Active TM | Manhattan | 25% redução custos frete | 6-9 meses | I01 | A1.3 | |
| **Pricing Platform** | PROS / Zilliant | PROS / Zilliant | 20% aumento margem | 6-8 meses | I07 | A7.1, A7.4 | O **Pricing Dinâmico** é um "Quick Win" estrutural que busca aumentar a margem líquida |
| **SCM/S&OP** | SAP IBP / Kinaxis | SAP / Kinaxis | 30% redução inventário | 9-12 meses | I01<br> I06 | A1.8<br> A6.1, A6.5, A6.10 | |

### 🟡 **RECOMENDAÇÃO HYBRID - CUSTOMIZAÇÃO FOCADA**

| Sistema | Abordagem | Justificativa | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- |
| **Motor CDC** | Base FICO + Custom Rules | Regulamentação específica BR, diferenciação competitiva | I04 <br> I05<br> I12 | A4.8<br> A5.1, A5.2, A5.3<br> A12.5 | |
| **Hub de Serviços** | ServiceNow + Custom Workflows | Processos únicos GCB, integrações legadas | I04 | A4.4, A4.6 | |
| **Motor Recomendação** | AWS Personalize + Custom Models | Dados proprietários, diferenciação |  I03<br> I04 | A3.5<br> A4.2 | |

### 🔴 **RECOMENDAÇÃO MAKE - APENAS DIFERENCIADORES**

*   **Configurações Regionais/Bandeiras**: Lógica de negócio única GCB (I04 A4.5)
*   **Integrações Mainframe**: Bridges temporários para migração (I04 A4.6)

* * *

CAMADA 3: INTEGRAÇÃO E MIDDLEWARE
---------------------------------

### 🟢 **RECOMENDAÇÃO BUY - PLATAFORMA UNIFICADA**

| Componente | Solução COTS | Benefício | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- |
| **API Gateway** | MuleSoft Anypoint / Kong Enterprise | Governança APIs, security | I09 | A9.1, A9.2, A9.4, A9.5 | O **Adyen Payment Hub** é um "Super Quick Win" e o **Gateway Pagamentos Unificado** é um "Quick Win" estratégico, com foco em aumentar a conversão |
| **ESB/iPaaS** | MuleSoft / Boomi / Azure Logic Apps | Integrações pré-construídas | | | |
| **Gateway Pagamentos** | Adyen / Stripe Connect | PCI compliance, métodos locais | | | |
| **Hub Conciliação** | Adyen Financial Platforms | Automação 95% conciliação | I02<br> I09<br> I12 | A2.4<br> A9.8<br> A12.3 | |

### 🟡 **HYBRID - CONFIGURAÇÃO INTENSIVA**

| Sistema | Abordagem | Justificativa | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- |
|**Hub Fretes**| Plataforma base + integrações regionais | Integração dos canais com novo hub de fretes e construção de torre de controle unificada com solução de TMS" se alinha com o Hub Fretes | I01 | A1.3 |  |
|**Hub Pedidos** | OMS COTS + orchestration customizada | Integração dos canais com hub de pedidos unificado e configurável entre canais e bandeiras" é diretamente relacionada ao Hub Pedidos | I01 | A1.4 | O "Orquestrador Pedidos" é um "Quick Win" para a Gestão de Pedidos (E02) visando uma experiência de checkout unificada |

* * *

CAMADA 4: DADOS E ANALYTICS
---------------------------

### 🟢 **RECOMENDAÇÃO BUY - CLOUD NATIVE**

| Solução | Plataforma | ROI | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- |
| **Customer Data Platform** | Segment / Treasure Data | 40% melhoria segmentação | I01 | A1.1 | O CDP Segment é um "Quick Win" para a Visão Cliente (E04), com o objetivo de tornar as campanhas mais efetivas<br>A CDP + Segmentação Avançada é um "Quick Win" estrutural para efetividade de campanhas e personalização |
| **Advanced Analytics** | Databricks / Snowflake | 50% redução time-to-insight | I01<br>I05<br> I06<br> I07 | A1.6<br>A5.4<br> A6.11<br> A7.5 | |
| **BI/Dashboards** | Tableau / PowerBI | 60% redução relatórios manuais | | | Analytics em Tempo Real (Tableau/PowerBI + Snowflake) é um "Quick Win" estratégico, focado em decisões data-driven e otimização de estoque |
| **ML/AI Platform** | AWS SageMaker / Azure ML | 30% aumento precisão modelos | I03 | A3.5 | "AI/ML avançado" é uma fase de otimização futura no roadmap |

### 🟡 **HYBRID - DADOS PROPRIETÁRIOS**

| Sistema | Abordagem | Justificativa | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- |
|**Loyalty Engine** | Base Salesforce + regras customizadas | | I02<br> I04<br> I05 | A2.5, A2.13<br> A4.8<br> A5.5 | O Loyalty Unificado é um "Quick Win" para a Visão Cliente (E04), visando aumentar a frequência de compra de clientes VIP |
|**Analytics CDC** | Plataforma ML + modelos proprietários | | I05 | A5.4 | |

* * *

CAMADA 5: INFRAESTRUTURA E SEGURANÇA
------------------------------------

### 🟢 **RECOMENDAÇÃO BUY - CLOUD FIRST**

| Componente | Solução | Justificativa | Iniciativas | Atividades | Obs. |
| --- | --- | --- | --- | --- | --- |
| **Cloud Infrastructure** | AWS / Azure Multi-Region | Elasticidade, disaster recovery |I02 | A2.2 | Finalizar a migração de 10 funcionalidades legadas do Mainframe por meio de modernização para cloud" é uma atividade direta. A estratégia geral do blueprint é "Cloud First" e "AWS-FIRST" |
| **Security/Identity** | Okta / Azure AD | Compliance, SSO omnichanal | I08 | A8.4 | |
| **Monitoring** | Datadog / New Relic | Observabilidade full-stack | | | O New Relic/Datadog é um "Super Quick Win" e o API Gateway + Monitoramento é um "Quick Win" estratégico, ambos visando visibilidade total dos sistemas e alertas proativos |
| **Backup/DR** | Veeam Cloud / AWS Backup | RTO/RPO garantidos | | | |

* * *

🚀 QUICK WINS DETALHADOS POR INICIATIVA ESTRUTURANTE
----------------------------------------------------

### **E01 - CATÁLOGO UNIFICADO - Quick Wins**

| Solução | Prazo | Investimento | ROI 6M | Benefício Chave |
| --- | --- | --- | --- | --- |
| **PIM Akeneo** | 12 sem | R$ 2.5M | R$ 12M | Catálogo em 1/3 do tempo atual |
| **Elastic Search** | 8 sem | R$ 800K | R$ 28M | +18% conversão por busca relevante |
| **CDN Global** | 4 sem | R$ 400K | R$ 5M | +2s velocidade = +7% conversão |

### **E02 - GESTÃO PEDIDOS - Quick Wins**

| Solução | Prazo | Investimento | ROI 6M | Benefício Chave |
| --- | --- | --- | --- | --- |
| **OMS Fluent Lite** | 16 sem | R$ 4M | R$ 25M | -30% cancelamentos por ruptura |
| **Orquestrador Pedidos** | 12 sem | R$ 2M | R$ 15M | Unified checkout experience |
| **Tracking em Tempo Real** | 8 sem | R$ 1.2M | R$ 8M | -50% chamados "onde está?" |

### **E03 - ESTOQUE OTIMIZADO - Quick Wins**

| Solução | Prazo | Investimento | ROI 6M | Benefício Chave |
| --- | --- | --- | --- | --- |
| **Demand Sensing** | 12 sem | R$ 3M | R$ 35M | -25% ruptura itens A |
| **Inventory Visibility** | 8 sem | R$ 1.5M | R$ 18M | Ship-from-store habilitado |
| **Smart Replenishment** | 16 sem | R$ 2.8M | R$ 22M | -15% estoque morto |

### **E04 - VISÃO CLIENTE - Quick Wins**

| Solução | Prazo | Investimento | ROI 6M | Benefício Chave |
| --- | --- | --- | --- | --- |
| **Salesforce CRM** | 16 sem | R$ 5M | R$ 38M | +25% eficiência vendedores |
| **CDP Segment** | 12 sem | R$ 2.2M | R$ 22M | Campanhas 3x mais efetivas |
| **Loyalty Unificado** | 20 sem | R$ 3.5M | R$ 30M | +40% frequência compra clientes VIP |

* * *

## Tabela de Lista de Projetos

| Iniciativa | Atividade | Descrição | Estruturante | T-shirt | Dados | Front | Integração | Back |
| --- | --- | --- | --- | --: | --: | --: | --: | --: |
| I01 | ​A1.1 | ​Integração dos canais com a nova base centralizada de clientes | E04 | P | x | x |
| I01 | A1.10 | Implementação de novas tecnologias de rastreio e monitoramento de cargas (beacon, smart tags e etc) |  |  |  |
| I01 | ​A1.2 | Implementação de OMS e Gestão Avançada de Pedidos | E02 | G | x | x | x |
| I01 | ​A1.3 | ​Integração dos canais com novo hub de fretes e construção de torre de controle unificada com solução de TMS | E03 | M | x | x | x |
| I01 | A1.4 | ​Integração dos canais com hub de pedidos unificado e configurável entre canais e bandeiras | E02 | M | x | x | x | x |
| I01 | A1.5 | Desenvolvimento de novas modalidades de frete focadas em regionalização de embarcadores |  |  |  |
| I01 | A1.6 | Advanced Analytics para aumentar assertividade e informatividade da torre de controle |  |  |  |
| I01 | A1.7 | Evolução de capacidades de logistica reversa  |  |  |  |
| I01 | A1.8 | Integração WMS com plataformas de S&OP |  |  |  |
| I01 | A1.9 | Integração Manhattan com ERP (SAP) e remoção de legado |  |  |  |
| I12 | A12.1 | Nova plataforma de gestão de sortimentos para B2B |  | P | x | x | x |
| I12 | A12.2 | Desenvolvimento de nova loja integrada |  | M | x | x | x |
| I12 | A12.3 | Integração automatica com ERP para conciliação automatica |  | M | x | x | x |
| I12 | A12.4 | Nova plataforma de administração para B2B |  | M | x | x | x |
| I12 | A12.5 | Desenvolvimento de componente de CDC integrado para B2B |  | M | x | x | x |
| I12 | A12.6 | Desenvolvimento de componente de S&S integrado para B2B |  | M | x | x | x |
| I02 | A2.1 | Modernização PDV Multiskill Desk e Mobile e Estudo de PDV COTS | - | 2M | x | x | x |
| I02 | A2.10 | Integração retaguarda com ERP e WMS |  |  |  |
| I02 | A2.11 | Implementação PDV Vanilla |  |  |  |
| I02 | A2.12 | Customização PDV |  |  |  |
| I02 | A2.13 | Integração Loyalty/CRM |  |  |  |
| I02 | A2.2 | Finalizar a migração de 10 funcionalidades legadas do Mainframe por meio de modernização para cloud | - | 2M | x | x | x |
| I02 | A2.3 | Habilitação de oferta de produtos complementares (cross-sell e up-sell) para múltiplos itens | I03, E01, E03 | G | x | x | x |
| I02 | A2.3 | Habilitação de oferta de produtos complementares (cross-sell e up-sell) para múltiplos itens | E01 | G |  |
| I02 | A2.3 | Habilitação de oferta de produtos complementares (cross-sell e up-sell) para múltiplos itens | E03 | G |  |
| I02 | A2.4 | ​Automatização do processo de conciliação de pagamentos para eliminar erros e riscos financeiros | E03 |  | x | x | x |
| I02 | A2.5 | ​Integração com parceiros e programas de fidelidade |  - |  | x | x | x |
| I02 | A2.6 | Seleção de Retaguarda de Loja - Mercado |  |  |  |
| I02 | A2.7 | Integração com OMS |  |  |  |
| I02 | A2.8 | Seleção de PDV- Mercado |  |  |  |
| I02 | A2.9 | Implementação Retaguarda |  |  |  |
| I03 | A3.1 | ​Redesenho do Customer Journey da jornada de busca (filtros, selos e flags) integrada ao novo catalogo de produtos | E01 | G | x | x | x |
| I03 | A3.10 | Desenvolvimento de nova plataforma para sellers |  | G | x | x | x | x |
| I03 | A3.11 | Rankeamento de Sellers |  | P | x | x | x |
| I03 | A3.12 | Experiencia personalizada da jornada do cliente |  | G | x | x | x | x |
| I03 | A3.2 | Integração com solução de Gestão do Catálogo e Informações de Produtos (PIM) | E01, E02 | P | x | x | x |
| I03 | A3.2 | Integração com solução de Gestão do Catálogo e Informações de Produtos (PIM) | E01 | P |  |
| I03 | A3.2 | Integração com solução de Gestão do Catálogo e Informações de Produtos (PIM) | E02 | P |  |
| I03 | A3.3 | ​Melhorias na jornada de PDP (fechamento de compra, reviews, características do produto, entre outros)  | E02, E04 | M | x | x | x |
| I03 | A3.3 | ​Melhorias na jornada de PDP (fechamento de compra, reviews, características do produto, entre outros)  | E02 | M |  |
| I03 | A3.3 | ​Melhorias na jornada de PDP (fechamento de compra, reviews, características do produto, entre outros)  | E04 | M |  |
| I03 | A3.4 | ​Redesenho do Customer Journey em outras jornadas (carrinho e checkout) | E01 | G |  |
| I03 | A3.4 | ​Redesenho do Customer Journey em outras jornadas (carrinho e checkout) | E02 | G |  |
| I03 | A3.4 | ​Redesenho do Customer Journey em outras jornadas (carrinho e checkout) | E03 | G |  |
| I03 | A3.4 | ​Redesenho do Customer Journey em outras jornadas (carrinho e checkout) | E01, E02, E03 | G | x | x | x | x |
| I03 | A3.5 | ​Desenvolvimento de motor com AI de recomendação de produtos de vitrine para o perfil do cliente | E04 | M | x | x | x | x |
| I03 | A3.6 | Integração plataforma de e-commerce com OMS |  | P |  | x | x |
| I03 | A3.7 | Seleção e implementação de nova plataforma de e-commerce  |  | G | X | X | X | X |
| I03 | A3.8 | Integração da nova plataforma com ERP e WMS |  | P |  | x | x |
| I03 | A3.9 | Implementação de novo CMS para base de Sellers |  | G | x | x | x | x |
| I04 | A4.1 | ​Integração com CDC para obtenção de dados de fim de contrato para oferta de serviços | I05 | PP |  | x | x |
| I04 | A4.10 | Desenvolvimento de módulo de campanhas para S&S |  | M | x | x | x | x |
| I04 | A4.2 | ​Criação de motor de recomendações de serviços (Visão Relacional das Capacidades) | E01, E04 | 2M | x | x | x |
| I04 | A4.2 | ​Criação de motor de recomendações de serviços (Visão Relacional das Capacidades) | E01 | 2M |  |
| I04 | A4.2 | ​Criação de motor de recomendações de serviços (Visão Relacional das Capacidades) | E04 | 2M |  |
| I04 | A4.3 | ​Adequação da jornada para incluir as ofertas de serviços ao longo da experiência do cliente |  - | M | x | x | x |
| I04 | A4.4 | ​Definição de um hub de serviços unificado e desacoplado do mainframe |  - | 2P | x | x | x |
| I04 | A4.5 | Implementação de primeira fase de arquitetura para configurações a níveis regionais |  - | 2P | x | x |
| I04 | A4.6 | Atualização do hub de serviços habilitando que seja ​configurável a nível regional entre canais e bandeiras |  - | M | x | x | x | x |
| I04 | A4.7 | Habilitação de sistema de comissionamento para vendedores integrado ao HCM |  | P | x | x | x |
| I04 | A4.8 | Integração de motor de CDC com CRM e Loyalty |  | P |  | x | x |
| I04 | A4.9 | Integração de novas modalidades de S&S |  | P |  | x | x |
| I05 | A5.1 | ​Redesenho de motor de aprovação de CDC (configuração de ativação, taxa de juros diferenciada por item, migração da consulta CPF, cálculo de parcelas e originação de contratos para a baixa plataforma) | E1, E4  | 2P | x | x | x |
| I05 | A5.1 | ​Redesenho de motor de aprovação de CDC (configuração de ativação, taxa de juros diferenciada por item, migração da consulta CPF, cálculo de parcelas e originação de contratos para a baixa plataforma) | E01 | 2P |  |
| I05 | A5.1 | ​Redesenho de motor de aprovação de CDC (configuração de ativação, taxa de juros diferenciada por item, migração da consulta CPF, cálculo de parcelas e originação de contratos para a baixa plataforma) | E04 | 2P |  |
| I05 | A5.2 | ​Habilitação CDC para carrinho misto (1P e 3P) e múltiplos itens (lojas físicas) | E01 | 2P | x | x | x |
| I05 | A5.3 | ​Revisão da jornada CDC para acelerar fluxo de aprovação | E01, E04 | 2P | x | x | x |
| I05 | A5.3 | ​Revisão da jornada CDC para acelerar fluxo de aprovação | E01 | 2P |  |
| I05 | A5.3 | ​Revisão da jornada CDC para acelerar fluxo de aprovação | E04 | 2P |  |
| I05 | A5.4 | ​Advanced Analytics para segmentação de ofertas e uso de leads com CDC | - | #N/D | x | x | x | x |
| I05 | A5.5 | Integração com CRM e Loyalty |  |  |  |
| I05 | A5.6 | Desenvolvimento de novos produtos de crédito (consignado, empréstimo pessoal, consórcio e etc) |  |  |  |
| I05 | A5.7 | Integração com novos Bureaus |  |  |  |
| I05 | A5.8 | Desenvolvimento de CDC para Sellers e Parceiros |  |  |  |
| I06 | A6.1 | ​Otimização do fluxo de abastecimento com ferramentas de Inteligência Logística e SCM | E03 | P | x | x | x |
| I06 | A6.10 | Integração de SCM e S&OP e plataforma de alocação de sellers no fulfillment |  |  |  |
| I06 | A6.11 | Advanced Analytics para requisição e solicitação de abastecimento automatico |  |  |  |
| I06 | A6.2 | ​Desenvolvimento de capacidade de Remessa Consignada | E03 | G | x | x | x |
| I06 | A6.3 | ​Evolução dos processos, ferramentas e capacidades de fullfilment no Manhattan integradas com ISLS (In-Store Logistics System) | E03 | G | x | x | x |
| I06 | A6.4 | ​Desenvolvimento de capacidades para habilitação e integração no Vende+ | E03 | M | x | x | x |
| I06 | A6.5 | ​Automação de processos e ferramentas de S&OP integradas ao WMS como fonte única da verdade para dados de estoques | E03 | M | x | x | x |
| I06 | A6.6 | Integração para emissão de notas com parceiros |  |  |  |
| I06 | A6.7 | Integração com OMS para pedidos 3P |  |  |  |
| I06 | A6.8 | Integração com CBFull para 3P em fulfillment |  |  |  |
| I06 | A6.9 | Desenvolvimento de plataforma alocação de sellers no fulfillment |  |  |  |
| I07 | A7.1 | Implementação de plataforma de pricing integrada |  | P | x | x | x |
| I07 | A7.2 | Implementação de ferramenta de oferta |  | M | x | x | x |
| I07 | A7.3 | Integração de ferramenta de oferta com CRM |  | M | x | x | x |
| I07 | A7.4 | Parametrização de regras e condições de promocionamento |  | M | x | x | x |
| I07 | A7.5 | Integração com e-commerce para captua e interpretação de informações |  | M | x | x | x |
| I07 | A7.5 | Advanced Analitycs para recomendação de ofertas |  | M | x | x | x |
| I08 | A8.1 | Nova plataforma de atendimento ao consumidor |  | M | x | x | x |
| I08 | A8.2 | Modernização de plataformas de CCM |  | M | x | x | x |
| I08 | A8.3 | Integração de CRM sanitizado com canais de atendimento |  | M | x | x | x |
| I08 | A8.4 | Implementação de Sistema de antifraude para programas de pontos |  | M | x | x | x |
| I08 | A8.5 | Integração com Plataforma de CDC e S&S para ativação |  | M | x | x | x |
| I08 | A8.6 | Integração de plataforma de atendimento com OMS para acompanhamento de pedidos |  | M | x | x | x |
| I08 | A8.7 | Integração de plataforma de CCM com CRM para ativação |  | M | x | x | x |
| I09 | A9.1 | ​Implementação de solução de gateway de pagamentos alinhado com as necessidades do negocio |  - | 2P | x | x | x |
| I09 | A9.2 | ​Implementação de novos métodos de pagamento – Google Pay & Rev Pix |  - | G | x | x | x | x |
| I09 | A9.3 | ​Desenvolvimento de integrações multicanal | E01 | P |  | x | x |
| I09 | A9.4 | ​Criação de hub central configurável e desacoplado do mainframe para meios de pagamento omnicanal | E03 | 2M | x | x | x | x |
| I09 | A9.5 | Implementação de novos meios de pagamento - Apple Pay, carteiras digitais |  |  |  |
| I09 | A9.6 | Modernização adquirentes |  |  |  |
| I09 | A9.7 | Harmonização de adquirentes e hub de pagamentos fisico e digital |  |  |  |
| I09 | A9.8 | Integração de conciliação bancária com ERP |  |  |  |
