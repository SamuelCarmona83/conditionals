import random # pseudo-random

pintas = ['♣', '♦', '♥', '♠']
valores = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# Definicion de la funcion

def generate_card():

    new_card = {
        "pinta": random.choice(pintas),
        "valor": random.choice(valores)
    }
    
    return new_card

mano = []

for _ in range(5):
    mano.append(generate_card())

print(mano)