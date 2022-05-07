from game import possibleMoves
from game import isGameOver
import gameerror
import game
import threading
#IA utilisant l'approfondissement itératif
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
	winner=None
	if len(state['board'][playerIndex]) > len(state['board'][otherIndex]):
		winner = playerIndex
	elif len(state['board'][playerIndex]) < len(state['board'][otherIndex]):
		winner = otherIndex
	return winner

def heuristic(state,player=None):
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
	LISTECENTRE=[27,28,35,36]
	for el in LISTCOIN:
		if el in state['board'][player]:
			res+=10
		elif el in state['board'][player2]:
			res-=10
	res=res-0.3*len(game.possibleMoves({"players": ["h", "f"],"current": player2,"board": state['board']}))
	res=res+0.3*len(game.possibleMoves(state))
	nombrepions=len(state['board'][player])+len(state['board'][player2])
	if nombrepions<32:
		for elem in LISTECENTRE:
			if elem in state['board'][player]:
				res+=5
		DELTAPION=len(state['board'][player2])-len(state['board'][player])
		res=res+DELTAPION/5
	if nombrepions>=32:
		for elmt in LISTBORDS:
			if elmt in state['board'][player]:
				res+=1
			elif elmt in state['board'][player2]:
				res-=1
			coord=game.coord(elmt)
			x,y=coord
			lelemnext=[]
			for el2 in LISTBORDS:
				if (elmt,el2) not in lelemnext or (el2,elmt) not in lelemnext: 
					for i in [-1,0,1]:
						if game.coord(el2) ==(x+i,y+i) :
							if elmt in state['board'][player] and el2 in state['board'][player] :
								res+=0.5
								lelemnext.append((el,el2))
								lelemnext.append((el2,el))
							elif elmt in state['board'][player2] and el2 in state['board'][player2]:
								res-=0.5
								lelemnext.append((el2,el))
		res=res-0.2*len(state['board'][player2])
		res=res+0.2*len(state['board'][player2])		
	return res			
from collections import defaultdict
init,next=Othello(['h','m'])
def negamaxWithPruningIterativeDeepening(state, player, timeout=8.0):
	global start
	start = time.time()
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
			cache[tuple(state)] = res[0]
			return res
	value,  move = 0, None
	depth = 1
	over = False
	def not10sec(state):
		nonlocal value
		nonlocal move
		nonlocal over
		nonlocal depth
		nonlocal player
		nonlocal timeout
		value, move, over = cachedNegamaxWithPruningLimitedDepth(state, player, depth)
		depth += 1
		if depth>(64-(len(state['board'][1])+len(state['board'][0]))):
			timeout=0
		print('depth =', depth)
	A=True
	def concurrence():
		nonlocal A
		while A==True:
			not10sec(state)
	thread=threading.Thread(target=concurrence,args=())
	thread.start()
	while time.time() - start<timeout :
		None
	A=False
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
	return move
