# Import libraries
# -----------------

from random import random

player_1_score=0
player_2_score=0

# Import libraries
# -----------------

def play_tennis(playing):

	global player_1_score
	global player_2_score

	print("Score = {}/{}".format(player_1_score,player_2_score))
	
	if playing is True:
		# Coin flip to see who serves
		coin_flip=random()
		if coin_flip > 0.5:
			print("Player 2 Serves")
			chance_to_hit = random()
			if chance_to_hit > 0.5:
				print("Player 2 serves successfully!")
				tennis_player_1()
			else:
				print("Player 2 missed the serve and tries again...")
				chance_to_hit = random()
				if chance_to_hit > 0.5:
					print("Player 2 serves successfully!")
					tennis_player_1()
				else:
					print("Player 2 screwed up. Player 1 gets a point.")
					play_tennis(True)
		else:
			print("Player 1 Serves")
			tennis_player_2()
	else:
		# Winning conditions
		if player_1_score==40:
			print("Player 1 Wins!")
		if player_2_score==40:
			print("Player 2 Wins!")

	
# Turn: Player 1
# -----------------
def tennis_player_1():

	global player_1_score
	global player_2_score

	chance_to_hit = random()
	if chance_to_hit > 0.5:
		# Hit
		print("Player 1 hits the ball!")
		tennis_player_2()
	else:
		# Miss
		print("Player 1 misses! Player 2 gets a point")
		if player_2_score == 30:
			player_2_score = 40
			play_tennis(False)
		if player_2_score == 15:
			player_2_score = 30
			play_tennis(True)
		if player_2_score == 0:
			player_2_score = 15
			play_tennis(True)
	
# Turn: Player 2
# -----------------
def tennis_player_2():

	global player_1_score
	global player_2_score

	chance_to_hit = random()
	if chance_to_hit > 0.5:
		# Hit
		hit=True
		print("Player 2 hits the ball!")
		tennis_player_1()
	else:
		# Miss
		hit=False
		print("Player 2 misses! Player 1 gets a point")
		if player_1_score == 30:
			player_1_score = 40
			play_tennis(False)
		if player_1_score == 15:
			player_1_score = 30
			play_tennis(True)
		if player_1_score == 0:
			player_1_score = 15
			play_tennis(True)

# Initiate game
# -----------------
play_tennis(True)
