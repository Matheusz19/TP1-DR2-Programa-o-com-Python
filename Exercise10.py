import random

protagonistas = ["um homem", "um cavaleiro", "uma princesa", "um rei", "um mago"]
acoes = ["salvou", "encontrou", "perdeu", "desafiou", "ajudou"]
locais = ["em uma floresta encantada", "no topo de uma montanha", "em um castelo sombrio", "em uma cidade futurista", "em um reino submerso"]
antagonistas = ["um org", "um dragão", "um gigante", "um anão", "um robô"]

protagonista = random.choice(protagonistas)
acao = random.choice(acoes)
local = random.choice(locais)
antagonista = random.choice(antagonistas)

historia = f"Era uma vez {protagonista} que {acao} um segredo {local} de {antagonista}."
print(historia)