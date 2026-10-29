# Consultor Avançado de Carreiras em TI (v2.0)

Este é um Sistema Especialista Baseado em Regras com Tratamento de Incerteza e Pontuação Ponderada. O sistema atua como um consultor inteligente, calculando a compatibilidade do usuário com 10 trilhas de carreira em TI, identificando "Skill Gaps" e gerando um roadmap personalizado.

## Diferenciais desta Versão (v2.0)
- **Desacoplamento de Conhecimento:** As regras e pesos não estão no código Python. O motor de inferência lê dinamicamente o arquivo `conhecimento.json`.
- **Entrada Gradual (Escala Likert):** O sistema não utiliza perguntas binárias, mas sim graus de afinidade (1 a 5) para um cálculo mais realista.
- **Motor de Inferência Ponderado:** Algoritmo matemático próprio que multiplica as respostas pelos pesos estabelecidos na matriz de decisão, gerando um Top 3 de compatibilidade (%).
- **Análise de Gaps:** Cruzamento do conhecimento atual do usuário com os requisitos da trilha recomendada para gerar um plano de ação focado.

## Tecnologias Utilizadas
- Python 3.10+
- Pandas (Tratamento de dados e geração de gráficos)
- JSON (Base de Conhecimento Desacoplada)
- Streamlit (Interface Web Multi-etapas)

