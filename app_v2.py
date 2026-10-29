import streamlit as st
import pandas as pd
from motor_v2 import MotorInferenciaV2

st.set_page_config(page_title="Consultor Avançado TI", layout="wide")
st.title("🚀 Consultor Avançado de Carreiras em TI (v2.0)")

motor = MotorInferenciaV2()

tab1, tab2, tab3 = st.tabs(["Passo 1: Afinidades", "Passo 2: Nível Atual", "Passo 3: Diagnóstico e Roadmap"])

with tab1:
    st.header("Qual é o seu nível de afinidade com os seguintes temas?")
    st.write("Responda de 1 (Odeio/Não tenho) a 5 (Amo muito/Tenho muita).")
    
    mat = st.slider("Matemática, Estatística e Lógica Complexa", 1, 5, 3)
    logica = st.slider("Escrever códigos e algoritmos", 1, 5, 3)
    visual = st.slider("Design, Layouts e Experiência do Usuário (UI/UX)", 1, 5, 3)
    infra = st.slider("Servidores, Redes e Segurança", 1, 5, 3)
    negocios = st.slider("Gestão, Negócios e Comunicação com clientes", 1, 5, 3)

with tab2:
    st.header("Quais tecnologias/conceitos você já domina?")
    # Lista consolidada de todas as exigências das 10 trilhas
    opcoes_tech = [
        "Apache Spark ou Kafka", "Bancos de Dados (SQL/NoSQL)", "Conceitos OWASP Top 10", 
        "Conceitos de Alta Disponibilidade", "Conceitos de Testes de Software", 
        "Construção de APIs REST", "Consumo de APIs REST", "Criação de Casos de Teste", 
        "Docker & Containers", "Estatística Básica", "Ferramentas de Pentest (Kali)", 
        "Figma básico", "Framework (React/Vue/Angular)", "Fundamentos AWS/Azure/GCP", 
        "Fundamentos de Criptografia", "Git e CI/CD", "HTML/CSS Semântico", 
        "Infraestrutura como Código (Terraform)", "JavaScript ES6+", 
        "Linguagem OO (Java, C# ou Python)", "Linux (Linha de comando)", 
        "Levantamento de Requisitos", "Lógica de Programação e Algoritmos", 
        "Metodologias Ágeis (Scrum/Kanban)", "Modelagem de Dados", "Métricas de Produto", 
        "Pandas & Numpy", "Pipelines ETL em Nuvem", "Portfólio com páginas responsivas", 
        "Projeto de IA/ML no GitHub", "Projeto de automação (AWS/GCP)", 
        "Publicação nas Lojas", "Python Avançado", "React Native ou Flutter", 
        "Redes Básicas", "SQL e Bancos Relacionais", "Swift ou Kotlin", 
        "Testes Automatizados (Selenium/Cypress)", "Testes Unitários", "Técnicas de Priorização"
    ]
    conhecimentos_atuais = st.multiselect("Selecione o que já sabe:", sorted(opcoes_tech))

with tab3:
    st.header("🎯 Seu Diagnóstico Profissional")
    if st.button("Gerar Análise Completa"):
        
        # Envia as 5 respostas para o motor
        respostas = {"matematica": mat, "logica": logica, "visual": visual, "infra": infra, "negocios": negocios}
        top3 = motor.calcular_compatibilidade(respostas)
        
        st.subheader("🏆 Top 3 Trilhas Compatíveis")
        col1, col2, col3 = st.columns(3)
        col1.success(f"**1º {top3[0][0]}**\n\nCompatibilidade: {top3[0][1]}%")
        col2.info(f"**2º {top3[1][0]}**\n\nCompatibilidade: {top3[1][1]}%")
        col3.warning(f"**3º {top3[2][0]}**\n\nCompatibilidade: {top3[2][1]}%")
        
        df_grafico = pd.DataFrame(top3, columns=["Trilha", "Compatibilidade (%)"]).set_index("Trilha")
        st.bar_chart(df_grafico)
        
        trilha_vencedora = top3[0][0]
        st.subheader(f"🗺️ Roadmap Personalizado para {trilha_vencedora}")
        st.write("Baseado no seu conhecimento atual, aqui está o que falta para atingir o nível **Júnior**:")
        
        gaps = motor.gerar_roadmap(trilha_vencedora, conhecimentos_atuais)
        
        if len(gaps) == 0:
            st.success("Parabéns! Você já possui os requisitos básicos para começar como Júnior nesta área.")
        else:
            for gap in gaps:
                st.markdown(f"- 🔴 Precisa estudar: **{gap}**")