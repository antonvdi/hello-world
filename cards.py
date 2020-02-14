import random

deck = []

class card(object):
    def __init__(self, number, color):
        self.number = number
        self.color = color

def create(color):
	for i in range(1, 14):
		deck.append(card(i, color))

def showcard(card):
	if card.number == 1:
		print("Ace" + card.color)
	elif card.number == 11:
		print("Jack" + card.color)
	elif card.number == 12:
		print("Queen" + card.color)
	elif card.number == 13:
		print("King" + card.color)
	else:
		print(str(card.number) + card.color)

create("♥")
create("♣")
create("♠")
create("♦")

for card in deck:
	showcard(card)

answer = input('Shuffle? y/n: \n')
if answer == "y":
	random.shuffle(deck)
	answer2 = input('Draw a card: \n')
	showcard(deck[int(answer2)])
elif answer == "n":
	pass
else:
	print("Wrong answer...")


	