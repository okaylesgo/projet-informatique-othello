import pytest
import gameerror
import IA
import game
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
    state={"players": ["LUR", "LRG"],"current": 0,"board": [[28, 35,29,30],[27, 36,37,38]]}
    with pytest.raises(gameerror.BadMove):
        raise game.willBeTaken(state,0)
