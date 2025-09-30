import random

def raffle_draw(participants):
    winner = random.sample(participants, 1)
    return winner[0]

participants = ['faruk', 'rafi', 'rafa', 'faru', 'faruk']
print("Winner:", raffle_draw(participants))


def raffle_draw(participants):
    return random.choice(participants)

participants = ['faruk', 'rafi', 'rafa', 'faru', 'faruk']
print("Winner:", raffle_draw(participants))
