import random
import os
class Cartes:
	def __init__(self):
		self.total_cards = ([], 149)
		self.discard_pile = []
		self.card_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		self.hidden_card_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		self.pseudo = "user"
		self.player_card_count = 12
		self.score = 0
		self.end = False
		
	def createDeck(self):
		self.c = [ -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
					0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
					1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,
					2,  2,  2,  2,  2,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,
					4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  5,  5,  5,  5,  5,
					5,  5,  5,  5,  5,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,
					7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  8,  8,  8,  8,  8,
					8,  8,  8,  8,  8,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,
					10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11,
					11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12 ]
		
		self.removed_card_count = 0
		self.total_cards = (self.c, 149 - self.removed_card_count)
		
	def initGrid(self):
		self.player_card_count = 12
		for i in range(0, 3):
			for j in range(0, 4):
				removed_card = self.c[random.randint(0, 149 - self.removed_card_count)]
				self.card_grid[i][j] = removed_card
				for k in range(0, 149 - self.removed_card_count):
					if self.c[k] == removed_card:
						self.c.pop(k)
						self.removed_card_count += 1
						break
						
	def createPlayer(self):
		self.pseudo = str(input("Choisis ton pseudo : "))
		

	def display(self):
		print(self.pseudo)
		self.currentScore()
		print("Score : ", self.score)
		for i in range(len(self.card_grid)):
			row = []

			for j in range(len(self.card_grid[0])):
				if self.hidden_card_grid[i][j] == 1:
					row.append(str(self.card_grid[i][j]))
				else:
					row.append("▯")

			print("\t".join(row))

	def skijo(self):
		for j in range(len(self.card_grid[0])):
			col = [self.card_grid[i][j] for i in range(3) if i < len(self.card_grid) and j < len(self.card_grid[0])]
			if len(col) == 3 and col[0] == col[1] == col[2] and all(self.hidden_card_grid[i][j] == 1 for i in range(3)):
				for i in range(3):
					self.discard_pile.append(self.card_grid[i][j])
					del self.hidden_card_grid[i][j]
					del self.card_grid[i][j]
				print("SKIJO DE", self.discard_pile[len(self.discard_pile) - 1], "!")
				self.player_card_count -= 3
				self.display()
					
	def draw(self):
		discard_card = 0
		drawn_card = self.c[random.randint(0, 149 - self.removed_card_count)]
		for k in range(0, 149 - self.removed_card_count):
			if self.c[k] == drawn_card:
				del(self.c[k])
				self.removed_card_count += 1
				break
		print("La carte piocher est : ", drawn_card)
		while True:
			choice = str(input("Choisissez l'action : R(emplacer) ou (D)éfausser la carte : "))
			while choice != "R" and choice != 'r' and choice != "D" and choice != "d":
				print("Resaisissez votre demande")
				choice = str(input("Choisissez l'action : R(emplacer) ou (D)éfausser la carte : "))
			if choice == "R" or choice == "r":
				ccase = int(input("Colonne de la case à changer : "))
				while ccase != 1 and ccase != 2 and ccase != 3 and ccase != 4:
					print("Rentrez un entier (1, 2, 3 ou 4)")
					ccase = int(input("Colonne de la case à changer : "))
				rcase = int(input("Ligne de la case à changer : "))
				while rcase != 1 and rcase != 2 and rcase != 3:
					print("Rentrez un entier (1, 2 ou 3)")
					rcase = int(input("Colonne de la case à changer : "))
				self.hidden_card_grid[rcase - 1][ccase - 1] = 1
				discard_card = self.card_grid[rcase - 1][ccase - 1]
				print("La carte que vous avez remplacé etait un ", discard_card)
				self.discard_pile.append(discard_card)
				self.card_grid[rcase - 1][ccase - 1] = drawn_card
				self.display()
				if len(self.discard_pile) == 0:
					print("defausse vide")
				else:
					print("dernière carte de la défausse ->", self.discard_pile[len(self.discard_pile)-1])
			else:
				self.discard_pile.append(drawn_card)
				print("choisissez une carte à découvrir")
				ccard = int(input("Colonne de la carte à retourner : "))
				while ccard != 1 and ccard != 2 and ccard != 3 and ccard != 4:
					print("Rentrez un entier (1, 2, 3 ou 4)")
					ccard = int(input("Colonne de la carte à retourner : "))
				rcard = int(input("Ligne de la carte à retourner : "))
				while rcard != 1 and rcard != 2 and rcard != 3:
					print("Rentrez un entier (1, 2 ou 3)")
					rcard = int(input("Ligne de la carte à retourner : "))
				self.hidden_card_grid[rcard - 1][ccard - 1] = 1
				self.display()
				if len(self.discard_pile) == 0:
					print("defausse vide")
				else:
					print("dernière carte de la défausse ->", self.discard_pile[len(self.discard_pile)-1])
			break

	def getCardDeleted(self):
		caget = self.discard_pile[len(self.discard_pile)-1]
		self.discard_pile.pop()
		print("Vous avez pris la carte ", caget)
		jcase = int(input("Colonne de la carte à changer : "))
		while jcase != 1 and jcase != 2 and jcase != 3 and jcase != 4:
			print("Rentrez un entier (1, 2, 3 ou 4)")
			jcase = int(input("Colonne de la carte à changer : "))
		icase = int(input("Ligne de la carte à changer : "))
		while icase != 1 and icase != 2 and icase != 3 and icase != 4:
			print("Rentrez un entier (1, 2, 3 ou 4)")
			icase = int(input("Ligne de la carte à changer : "))
		ca_defauss = self.card_grid[icase - 1][jcase - 1]
		self.discard_pile.append(ca_defauss)
		self.card_grid[icase - 1][jcase - 1] = caget
		self.hidden_card_grid[icase - 1][jcase - 1] = 1
		self.display()
		if len(self.discard_pile) == 0:
			print("defausse vide")
		else:
			print("dernière carte de la défausse ->", self.discard_pile[len(self.discard_pile)-1])

		
			
	def currentScore(self):
		self.score = 0

		for i in range(len(self.card_grid)):
			for j in range(len(self.card_grid[0])):
				if self.hidden_card_grid[i][j] == 1:
					self.score += self.card_grid[i][j]
	
	def scoreEnd(self):
		self.score = 0

		for i in range(len(self.card_grid)):
			for j in range(len(self.card_grid[0])):
				self.score += self.card_grid[i][j]

	def finish(self):
		self.end = True
		if self.player_card_count == 0:
			self.end = True
			return self.end
		for i in range(len(self.hidden_card_grid)):
			for j in range(len(self.hidden_card_grid[0])):
				if self.hidden_card_grid[i][j] == 0:
					self.end = False
					break
			else:
				continue
			break
		return self.end

	def start(self):
		self.display()
		print("Vous devez retourner deux cartes de votre jeu pour commencer")
		column_start_card_1 = int(input("Colonne de la première carte à retourner : "))
		while column_start_card_1 != 1 and column_start_card_1 != 2 and column_start_card_1 != 3 and column_start_card_1 != 4:
			print("Rentrez un entier (1, 2, 3 ou 4)")
			column_start_card_1 = int(input("Colonne de la première carte à retourner : "))
		line_start_card_1 = int(input("Ligne de la première carte à retourner : "))
		while line_start_card_1 != 1 and line_start_card_1 != 2 and line_start_card_1 != 3 and line_start_card_1 != 4:
			print("Rentrez un entier (1, 2, 3 ou 4)")
			line_start_card_1 = int(input("Ligne de la première carte à retourner : "))
		self.hidden_card_grid[line_start_card_1 - 1][column_start_card_1 - 1] = 1
		self.display()
		column_start_card_2 = int(input("Colonne de la deuxième carte à retourner : "))
		while column_start_card_2 != 1 and column_start_card_2 != 2 and column_start_card_2 != 3 and column_start_card_2 != 4:
			print("Rentrez un entier (1, 2, 3 ou 4)")
			column_start_card_2 = int(input("Colonne de la deuxième carte à retourner : "))
		line_start_card_2 = int(input("Ligne de la deuxième carte à retourner : "))
		while line_start_card_2 != 1 and line_start_card_2 != 2 and line_start_card_2 != 3 and line_start_card_2 != 4:
			print("Rentrez un entier (1, 2, 3 ou 4)")
			line_start_card_2 = int(input("Ligne de la deuxième carte à retourner : "))
		self.hidden_card_grid[line_start_card_2 - 1][column_start_card_2 - 1] = 1
		os.system('cls' if os.name == 'nt' else 'clear')
		self.display()


	def jeuexe(self):
		print("\nprochain tour !")
		self.currentScore()
		self.display()
		if len(self.discard_pile) == 0:
			print("defausse vide")
		else:
			print("dernière carte de la défausse ->", self.discard_pile[len(self.discard_pile)-1])
		if self.discard_pile == []:
			choice = str(input("La defausse est vide, (p)iochez : "))
			self.draw()
		else:
			choice = str(input("Prendre la (c)arte de la defausse ou (p)iocher : "))
			while choice != 'p' and choice != 'P' and choice != 'c' and choice != 'C':
				print("Resaisissez votre demande")
				choice = str(input("Prendre la (c)arte de la defausse ou (p)iocher : "))
			if choice == 'p' or choice == 'P':
				self.draw()
			else:
				self.getCardDeleted()
			
		self.skijo()
		self.currentScore()


