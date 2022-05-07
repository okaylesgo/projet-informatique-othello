import game
import gameerror
#IA de secours au cas où la deuxième IA a un souci.
def IA(requete):
    a=requete['current']
    init,next=game.Othello(['monsieurH','MADAMEF']) 
    plusgrand=0
    indice=None
    for i in range(64):
        try:                           
            etat=next(requete,i)
            if len(etat['board'][a])>plusgrand:
                plusgrand=len(etat['board'][a])
                indice=i
        
        except gameerror.BadMove:
                None
        except gameerror.GameWin as win:
            ETAT=requete['board']
            if i not in ETAT[0] and ETAT[1]:
                return i  
        except gameerror.GameDraw:
            ETAT=requete['board']
            if i not in ETAT[0] and ETAT[1]:
                return i
    return indice