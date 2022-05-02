from game import possibleMoves
from game import isGameOver
import gameerror
import game
def Othello(players):
	# 00 01 02 03 04 05 06 07
	# 08 09 10 11 12 13 14 15
	# 16 17 18 19 20 21 22 23
	# 24 25 26 27 28 29 30 31
	# 32 33 34 35 36 37 38 39
	# 40 41 42 43 44 45 46 47
	# 48 49 50 51 52 53 54 55
	# 56 57 58 59 60 61 62 63

	state = {
		'players': players,
		'current': 0,
		'board': [
			[28, 35],
			[27, 36]
		]
	}
	def next(state, move):
			newState = copy.deepcopy(state)
			playerIndex = state['current']
			otherIndex = (playerIndex+1)%2
			if len(possibleMoves(state)) > 0 and move is None:
				raise gameerror.BadMove('You cannot pass your turn if there are possible moves')
			if move is not None:
				cases = game.willBeTaken(state, move)

				newState['board'][playerIndex].append(move)

				for case in cases:
					newState['board'][otherIndex].remove(case)
					newState['board'][playerIndex].append(case)
				
			newState['current'] = otherIndex
			
			return newState

	return state, next
init, next=Othello(['monsieurH','MADAMEF'])


import time
import copy

def winner(state):
	playerIndex = state['current']
	otherIndex = (playerIndex+1)%2
	winner=0
	if len(state['board'][playerIndex]) > len(state['board'][otherIndex]):
		winner = 1
	elif len(state['board'][playerIndex]) < len(state['board'][otherIndex]):
		winner = -1
	return winner

def heuristic(state,player):
	player=state['current']
	if player==0:
		player2=1
	elif player==1:
		player2=0
	if isGameOver(state):
		theWinner = winner(state)
		if theWinner is None:
			return 0
		if theWinner == player:
			return 10000
		return -10000
	res=0
	LISTCOIN=[0,7,56,63]
	LISTBORDS=[1,2,3,4,5,6,8,15,16,23,24,31,32,39,40,47,48,55,56,57,58,59,60,61,62,63]	
	for el in LISTCOIN:
		if el in state['board'][player]:
			res+=3
		elif el in state['board'][player2]:
			res-=3
	for el in LISTBORDS:
		if el in state['board'][player]:
			res+=1
		elif el in state['board'][player2]:
			res-=1
	res=res-len(game.possibleMoves({"players": ["h", "f"],"current": player2,"board": state['board']}))
	res=res+len(game.possibleMoves({"players": ["h", "f"],"current": player,"board": state['board']}))
	
	return res

from collections import defaultdict
init,next=Othello(['h','m'])
def negamaxWithPruningIterativeDeepening(state, player, timeout=0.2):
	cache = defaultdict(lambda : 0)
	def cachedNegamaxWithPruningLimitedDepth(state, player, depth, alpha=float('-inf'), beta=float('inf')):
		over = isGameOver(state)
		if over or depth == 0:
			res = -heuristic(state, player), None, over
		

		else:
			theValue, theMove, theOver = float('-inf'), None, True
			possibilities = [(move, next(state, move)) for move in possibleMoves(state)]
			possibilities.sort(key=lambda poss: cache[tuple(poss[1])])
			for move, successor in reversed(possibilities):
				value, _, over = cachedNegamaxWithPruningLimitedDepth(successor, player%2+1, depth-1, -beta, -alpha)
				theOver = theOver and over
				if value > theValue:
					theValue, theMove = value, move
				alpha = max(alpha, theValue)
				if alpha >= beta:
					break
			res = -theValue, theMove, theOver
			print(theMove)
		cache[tuple(state)] = res[0]
		return res

	value, move = 0, None
	depth = 1
	start = time.time()
	over = False
	while value > -10000 and time.time() - start < timeout and not over:
		value, move, over = cachedNegamaxWithPruningLimitedDepth(state, player, depth)
		depth += 1
		print(move)

	print('depth =', depth)
	return value, move



def timeit(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = fun(*args, **kwargs)
		print('Executed in {}s'.format(time.time() - start))
		return res
	return wrapper

@timeit
def IA2(state):
	player = state['current']
	_, move = negamaxWithPruningIterativeDeepening(state, player)
	print(move)
if 	__name__=="__main__":
	state={"players": ["LUR", "LRG"],"current": 0,"board": [[28, 35],[27, 36,37,38]]}
	init,next=Othello(['monsieurH','MADAMEF'])
	print(IA2(state))