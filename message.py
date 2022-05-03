def quelmessagejenvoie(state):
    player=state['current']
    if player==0:
        player2=1
    elif player==1:
        player2=0
    if len(state['board'][player])+len(state['board'][player2])<10:
        return 'Toute facon je suis le meilleur'
    elif len(state['board'][player])+len(state['board'][player2])>=10:
        if len(state['board'][player2])-len(state['board'][player])>10:
            return 'haha mon reuf ^^ jrigolais tu peux te calmer?'
        elif len(state['board'][player2])-len(state['board'][player])<5:
            return 'CEST TOUT CE QUE TU AS'
        else:
            return 'katchaw'
