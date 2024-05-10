class AgenteIA:
    def __init__(self):
        self.knowledge_base = {
            "Qual é a capital do Brasil?": "Brasília.",
            "Quantos anos Jonas têm?": "53.",
            "Qual é a cor do seu cabelo?": "Castanho."
        }

    def perguntar(self, pergunta):
        if pergunta in self.knowledge_base:
            return self.knowledge_base[pergunta]
        else:
            return "Desculpe, não sei a resposta para essa pergunta."
agente = AgenteIA()
pergunta1 = "Qual é a capital do Brasil?"
pergunta2 = "Quantos anos Jonas têm?"
pergunta3 = "Qual é a cor do seu cabelo?"
resposta1 = agente.perguntar(pergunta1)
resposta2 = agente.perguntar(pergunta2)
resposta3 = agente.perguntar(pergunta3)
print("Pergunta: ", pergunta1)
print("Resposta: ", resposta1)
print("Pergunta: ", pergunta2)
print("Resposta: ", resposta2)
print("Pergunta: ", pergunta3)
print("Resposta: ", resposta3)
