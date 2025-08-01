#!/usr/bin/env python3
"""
GCB Blueprint - Arquitetura de Alto Nível
Transformação Digital Full-Stack com foco em Buy vs Make
"""

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda, ECS
from diagrams.aws.database import RDS, Dynamodb, Redshift
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.mobile import APIGateway
from diagrams.aws.analytics import Quicksight, Kinesis
from diagrams.aws.ml import Sagemaker, Personalize
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, ELB
from diagrams.aws.security import IAM, Cognito
from diagrams.aws.management import Cloudwatch

from diagrams.saas.analytics import Snowflake
from diagrams.onprem.analytics import Tableau
from diagrams.saas.chat import Slack
from diagrams.saas.communication import Twilio
from diagrams.saas.identity import Okta
from diagrams.generic.blank import Blank as Stripe
from diagrams.onprem.database import Oracle
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Nginx
from diagrams.generic.blank import Blank
from diagrams.generic.database import SQL
from diagrams.generic.compute import Rack

from diagrams.generic.device import Mobile

# Configurações do diagrama
graph_attr = {
    "fontsize": "12",
    "bgcolor": "white",
    "pad": "1.0"
}

with Diagram("GCB Blueprint - Arquitetura Transformação Digital", 
             filename="gcb_architecture_blueprint", 
             show=False,
             graph_attr=graph_attr,
             direction="TB"):

    # CAMADA 1: EXPERIÊNCIA DO CLIENTE (Frontend/UI)
    with Cluster("🎨 CAMADA EXPERIÊNCIA - Frontend/UI"):
        
        with Cluster("E-commerce & Digital"):
            ecommerce = Blank("Portal E-commerce\n(Salesforce/Adobe)")
            b2b_portal = Blank("Portal B2B\n(Salesforce B2B)")
            mobile_app = Mobile("App Mobile\n(PWA)")
            seller_cms = Blank("CMS Sellers\n(Adobe Experience)")
        
        with Cluster("Ponto de Venda"):
            pdv_multiskill = Blank("PDV Multiskill\n(Microsoft/NCR)")
            pdv_vanilla = Blank("PDV Vanilla\n(COTS)")
            pdv_custom = Blank("PDV Custom\n(Extensões)")
        
        with Cluster("Atendimento"):
            atendimento = Blank("Portal Atendimento\n(Salesforce Service)")
            ccm = Blank("Platform CCM\n(Modernizada)")

    # CDN e Load Balancing
    cdn = CloudFront("CloudFront CDN")
    load_balancer = ELB("Application LB")
    
    # API Gateway - Ponto de entrada
    api_gateway = APIGateway("API Gateway\n(Kong/AWS)")

    # CAMADA 2: SISTEMAS CORE DE NEGÓCIO (Backend/Business Logic)
    with Cluster("⚙️ CAMADA CORE BUSINESS - Backend Logic"):
        
        with Cluster("🚚 Logística & Pedidos (E02/E03)"):
            oms = Blank("OMS\n(IBM Sterling/Fluent)")
            tms = Blank("TMS\n(Manhattan Active)")
            wms = Blank("WMS\n(Manhattan)")
            torre_controle = Lambda("Torre Controle\n(Analytics)")
            
        with Cluster("📦 Produtos & Catálogo (E01)"):
            pim = Blank("PIM\n(Akeneo/Salsify)")
            search_engine = Blank("Search Engine\n(Elasticsearch)")
            motor_recomendacao = Sagemaker("Motor Recomendação\n(AWS Personalize)")
            
        with Cluster("💰 Crédito & Financeiro"):
            motor_cdc = ECS("Motor CDC\n(FICO + Custom)")
            aprovacao_credito = Lambda("Aprovação Crédito\n(Hybrid)")
            comissionamento = Blank("Comissionamento\n(HCM Integration)")
            
        with Cluster("🛠️ Serviços & Suporte"):
            hub_servicos = ECS("Hub Serviços\n(ServiceNow + Custom)")
            motor_servicos = Sagemaker("Motor Recomendação\nServiços")
            campanhas = Lambda("Campanhas S&S")
            
        with Cluster("💲 Pricing & Promoções"):
            pricing_platform = Blank("Pricing Platform\n(PROS/Zilliant)")
            ferramenta_ofertas = Lambda("Ferramenta Ofertas")
            motor_promocoes = Lambda("Motor Promocional")

    # CAMADA 3: INTEGRAÇÃO E MIDDLEWARE
    with Cluster("🔗 CAMADA INTEGRAÇÃO - Middleware"):
        
        with Cluster("Hubs Centrais"):
            hub_pagamentos = Stripe("Hub Pagamentos\n(Adyen/Stripe)")
            hub_fretes = ECS("Hub Fretes")
            hub_pedidos = ECS("Hub Pedidos")
            
        with Cluster("Barramentos & APIs"):
            esb = APIGateway("ESB/iPaaS\n(MuleSoft/Boomi)")
            integration_layer = Lambda("Integration Layer")
            event_bus = Eventbridge("Event Bus")
            
        with Cluster("Conciliação & Sync"):
            conciliacao = Lambda("Conciliação Auto\n(Pagamentos/ERP)")
            sync_engine = Lambda("Sync Engine")

    # CAMADA 4: DADOS E ANALYTICS
    with Cluster("📊 CAMADA DADOS - Analytics & ML"):
        
        with Cluster("Customer Data (E04)"):
            cdp = S3("Customer Data Platform\n(Segment/Adobe)")
            crm_unified = Blank("CRM Unificado\n(Salesforce)")
            loyalty = Blank("Loyalty Platform\n(Salesforce + Custom)")
            
        with Cluster("Business Intelligence"):
            data_lake = S3("Data Lake\n(S3 + Glue)")
            data_warehouse = Redshift("Data Warehouse\n(Redshift/Snowflake)")
            analytics_platform = Quicksight("Advanced Analytics\n(QuickSight/Tableau)")
            
        with Cluster("Machine Learning"):
            ml_platform = Sagemaker("ML Platform\n(SageMaker)")
            ai_personalization = Personalize("AI Personalização")
            demand_forecasting = Sagemaker("Demand Forecasting")

    # CAMADA 5: INFRAESTRUTURA E SEGURANÇA
    with Cluster("🔐 CAMADA INFRAESTRUTURA - Cloud & Security"):
        
        with Cluster("Cloud Native"):
            containers = ECS("Container Platform\n(ECS/EKS)")
            serverless = Lambda("Serverless\n(Lambda)")
            storage = S3("Object Storage\n(S3)")
            
        with Cluster("Segurança & Identidade"):
            identity = Cognito("Identity Management\n(Cognito/Okta)")
            security = IAM("Security & IAM")
            monitoring = Cloudwatch("Monitoring\n(CloudWatch/DataDog)")
            
        with Cluster("Sistemas Legados"):
            mainframe = Rack("Mainframe\n(Legacy)")
            sap_erp = Oracle("SAP ERP")
            legacy_db = SQL("Legacy DBs")

    # INTEGRAÇÕES E FLUXOS PRINCIPAIS
    
    # Frontend para API Gateway
    [ecommerce, b2b_portal, mobile_app] >> cdn >> load_balancer >> api_gateway
    [pdv_multiskill, pdv_vanilla, atendimento] >> api_gateway
    
    # API Gateway para Core Systems
    api_gateway >> [oms, pim, motor_cdc, hub_servicos, pricing_platform]
    api_gateway >> hub_pagamentos
    
    # Core Business Integrations
    oms >> [tms, wms, torre_controle]
    pim >> [search_engine, motor_recomendacao]
    motor_cdc >> aprovacao_credito >> comissionamento
    hub_servicos >> [motor_servicos, campanhas]
    pricing_platform >> [ferramenta_ofertas, motor_promocoes]
    
    # Middleware Orchestration
    esb >> [integration_layer, event_bus, sync_engine]
    hub_pedidos >> oms
    hub_fretes >> tms
    conciliacao >> hub_pagamentos
    
    # Data Flow
    [oms, pim, motor_cdc, hub_servicos] >> data_lake >> data_warehouse >> analytics_platform
    cdp >> [crm_unified, loyalty]
    data_warehouse >> [ml_platform, ai_personalization, demand_forecasting]
    
    # AI/ML Feedback Loops
    motor_recomendacao >> ai_personalization
    demand_forecasting >> torre_controle
    ml_platform >> [motor_servicos, motor_promocoes]
    
    # Infrastructure Dependencies
    [containers, serverless] >> storage
    identity >> security >> monitoring
    
    # Legacy Integration (Gradual Migration)
    mainframe >> Edge(label="Migração Gradual", style="dashed") >> containers
    sap_erp >> integration_layer
    legacy_db >> Edge(label="Data Migration", style="dashed") >> data_lake
    
    # Cross-cutting Concerns
    monitoring >> Edge(label="Observability", style="dotted", color="gray") >> [api_gateway, oms, data_warehouse]
    security >> Edge(label="Security", style="dotted", color="red") >> [api_gateway, cdp, hub_pagamentos]
    event_bus >> Edge(label="Events", style="dotted", color="blue") >> [oms, motor_cdc, loyalty]