def jeu():
	players = []
	nb_j = int(input("nombre de joueurs (2 - 8) : "))
	while nb_j > 8 or nb_j < 2:
		print("Entrez un entier entre 2 et 8")
		nb_j = int(input("nombre de joueurs (2 - 8) : "))

	for _ in range(nb_j):
		player = Cartes()
		player.createPlayer()
		player.createDeck()
		players.append(player)
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	for i in range(nb_j):
		players[i].initGrid()
		for j in range(nb_j):
			if i != j:
				players[j].c = players[i].c.copy()
				players[j].removed_card_count = players[i].removed_card_count
				players[j].total_cards = players[i].total_cards

	for player in players:
		player.start()

	sorted(players, key=lambda p: p.score, reverse=True)
	print(f"Le joueur qui a le moins de point commence {players[0].pseudo} !")
	player_end = None
	while all(not(player.finish()) for player in players):
		for player in players:
			player.jeuexe()
			for player2 in players:
				if player2 != player:
					player2.discard_pile = player.discard_pile
					player2.c = player.c
					player2.removed_card_count = player.removed_card_count
					player2.total_cards = player.total_cards
	
	for player in players:	
		if player_end is None and player.finish():
			player_end = player.pseudo

	for player in players:
		for player in players:
			player.scoreEnd()
		if player_end == player.pseudo:
			print(f"Le joueur qui a finit la partie est {player_end} avec un score de {player.score}")
			if player.score > max([p.score for p in players if p != player]):
				player.score += 10
				print(f"{player_end} prends 10 points supplémentaires car il n'a pas le plus petit score")
	
	winner = min(players, key=lambda p: p.score)

	print(f"\nLe gagnant de la partie est {winner.pseudo} avec un score de {winner.score}")
	print("Scores des joueurs:")
	for player in players:
		player.hidden_card_grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
		player.display()

jeu()
