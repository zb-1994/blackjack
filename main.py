from carddraw import *

print('Welcome to Backjack!\n')

#name = input('Enter your name: ')

p_handCards = []
d_handCards = []

p = 0
while p <= 1:
    p_card = carddraw()
    p_handCards.append(p_card)
    p += 1
p_total = sum(p_handCards)

d = 0
while d <= 1:
    d_card = carddraw()
    d_handCards.append(d_card)
    d += 1
d_total = sum(d_handCards)

print('Your cards are: {} and {}'.format(p_handCards[0],p_handCards[1]))
print('Dealer cards are: {} and {}'.format(d_handCards[0],d_handCards[1]))
print('Your hand is {} points'.format(p_total))
print('Dealer hand is {} points'.format(d_total))

if p_total > d_total:
    print('You win')
elif d_total > p_total:
    print('Dealer won')
else:
    print('Push. No winner.') 