# Diagrama complementar para Quick Wins
with Diagram("GCB Quick Wins - Implementação Faseada", 
             filename="gcb_quick_wins_phases", 
             show=False,
             graph_attr=graph_attr,
             direction="LR"):

    # FASE 1: Quick Wins (0-6 meses)
    with Cluster("🚀 FASE 1: Quick Wins (0-6M)"):
        
        with Cluster("Tier 0 (0-30 dias)"):
            qw_api = APIGateway("API Gateway")
            qw_cdn = CloudFront("CloudFront CDN")
            qw_analytics = Quicksight("QuickSight")
            qw_search = Blank("OpenSearch")
            
        with Cluster("Tier 1 (30-90 dias)"):
            qw_payments = Stripe("Payment Gateway")
            qw_monitoring = Cloudwatch("Monitoring")
            qw_crm_basic = Blank("CRM Basic")
            
        with Cluster("Tier 2 (90-180 dias)"):
            qw_pim = Blank("PIM Platform")
            qw_cdp = S3("CDP Basic")
            qw_ml_basic = Sagemaker("ML Basic")

    # FASE 2: Core Systems (6-12 meses)
    with Cluster("⚙️ FASE 2: Core Systems (6-12M)"):
        phase2_oms = Blank("OMS Complete")
        phase2_wms = Blank("WMS Integration")
        phase2_ecommerce = Blank("E-commerce Platform")
        phase2_data = Redshift("Data Warehouse")

    # FASE 3: Diferenciadores (12-18 meses)
    with Cluster("🎯 FASE 3: Diferenciadores (12-18M)"):
        phase3_cdc = ECS("CDC Customizado")
        phase3_ai = Personalize("AI Avançado")
        phase3_omni = Lambda("Omnichannel")

    # FASE 4: Otimização (18-24 meses)
    with Cluster("🏆 FASE 4: Otimização (18-24M)"):
        phase4_automation = Lambda("Full Automation")
        phase4_legacy_off = Blank("Legacy Decommission")
        phase4_scale = ECS("Auto Scaling")

    # Fluxo sequencial das fases
    qw_api >> phase2_oms >> phase3_cdc >> phase4_automation
    qw_payments >> phase2_ecommerce >> phase3_omni >> phase4_scale
    qw_analytics >> phase2_data >> phase3_ai >> phase4_legacy_off

print("✅ Diagramas gerados com sucesso!")
print("📁 Arquivos criados:")
print("   - gcb_architecture_blueprint.png")
print("   - gcb_quick_wins_phases.png")
print("\n🎯 Para executar:")
print("   pip install diagrams")
print("   python gcb_architecture.py")
