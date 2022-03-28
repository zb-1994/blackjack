from carddraw import *

print('Welcome to Backjack!\n')

name = input('Enter your name: ')

handCards = []

i = 0
while i <= 1:
    card = carddraw()
    handCards.append(card)
    i += 1

total = sum(handCards)
print(handCards)
print('Your cards are: {} and {}'.format(handCards[0],handCards[1]))
print('Your hand is {} points'.format(total))