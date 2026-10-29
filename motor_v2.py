import json
import pandas as pd

class MotorInferenciaV2:
    def __init__(self, caminho_json="conhecimento.json"):
        # Lê a Base de Conhecimento Desacoplada
        with open(caminho_json, 'r', encoding='utf-8') as f:
            self.conhecimento = json.load(f)
            
    def calcular_compatibilidade(self, respostas_usuario):
        pontuacoes = {}
        
        # Pega os pesos de cada trilha do JSON
        trilhas = self.conhecimento["trilhas"]
        
        for trilha, pesos in trilhas.items():
            pontuacao_absoluta = 0
            pontuacao_maxima_possivel = 0
            
            # Multiplica a resposta do usuário pelo peso exigido pela trilha
            for atributo, peso in pesos.items():
                resposta = respostas_usuario.get(atributo, 1) # Resposta de 1 a 5
                pontuacao_absoluta += resposta * peso
                pontuacao_maxima_possivel += 5 * peso # O máximo seria responder 5 em tudo
                
            # Calcula a porcentagem de compatibilidade
            percentual = (pontuacao_absoluta / pontuacao_maxima_possivel) * 100
            pontuacoes[trilha] = round(percentual, 1)
            
        # Ordena para pegar o Top 3
        ranking_ordenado = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)
        return ranking_ordenado[:3]

    def gerar_roadmap(self, trilha_vencedora, conhecimentos_atuais):
        # Pega a lista do que um Júnior precisa saber
        habilidades_necessarias = set(self.conhecimento["roadmap_juniors"][trilha_vencedora])
        conhecimentos_atuais_set = set(conhecimentos_atuais)
        
        # Skill Gap (O que falta aprender = Necessário - Atual)
        gaps = habilidades_necessarias - conhecimentos_atuais_set
        return list(gaps)