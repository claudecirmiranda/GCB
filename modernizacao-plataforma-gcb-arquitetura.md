# Arquitetura de Referência para a Modernização da Plataforma Tecnológica do Grupo Casas Bahia (GCB)

## Sumário
1. [Objetivo](#objetivo)
2. [Contexto Atual da Plataforma](#contexto-atual-da-plataforma)
3. [Diretrizes Arquiteturais](#diretrizes-arquiteturais)
4. [Iniciativas Estruturantes](#iniciativas-estruturantes)
5. [Arquitetura-Alvo (High-Level)](#arquitetura-alvo-high-level)
6. [Mapeamento Tecnológico por Iniciativa](#mapeamento-tecnológico-por-iniciativa)
7. [Priorização Técnica das Entregas](#priorização-técnica-das-entregas)
8. [Modelo de Referência de Microsserviços](#modelo-de-referência-de-microsserviços)
9. [Considerações sobre Kubernetes e Multi-Cloud](#considerações-sobre-kubernetes-e-multi-cloud)
10. [Próximos Passos](#próximos-passos)

---

## 1. Objetivo

Este documento tem como objetivo descrever a arquitetura de referência que orientará a modernização da plataforma tecnológica do Grupo Casas Bahia (GCB), com foco em:

- Suportar a velocidade das mudanças exigidas pelo mercado
- Reduzir a complexidade e o acoplamento do portfólio atual de aplicações
- Eliminar ineficiências operacionais e altos custos de manutenção
- Adotar uma arquitetura baseada em microsserviços, cloud-native e APIs
- Alavancar soluções modernas com aderência aos padrões técnicos do GCB e às capacidades da AWS (EKS, EventBridge, DynamoDB, etc.)
- Atender de forma escalável e segura às principais iniciativas estruturantes e de negócio

---

## 2. Contexto Atual da Plataforma

A plataforma atual do GCB apresenta desafios significativos que limitam sua capacidade de resposta às demandas do mercado:

- **Arquitetura monolítica e acoplada**: dificulta a evolução, integração e escalabilidade das soluções.
- **Execução de processos fragmentada**: diversos sistemas isolados geram retrabalho e falhas operacionais.
- **Alto custo de manutenção e baixa eficiência operacional**: devido à redundância funcional e tecnológica.
- **Baixa aderência a práticas modernas**: como DevSecOps, observabilidade centralizada, arquitetura orientada a eventos e APIs abertas.
- **Dependência de legados críticos**, como mainframe e sistemas fechados para OMS, WMS, PIM e CRM.
- **Necessidade de transformação digital**, com foco em cloud-native, dados, personalização, automação e omnicanalidade.

---

## 3. Diretrizes Arquiteturais

A modernização da plataforma do GCB será guiada pelas seguintes diretrizes arquiteturais:

### 🧱 Arquitetura
- Adoção de **microsserviços desacoplados**, orientados por domínio de negócio (DDD).
- Serviços **cloud-native**, implantados via containers em **plataforma Kubernetes** (AKS, EKS ou OpenShift).
- **Comunicação baseada em APIs RESTful** (OpenAPI 3.0) e **eventos assíncronos** via Kafka (MSK) e EventBridge.
- Uso de **service mesh com Istio** para roteamento inteligente, políticas e observabilidade.

### ☁️ Multi-cloud e Portabilidade
- Manutenção de ambientes híbridos com suporte a **GCP e AWS**, promovendo independência e resiliência.
- Utilização de **Helm** e **Kustomize** para gerenciamento de deploys e portabilidade entre clouds.
- Exploração de benefícios do **AWS MAP (Migration Acceleration Program)** para acelerar a transformação.

### 🔐 Segurança
- Autenticação via **OAuth2/OpenID Connect**, com suporte a **JWT tokens** e **Cognito** na AWS.
- Armazenamento seguro de segredos e credenciais usando **Kubernetes Secrets**, **AWS Secrets Manager** e **Delinea**.
- Aplicação de **políticas de segurança zero-trust**, com malha de serviços, criptografia em trânsito e at-rest.

### 🔁 Integração e Interoperabilidade
- Exposição de funcionalidades por **API Gateway (Kong ou Amazon API Gateway)** com rate limiting e analytics.
- Integração com sistemas legados via **orquestração de fluxos (NiFi / IBM App Connect / Step Functions)**.
- Uso de **event-driven architecture (EDA)** com suporte a padrões pub/sub e event sourcing.

### 📈 Observabilidade e Operações
- Adoção de **instrumentação padronizada** com Prometheus, Grafana, Jaeger e Dynatrace.
- Definição de **SLIs, SLOs e SLAs** com alertas centralizados e painéis de visualização.
- Execução contínua de testes de performance e qualidade de código via **JMeter, k6, Cypress, Zephyr e SonarCloud**.

### 🚀 DevSecOps e Governança
- Esteiras CI/CD padronizadas com **GitHub Actions, Jenkins, Spinnaker** e versionamento obrigatório via Git.
- Política de **quality gate obrigatória** com SonarCloud (>=80% coverage em novos códigos).
- Catálogo de serviços via **Backstage**, com automação de governança, deploys e observabilidade por microsserviço.

---

## 4. Iniciativas Estruturantes

A modernização da plataforma terá como foco inicial quatro iniciativas estruturantes, que são fundamentais para suportar os demais projetos de negócio e habilitar uma operação omnicanal, integrada e orientada ao cliente:

---

### E01 – Catálogo de Produtos Eficiente e Unificado

**Objetivo:**  
Criar uma solução centralizada para gestão de produtos com dados enriquecidos e distribuídos de forma consistente em todos os canais.

**Pontos-Chave Arquiteturais:**
- Implantação de **PIM (Product Information Management)** moderno e escalável.
- Integração com canais via **APIs** (REST) e eventos.
- Utilização de **ElasticSearch ou OpenSearch (AWS)** para busca performática.
- Microsserviços para normalização, enriquecimento e sincronização de dados.

---

### E02 – Gestão Avançada de Pedidos (OMS)

**Objetivo:**  
Unificar o controle de pedidos de todos os canais (e-commerce, lojas, parceiros), habilitando orquestração e rastreamento fim a fim.

**Pontos-Chave Arquiteturais:**
- Implantação de novo **OMS (Order Management System)** com capacidade omnicanal.
- Microsserviços desacoplados para orquestração de pedidos.
- Eventos de pedido e status via **Kafka (MSK)** ou **EventBridge (AWS)**.
- Rastreabilidade completa com **observabilidade distribuída (Jaeger, Grafana)**.

---

### E03 – Estoques, Inventário e Cadeia de Abastecimento Otimizados

**Objetivo:**  
Consolidar a visão de estoque em tempo real e melhorar a acurácia logística.

**Pontos-Chave Arquiteturais:**
- Consolidação de **WMSs legados** em uma nova solução ou plataforma modular.
- Serviços de consulta em tempo real com **Redis (cache)** e replicação entre centros.
- Integração com **SCM e S&OP**, com APIs e eventos.
- Painéis operacionais via **Grafana + Prometheus**.

---

### E04 – Visão Unificada do Cliente

**Objetivo:**  
Criar uma base única e confiável de dados de cliente para personalização, atendimento e inteligência.

**Pontos-Chave Arquiteturais:**
- Implantação de um **Customer Data Platform (CDP)** ou base de dados unificada.
- Enriquecimento e deduplicação de dados com microsserviços.
- Exposição via **API Hub / Gateway** e eventos para sistemas consumidores.
- Uso de **MongoDB (NoSQL)** e **DynamoDB** para persistência distribuída.

---

Essas iniciativas serão os pilares técnicos da modernização, criando a base para entregas rápidas, escaláveis e integradas com os demais projetos de negócio.

---

## 5. Visão de Arquitetura de Referência

A arquitetura proposta tem como base os seguintes princípios:

- Microsserviços desacoplados por domínio de negócio (DDD).
- Orquestração via eventos e APIs (REST/gRPC), com gateway unificado.
- Plataforma Kubernetes (EKS, AKS, OpenShift) como base para execução.
- Observabilidade, segurança e governança integradas desde o início (Shift Left).
- Adoção de soluções cloud-native e COTS onde aplicável.

---

### Componentes da Arquitetura

#### 🔹 Camada de Apresentação
- Aplicações Web e Mobile: React, Angular, Vue.js, React Native, Flutter, Swift/Kotlin.
- CDN e otimização de entrega: **Akamai** (GCP) / **Amazon CloudFront** (AWS).

#### 🔹 Camada de API e Integração
- API Gateway: **Kong** (GCP) / **Amazon API Gateway**.
- Catálogo de APIs: **API Hub** + **Backstage**.
- Orquestração de integrações: **NiFi**, **App Connect**.
- Malha de serviços: **Istio** com **mTLS**, roteamento e observabilidade.

#### 🔹 Camada de Microsserviços
- Desenvolvimento em: Java (Spring Boot), .NET, Node.js, Python.
- Execução sobre Kubernetes: **OpenShift**, **EKS (AWS)** ou **AKS (GCP)**.
- Service Discovery: **Consul**.
- Configuração: **Configurat**, **AWS Parameter Store**, **ConfigMaps**.

#### 🔹 Camada de Mensageria e Eventos
- Barramento de eventos: **Kafka** (ou **Amazon MSK**), **EventBridge** (AWS).
- Fila assíncrona: **SQS (AWS)**, Kafka Topics, **Pub/Sub (GCP)**.
- Event Streaming com integração desacoplada entre serviços.

#### 🔹 Camada de Dados
- Banco relacional: PostgreSQL, MySQL, Oracle, SQL Server.
- Banco NoSQL e documentos: MongoDB, **DynamoDB (AWS)**.
- Cache e performance: Redis.
- Buscadores: ElasticSearch, **OpenSearch (AWS)**.
- Dados de cliente: CDP unificado com enriquecimento, mascaramento (Delphix), deduplicação.

#### 🔹 Observabilidade
- Tracing: **Jaeger**.
- Logs: Stackdriver, ELK, **CloudWatch** (AWS).
- Métricas: **Prometheus** + **Grafana**.
- APM: Dynatrace, Lighthouse.
- SLO/SLA/SLI definidos por domínio.

#### 🔹 DevOps & Deploy
- Repositórios: Git (GitHub GCB), pipelines CI/CD com GitHub Actions, Jenkins, Spinnaker.
- Helm/Kustomize para deploy.
- XebiaLabs, BMC Control-M para orquestração de jobs.
- Provisionamento: **Terraform** (infraestrutura como código).

#### 🔹 Segurança & Governança
- Autenticação/Autorização: OAuth2.0, OIDC.
- Gestão de segredos: **Delinea**, **AWS Secrets Manager**.
- Monitoramento de vulnerabilidades: **Qualys**, scanners automatizados.
- Criptografia em repouso e em trânsito.


---

## 6. Jornada de Modernização

A jornada de modernização do GCB segue uma abordagem incremental, orientada por valor de negócio e alinhada às 4 Iniciativas Estruturantes (E01–E04). Cada fase contempla o redesenho dos domínios principais, desacoplamento de sistemas legados e implantação de soluções modernas, cloud-native e escaláveis.

---

### 6.1 Etapas da Jornada

1. **Descoberta e Mapeamento**  
   Levantamento de sistemas legados, integrações, times responsáveis, restrições técnicas e dívida tecnológica.

2. **Definição de Domínios e Capabilities**  
   Modelagem por domínio com base em DDD, visão futura de capabilities e boundaries.

3. **Arquitetura de Referência e Plano de Transição**  
   Criação de arquitetura-alvo, com fases de transição, coexistência com legado, e componentes COTS/modernos.

4. **Desenvolvimento por Fase (Iniciativas E01 a E04)**  
   Implementação por lotes, com squads alinhados aos domínios, DevOps completo e observabilidade.

5. **Governança e Sustentação**  
   Implantação de práticas de SRE, arquitetura evolutiva, indicadores DORA, SLO/SLA e governança API-first.

---

## 6. Mapeamento Tecnológico por Iniciativa

Com base no blueprint atual da arquitetura macro do GCB, detalhamos o mapeamento das tecnologias legadas, soluções atuais em uso no GCP e alternativas/sugestões de modernização via AWS. Essa visão permite orientar a jornada de migração e modernização de forma estratégica e incremental.

---

### 📦 E01 – Catálogo de Produtos eficiente e unificado

| Componente       | Legado              | GCP atual                   | Alternativas AWS (sugestão de migração)                     |
|------------------|---------------------|-----------------------------|--------------------------------------------------------------|
| PIM              | Sistema proprietário| GCP + MongoDB               | AWS Marketplace PIM (Akeneo, Informatica) ou S3 + DynamoDB  |
| Motor de busca   | Solr                | ElasticSearch               | Amazon OpenSearch Service                                   |
| API Catálogo     | Java Monolito       | Spring Boot + GKE/OpenShift | Lambda/API Gateway ou ECS Fargate + App Mesh                |

---

### 📦 E02 – Gestão avançada de pedidos (OMS)

| Componente              | Legado                   | GCP atual                     | Alternativas AWS (sugestão de migração)          |
|-------------------------|--------------------------|-------------------------------|---------------------------------------------------|
| OMS                     | Sistema legado acoplado  | Microsserviços + Kafka        | EventBridge + Step Functions + DynamoDB           |
| Orquestração de pedidos | Lógica acoplada          | Apache NiFi                   | AWS Step Functions + Lambda                       |
| Base transacional       | SQL Server/Oracle        | PostgreSQL/MySQL (Cloud SQL)  | Amazon RDS / Aurora                               |
| Gateway                 | WebService SOAP/REST     | Kong API Gateway              | Amazon API Gateway                                |

---

### 📦 E03 – Estoques, inventário e cadeia de abastecimento (SCM)

| Componente               | Legado                  | GCP atual                     | Alternativas AWS (sugestão de migração)              |
|--------------------------|-------------------------|-------------------------------|------------------------------------------------------|
| WMS / SCM                | Sistema legado / batch  | Microserviços + PostgreSQL    | AWS Supply Chain + ECS/EKS + RDS                    |
| Inventário em tempo real | Tabelas batch           | Kafka Streams + Redis         | Amazon Kinesis + ElastiCache                        |
| Integrações com lojas    | FTP/Batch/XML           | API-first com NiFi/Kong       | EventBridge + API Gateway + Lambda                  |

---

### 📦 E04 – Visão unificada do cliente

| Componente                   | Legado                    | GCP atual                         | Alternativas AWS (sugestão de migração)               |
|-----------------------------|---------------------------|-----------------------------------|--------------------------------------------------------|
| CRM                         | Sistema legado            | Salesforce / microsserviços       | Amazon Connect CRM, Segment + Lambda                  |
| Enriquecimento de dados     | Manual / SQL scripts      | Delphix, DataHub                  | AWS Glue + AWS DataBrew                               |
| Identidade/autenticação     | Autenticação básica       | OAuth2 / OIDC / Keycloak          | Amazon Cognito + Secrets Manager                      |
| CDP (Customer Data Platform)| inexistente               | MongoDB + Kafka                   | DynamoDB + Personalize + Redshift                     |

---

### 6.2 Visão Consolidada por Camada Tecnológica

| Camada             | Tecnologias Legadas          | GCP Atual                        | AWS Equivalente / Sugestão                         |
|--------------------|-------------------------------|----------------------------------|----------------------------------------------------|
| Backend            | Java/.NET Monolitos          | GKE, Cloud Run, Functions        | ECS, Lambda, App Runner, EKS                       |
| API & Integração   | Middleware, WS SOAP          | Apigee, Endpoints, Kong, NiFi    | API Gateway, AppSync, EventBridge, Step Functions |
| Armazenamento      | SQL Server, Oracle, DBs legados| Cloud SQL, Firestore, Bigtable   | Aurora, DynamoDB, S3, RDS                          |
| Mensageria         | FTP/XML/Batch                | Pub/Sub                          | SNS, SQS, EventBridge                              |
| Observabilidade    | Ferramentas customizadas     | Stackdriver, OpenTelemetry       | CloudWatch, X-Ray, OpenTelemetry AWS SDKs         |
| Cache              | Redis local / memória app    | Memorystore                      | ElastiCache (Redis/Memcached)                     |
| Busca              | Solr                         | ElasticSearch                    | Amazon OpenSearch                                  |
| IA/ML              | -                            | Vertex AI, BigQuery ML           | Amazon Personalize, SageMaker                      |

---

### 6.3 Diretrizes de Migração

- **Priorizar componentes desacopláveis** com maior impacto em valor (ex: Catálogo, OMS, CRM).
- **Reusar tecnologias abertas e cloud-native**, favorecendo serviços gerenciados.
- **Reduzir acoplamento com mainframe** via camadas de eventos e APIs padronizadas.
- **Garantir coexistência temporal** com o legado, monitorando impacto técnico e funcional.

---

## 7. Priorização Técnica das Entregas

> Matriz de valor x complexidade, ordem de execução sugerida, interdependências entre blocos e ganhos esperados.

---

## 8. Modelo de Referência de Microsserviços

- Estrutura padrão de microsserviço
- Comunicação (REST, Kafka, EventBridge)
- Observabilidade
- Segurança
- CI/CD e Feature Toggle
- Exemplo de layout (Java/Spring Boot)

---

## 9. Considerações sobre Kubernetes e Multi-Cloud

- Padrão técnico Kubernetes
- Plataformas: AKS, EKS, OpenShift
- Estratégia multi-cloud e portabilidade com Helm/Kustomize
- Padrões de deploy e service discovery

---

## 10. Próximos Passos

- Documentar arquitetura detalhada por domínio
- Criar templates de microsserviço
- Planejar MVP técnico com foco no Catálogo (E01)
- Engajamento com AWS MAP e definição de workloads prioritárias

