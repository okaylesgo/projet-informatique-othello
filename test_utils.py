import pytest
import gameerror
import IA
import game
import IA2
import lancement
import message
state1={"players": ["LUR", "LRG"],"current": 0,"board": [[28, 35,29,30],[27, 36,37,38]]}
l1=[]
l2=[]
for i in range(32):
    l1.append(i)    
for i in range(32,64):
    l2.append(i)
state2={"layers": ["LUR", "LRG"],"current": 0,"board": [l1,l2]}
l3=[]
l4=[]
for i in range(62):
    l3.append(i)
for i in range(64):
    l4.append(i)
state3={"layers": ["LUR", "LRG"],"current": 0,"board": [l3,[62]]}
state4={"layers": ["LUR", "LRG"],"current": 0,"board": [l4,[]]}
def test_IA():
    init,next=game.Othello(['f','h'])
    assert IA.IA(state1) in game.possibleMoves(state1)
    l=[]
    for i in range(63):
        l.append(i)
    l.remove(0)
    state={"layers": ["LUR", "LRG"],"current": 0,"board": [[0],l]}
    assert IA.IA(state)==63
def test_game():
    init,next=game.Othello(['f','h'])
    with pytest.raises(gameerror.BadMove):
        raise game.willBeTaken(state1,94)
    with pytest.raises(gameerror.BadMove):
        raise next(state1,None)
    with pytest.raises(gameerror.GameDraw):
        raise next(state2,None)
    with pytest.raises(gameerror.GameWin):
        raise next(state3,63)
    end=gameerror.GameEnd(state4)
    print(end.state)
    print(end)
    winner=gameerror.GameWin(0,state4)
    print(winner)
    print(winner.winner)
    egalité=gameerror.GameDraw(state2)
    print(egalité)
    loop=gameerror.GameLoop(egalité)
    print(loop)
def test_IA2():
    assert IA2.IA2(state1) in game.possibleMoves(state1)
    with pytest.raises(gameerror.BadMove):
        raise IA2.next(state1,None)
import message
def test_message():
    state1={"players": ["LUR", "LRG"],"current": 0,"board": [[28, 35,29,30],[27, 36,37,38]]}
    state2={"players": ["LUR", "LRG"],"current": 0,"board": [l1,l2]}
    state3={"players": ["LUR", "LRG"],"current": 1,"board": [l3,[62]]}
    state4={"players": ["LUR", "LRG"],"current": 0,"board": [[12,13,14,28,34,35,35,29,30,31],[27, 36,37,38]]}
    state5={"players": ["LUR", "LRG"],"current": 0,"board": [[12,13,14,28,34],[27, 36,37,38,13,14,28,34,13,14,28,34]]}
    assert message.quelmessagejenvoie(state1)=='Toute facon je suis le meilleur'
    assert message.quelmessagejenvoie(state2)=='CEST TOUT CE QUE TU AS'
    assert message.quelmessagejenvoie(state3)=='haha mon reuf ^^ jrigolais tu peux te calmer?'

    assert message.quelmessagejenvoie(state5)== 'katchaw'
   