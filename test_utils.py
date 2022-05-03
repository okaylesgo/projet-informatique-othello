import pytest
import gameerror
import IA
import game
import lancement
import inscription
import IA2
def test_IA():
    init,next=game.Othello(['f','h'])
    state={"players": ["LUR", "LRG"],"current": 0,"board": [[28, 35,29,30],[27, 36,37,38]]}
    assert IA.IA(state) in game.possibleMoves(state)
    l=[]
    for i in range(63):
        l.append(i)
    l.remove(0)
    state={"layers": ["LUR", "LRG"],"current": 0,"board": [[0],l]}
    assert IA.IA(state)==63
def test_game():
    init,next=game.Othello(['f','h'])
    state1={"players": ["LUR", "LRG"],"current": 0,"board": [[28, 35,29,30],[27, 36,37,38]]}
    with pytest.raises(gameerror.BadMove):
        raise game.willBeTaken(state1,94)
    with pytest.raises(gameerror.BadMove):
        raise next(state1,None)
    l1=[]
    l2=[]
    for i in range(32):
        l1.append(i)
        
    for i in range(32,64):
        l2.append(i)
    state2={"layers": ["LUR", "LRG"],"current": 0,"board": [l1,l2]}
    with pytest.raises(gameerror.GameDraw):
        raise next(state2,None)
    l3=[]
    l4=[]
    for i in range(62):
        l3.append(i)
    for i in range(64):
        l4.append(i)
    state3={"layers": ["LUR", "LRG"],"current": 0,"board": [l3,[62]]}
    state4={"layers": ["LUR", "LRG"],"current": 0,"board": [l4,[]]}
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